"""Supplier Notice Extractor — LangChain structured output + Ollama.

The LLM classifies each free-text supplier email, then extracts the details for that kind of notice; Python
checks each one against stock cover, open orders and the supplier contract; the LLM writes the buyer's action list.

Run:  python 02_retail/09_supplier_notice_extractor/app.py
"""

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Literal

sys.path.append(str(Path(__file__).resolve().parents[2]))
from pydantic import BaseModel, Field

from common import banner, run_chain, run_structured, section

TODAY = date(2026, 10, 10)
EMAILS = [
    ("Nordic Dairy Co", "Hi team, PO 4471: due to a tanker shortage, delivery of Organic oat milk 1L (SKU-101) "
     "moves from 14 Oct 2026 to 21 Oct 2026. Quantity unchanged at 1,200 units. Apologies for the trouble."),
    ("SunShield Labs", "Please note that from 1 Nov 2026 the cost price of Sunscreen SPF50 200ml (SKU-102) will "
     "increase from 4.80 to 5.30 per unit, due to higher raw material costs."),
    ("WoolWorks Ltd", "Re PO 4485: we can only ship 120 of the 200 Wool scarf (grey) units ordered (SKU-103) this "
     "week. The balance of 80 will follow in about 3 weeks."),
    ("PastaPrima", "Good news! From the next order (PO 4490), Pasta sauce 500g (SKU-210) is replaced by our new "
     "450g jar, at the same cost price of 1.60 per unit."),
]
# What our systems know (normally ERP / inventory / contract database)
STOCK = {"SKU-101": {"units": 600, "weekly_sales": 470}, "SKU-102": {"units": 380, "weekly_sales": 260},
         "SKU-103": {"units": 640, "weekly_sales": 15}, "SKU-210": {"units": 1100, "weekly_sales": 300}}
CONTRACT = {"max_increase_pct": 3.0, "min_notice_days": 60}


# Step 1: what kind of notice is it?
class NoticeType(BaseModel):
    notice_type: Literal["delay", "price_change", "short_shipment", "substitution", "other"] = Field(
        description="delay = delivery date moved; price_change = cost price going up or down for the same product; "
                    "short_shipment = fewer units shipped than ordered; substitution = product replaced by a "
                    "different product or pack size, even if the price stays the same")
    sku: str = Field(description="SKU code, e.g. SKU-101")


# Step 2: a small schema per notice type (small models fill short, specific schemas far more reliably)
class Delay(BaseModel):
    original_date: str = Field(description="Original delivery date, e.g. 14 Oct 2026")
    new_date: str = Field(description="New delivery date, e.g. 21 Oct 2026")


class PriceChange(BaseModel):
    old_cost: float = Field(description="Current cost price per unit")
    new_cost: float = Field(description="New cost price per unit")
    effective_date: str = Field(description="Date the new price starts, e.g. 1 Nov 2026")


class ShortShipment(BaseModel):
    qty_ordered: int = Field(description="Units ordered on the purchase order")
    qty_shipped: int = Field(description="Units the supplier is shipping now")


class Substitution(BaseModel):
    old_pack_size: float = Field(description="Old pack size in g or ml, e.g. 500")
    new_pack_size: float = Field(description="New pack size in g or ml, e.g. 450")


DETAILS = {"delay": Delay, "price_change": PriceChange, "short_shipment": ShortShipment, "substitution": Substitution}


def days_until(text: str | None) -> int | None:
    """Days from today to the date found in the model's text ('2026-10-21...', '21 Oct 2026', '21 October 2026')."""
    if m := re.search(r"\d{4}-\d{2}-\d{2}", text or ""):
        return (date.fromisoformat(m.group()) - TODAY).days
    if m := re.search(r"(\d{1,2}) ([A-Za-z]{3})[a-z]* (\d{4})", text or ""):
        return (datetime.strptime(" ".join(m.groups()), "%d %b %Y").date() - TODAY).days
    return None


def check(supplier: str, kind: str, sku: str, d: dict) -> dict:
    """Business impact of one notice, from stock cover and contract terms."""
    s = STOCK.get(sku, {"units": 0, "weekly_sales": 0})
    cover_days = round(s["units"] / s["weekly_sales"] * 7, 1) if s["weekly_sales"] else None
    out = {"supplier": supplier, "sku": sku, "type": kind, "days_of_stock_cover": cover_days}
    if kind == "delay" and (days := days_until(d["new_date"])) is not None:
        out |= {"delivery_in_days": days, "stockout_risk": cover_days is not None and days > cover_days,
                "days_without_stock": max(round(days - cover_days), 0) if cover_days else None}
    elif kind == "price_change":
        pct = (d["new_cost"] / d["old_cost"] - 1) * 100
        notice = days_until(d["effective_date"])
        short_notice = notice is not None and notice < CONTRACT["min_notice_days"]
        out |= {"increase_pct": round(pct, 1), "notice_days": notice,
                "breaches_contract": pct > CONTRACT["max_increase_pct"] or (pct > 0 and short_notice),
                "contract_terms": f"max {CONTRACT['max_increase_pct']}% increase, {CONTRACT['min_notice_days']} days notice",
                "extra_cost_per_year": round((d["new_cost"] - d["old_cost"]) * s["weekly_sales"] * 52)}
    elif kind == "short_shipment":
        out |= {"shortfall_units": d["qty_ordered"] - d["qty_shipped"],
                "stockout_risk": cover_days is not None and cover_days < 21,   # balance arrives in ~3 weeks
                "overstocked_so_cancel_balance": cover_days is not None and cover_days > 120}
    elif kind == "substitution":
        out |= {"pack_change": f"{d['old_pack_size']:g} -> {d['new_pack_size']:g}",
                "hidden_cost_increase_pct": round((d["old_pack_size"] / d["new_pack_size"] - 1) * 100, 1),
                "needs": "new barcode, product listing and shelf-edge unit price"}
    return out


CLASSIFY = ("Classify this supplier email and find the SKU it is about. A new pack size or replacement product is "
            "a substitution, not a price change.")
SYSTEM = (
    "You are a retail buyer's assistant. From the checked supplier notices, write a prioritised action list: "
    "stock-out risks first, then contract breaches, then everything else. For each: what happened, the impact "
    "(quote the numbers given, never recalculate) and the action (e.g. expedite or find another supplier, push "
    "back on the price citing the contract terms, cancel the balance of an order we don't need, update listings "
    "and shelf labels). Under 250 words."
)


def main():
    banner("Retail 09 - Supplier Notice Extractor (LangChain structured output)")
    checks = []
    for supplier, text in EMAILS:
        email = f"From: {supplier}\n\n{text}"
        head = run_structured(CLASSIFY, email, NoticeType)
        details = {}
        if head.notice_type in DETAILS:
            details = run_structured("Extract these details from the supplier email.", email,
                                     DETAILS[head.notice_type]).model_dump()
        section(supplier, json.dumps({**head.model_dump(), **details}, indent=2))
        checks.append(check(supplier, head.notice_type, head.sku, details))
    section("Validation", json.dumps(checks, indent=2))
    section("Action list", run_chain(SYSTEM, "Checked notices:\n{c}", c=json.dumps(checks, indent=2)))


if __name__ == "__main__":
    main()
