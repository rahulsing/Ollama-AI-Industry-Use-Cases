"""Letter of Credit Document Checker — CrewAI + Ollama.

Run:  python 01_banking/44_trade_finance_lc_checker/app.py
"""

import json
import sys
from datetime import date
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

LC = {"number": "LC/2026/0458", "applicant": "Brightway Retail Ltd, Mumbai", "beneficiary": "Shenzhen Lumen Electronics Co",
      "amount": 120_000, "currency": "USD", "tolerance_pct": 5, "goods": "5,000 units LED panel lights model LP-60",
      "incoterm": "CIF Nhava Sheva", "latest_shipment": "2026-09-30", "expiry": "2026-10-20", "presentation_days": 21,
      "port_loading": "Shenzhen", "port_discharge": "Nhava Sheva", "partial_shipment": "Not allowed",
      "docs_required": ["Commercial invoice", "Full set clean on-board B/L", "Insurance certificate 110% CIF", "Packing list"]}

PRESENTATION = {
    "presented_on": "2026-10-16",
    "invoice": {"beneficiary": "Shenzhen Lumen Electronics Co", "amount": 126_500, "currency": "USD",
                "goods": "5,000 units LED panel lights model LP-60", "incoterm": "CIF Nhava Sheva"},
    "bill_of_lading": {"on_board_date": "2026-09-22", "port_loading": "Shenzhen", "port_discharge": "Nhava Sheva",
                       "clean": False, "clause": "3 cartons wet and torn", "originals": "3/3"},
    "insurance": {"coverage": 126_500, "currency": "USD", "date": "2026-09-24"},
    "packing_list": {"units": 5000},
}


def check() -> list[str]:
    d, inv, bl, ins = [], PRESENTATION["invoice"], PRESENTATION["bill_of_lading"], PRESENTATION["insurance"]
    max_amt = LC["amount"] * (1 + LC["tolerance_pct"] / 100)
    if inv["amount"] > max_amt: d.append(f"Invoice amount {inv['amount']:,} exceeds LC amount + tolerance {max_amt:,.0f}")
    if inv["goods"] != LC["goods"]: d.append("Goods description on invoice differs from LC")
    if bl["on_board_date"] > LC["latest_shipment"]: d.append("Late shipment")
    if not bl["clean"]: d.append(f"B/L is claused: '{bl['clause']}' (LC requires clean on-board B/L)")
    if ins["date"] > bl["on_board_date"]: d.append(f"Insurance dated {ins['date']} after shipment date {bl['on_board_date']}")
    if ins["coverage"] < 1.1 * inv["amount"]: d.append(f"Insurance cover {ins['coverage']:,} < 110% of invoice ({1.1 * inv['amount']:,.0f})")
    days = (date.fromisoformat(PRESENTATION["presented_on"]) - date.fromisoformat(bl["on_board_date"])).days
    if days > LC["presentation_days"]: d.append(f"Presented {days} days after shipment (> {LC['presentation_days']})")
    if PRESENTATION["presented_on"] > LC["expiry"]: d.append("Presented after LC expiry")
    return d


def main():
    banner("44 - Letter of Credit Document Checker (CrewAI)")
    disc = check()
    section("Discrepancies found", "\n".join(disc) or "None")
    checker = make_agent("LC Document Checker", "Examine documents strictly per UCP 600 and ISBP",
                         "Senior trade documentation checker; you cite the relevant UCP 600 article where possible.")
    ops = make_agent("Trade Operations Manager", "Decide how to handle the presentation",
                     "You decide between paying, refusing, or seeking applicant waiver, and draft the SWIFT MT734 refusal notice.")
    t1 = make_task("LC terms:\n{lc}\n\nPresentation:\n{pres}\n\nAutomated discrepancies:\n{disc}\n\n"
                   "Confirm each discrepancy, add any others, and classify as major/minor.", "Discrepancy list with UCP references.", checker)
    t2 = make_task("Recommend the handling and draft the refusal notice text listing all discrepancies.",
                   "Decision + draft MT734 narrative.", ops, context=[t1])
    section("Decision", run_crew([checker, ops], [t1, t2], {"lc": json.dumps(LC, indent=2),
                                                             "pres": json.dumps(PRESENTATION, indent=2), "disc": "\n".join(disc)}))


if __name__ == "__main__":
    main()
