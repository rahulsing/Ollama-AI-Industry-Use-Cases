"""Dynamic Pricing Advisor — CrewAI + Ollama.

Python proposes guard-railed prices (margin floor, max change); agents review and write the pricing memo.

Run:  python 02_retail/03_dynamic_pricing_advisor/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

PRODUCTS = [  # elasticity: % change in volume for a 1% price change
    {"sku": "P-1", "name": "Wireless earbuds", "cost": 21.0, "price": 49.99, "competitor_prices": [44.99, 46.50, 45.00],
     "weekly_units": 320, "weeks_of_stock": 3.0, "elasticity": -1.8},
    {"sku": "P-2", "name": "Stainless water bottle 750ml", "cost": 6.2, "price": 14.99, "competitor_prices": [17.99, 18.50, 16.99],
     "weekly_units": 540, "weeks_of_stock": 6.0, "elasticity": -1.1},
    {"sku": "P-3", "name": "Fleece throw blanket", "cost": 9.5, "price": 29.99, "competitor_prices": [27.99, 29.00, 31.50],
     "weekly_units": 85, "weeks_of_stock": 22.0, "elasticity": -2.2},
]
MIN_MARGIN = 0.30      # never price below 30% gross margin
MAX_CHANGE = 0.10      # move at most 10% at a time


def propose(p: dict) -> dict:
    comp = sum(p["competitor_prices"]) / len(p["competitor_prices"])
    gap = (p["price"] / comp - 1) * 100
    target = comp
    reason = f"Move toward competitor average ({gap:+.1f}% vs competitors)"
    if p["weeks_of_stock"] > 12:          # overstock: price to clear
        target = min(comp, p["price"]) * 0.95
        reason = f"Overstock ({p['weeks_of_stock']} weeks of stock): cut to clear"
    elif p["weeks_of_stock"] < 4:         # low stock: no need to discount
        target = max(target, p["price"])
        reason = (f"Low stock ({p['weeks_of_stock']} weeks): hold price even though it is {gap:+.1f}% vs "
                  f"competitors, to avoid selling out")
    lo, hi = p["price"] * (1 - MAX_CHANGE), p["price"] * (1 + MAX_CHANGE)
    floor = p["cost"] / (1 - MIN_MARGIN)
    new = round(max(min(max(target, lo), hi), floor), 2)
    if new == round(hi, 2) and target > hi:
        reason += f"; capped at the {MAX_CHANGE:.0%} max move"
    change = new / p["price"] - 1
    units = p["weekly_units"] * (1 + p["elasticity"] * change)
    profit_now = (p["price"] - p["cost"]) * p["weekly_units"]
    profit_new = (new - p["cost"]) * units
    return {"sku": p["sku"], "name": p["name"], "current_price": p["price"], "competitor_avg": round(comp, 2),
            "proposed_price": new, "change_pct": round(change * 100, 1), "margin_pct": round((new - p["cost"]) / new * 100, 1),
            "expected_weekly_units": round(units), "weekly_gross_profit_now": round(profit_now),
            "weekly_gross_profit_new": round(profit_new), "weeks_of_stock": p["weeks_of_stock"], "pricing_reason": reason}


def main():
    banner("Retail 03 - Dynamic Pricing Advisor (CrewAI)")
    proposals = [propose(p) for p in PRODUCTS]
    section("Guard-railed price proposals", json.dumps(proposals, indent=2))

    analyst = make_agent("Pricing Analyst", "Explain each proposed price using competitors, stock and elasticity",
                         "Retail pricing analyst who balances volume, margin and price perception.")
    manager = make_agent("Category Manager", "Approve, adjust or reject each price change and write the pricing memo",
                         "You own the category P&L and protect customer trust (no confusing price swings).")
    t1 = make_task("Proposals (exact figures):\n{proposals}\n\nGuardrails: minimum margin 30%, max change 10% per move.\n\n"
                   "Explain the rationale (start from pricing_reason) and risks of each proposal.", "Per-SKU rationale and risks.", analyst)
    t2 = make_task("Proposals (exact figures; quote these, never recalculate):\n{proposals}\n\n"
                   "Decide APPROVE / ADJUST / REJECT per SKU and write a short pricing memo. Base each reason on pricing_reason.",
                   "Memo: decision table (SKU, current, proposed, decision, reason), expected profit impact, "
                   "and notes for marketing and store teams.", manager, context=[t1])
    section("Pricing memo", run_crew([analyst, manager], [t1, t2], {"proposals": json.dumps(proposals, indent=2)}))


if __name__ == "__main__":
    main()
