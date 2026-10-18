"""Customer Segmentation & Campaign Planner — LangChain chain + Ollama.

Python segments loyalty customers by recency, frequency and spend (RFM) and sets each segment's discount
limit; the LLM writes a campaign plan for every segment within those limits.

Run:  python 02_retail/10_customer_segmentation/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, run_chain, section

# Loyalty members, last 12 months: (customer ID, days since last order, orders, spend). IDs only, no personal data.
CUSTOMERS = [
    ("CU-01", 5, 18, 2400), ("CU-02", 12, 14, 1900), ("CU-03", 25, 11, 1300), ("CU-04", 40, 7, 820),
    ("CU-05", 55, 6, 640), ("CU-06", 18, 8, 900), ("CU-07", 8, 1, 60), ("CU-08", 20, 2, 140),
    ("CU-09", 3, 1, 45), ("CU-10", 95, 9, 1100), ("CU-11", 120, 6, 700), ("CU-12", 150, 12, 1600),
    ("CU-13", 240, 3, 210), ("CU-14", 310, 1, 35), ("CU-15", 200, 4, 300), ("CU-16", 75, 3, 260),
]
# Marketing guardrails per segment: the most we will discount, and why
MAX_DISCOUNT = {"Champions": (0, "they buy anyway: reward with early access, not discounts"),
                "Loyal": (5, "nudge toward Champions with bonus points"),
                "New": (10, "win the second purchase"),
                "At risk": (15, "win back valuable customers before they lapse"),
                "Hibernating": (0, "low-cost email only; don't spend on customers unlikely to return")}


def segment(days: int, orders: int) -> str:
    if days <= 30 and orders >= 10:
        return "Champions"
    if days <= 60 and orders >= 5:
        return "Loyal"
    if days <= 30 and orders <= 2:
        return "New"
    if days <= 180 and orders >= 5:
        return "At risk"
    return "Hibernating"


def profile() -> list[dict]:
    total = sum(c[3] for c in CUSTOMERS)
    groups: dict[str, list] = {name: [] for name in MAX_DISCOUNT}
    for cid, days, orders, spend in CUSTOMERS:
        groups[segment(days, orders)].append((cid, days, orders, spend))
    rows = []
    for name, members in groups.items():
        n = len(members)
        rows.append({"segment": name, "customers": n, "share_of_revenue_pct": round(sum(m[3] for m in members) / total * 100),
                     "avg_spend": round(sum(m[3] for m in members) / n) if n else 0,
                     "avg_orders": round(sum(m[2] for m in members) / n, 1) if n else 0,
                     "avg_days_since_last_order": round(sum(m[1] for m in members) / n) if n else 0,
                     "max_discount_pct": MAX_DISCOUNT[name][0], "guardrail": MAX_DISCOUNT[name][1],
                     "customer_ids": [m[0] for m in members]})
    return rows


SYSTEM = (
    "You are a retail CRM marketing manager. For each customer segment write a campaign: goal, offer, channel "
    "(email, app push, SMS or direct mail) and a one-line message idea. Never exceed max_discount_pct and follow the "
    "guardrail. Quote the figures given; never recalculate. Start with the segment that matters most for revenue "
    "next quarter and say why. End with how to measure success (e.g. a control group). Under 300 words."
)


def main():
    banner("Retail 10 - Customer Segmentation & Campaign Planner (LangChain chain)")
    rows = profile()
    section("RFM segments", json.dumps(rows, indent=2))
    section("Campaign plan", run_chain(SYSTEM, "Segments:\n{s}", s=json.dumps(rows, indent=2)))


if __name__ == "__main__":
    main()
