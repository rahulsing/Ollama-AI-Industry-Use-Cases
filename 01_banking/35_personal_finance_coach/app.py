"""Personal Finance Coach — LangChain chain + Ollama.

Run:  python 01_banking/35_personal_finance_coach/app.py
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, run_chain, section

INCOME = 5200  # monthly take-home
TXNS = [("Rent", 1650), ("Tesco", 210), ("Uber Eats", 64), ("Deliveroo", 48), ("Netflix", 15), ("Spotify", 11),
        ("Disney+", 9), ("Gym", 55), ("Electric", 95), ("Amazon", 180), ("Zara", 140), ("Uber Eats", 52),
        ("Car loan", 320), ("Petrol", 140), ("Restaurants", 230), ("Sainsbury", 175), ("Phone", 35), ("ISA transfer", 200),
        ("Pub", 85), ("Amazon", 95), ("Deliveroo", 41), ("Council tax", 160), ("Water", 38)]

CATEGORY = {"Rent": "needs", "Electric": "needs", "Council tax": "needs", "Water": "needs", "Phone": "needs",
            "Tesco": "needs", "Sainsbury": "needs", "Car loan": "needs", "Petrol": "needs",
            "ISA transfer": "savings"}  # everything else = wants


def analyse() -> dict:
    by_bucket, by_merchant = defaultdict(float), defaultdict(float)
    for m, amt in TXNS:
        by_bucket[CATEGORY.get(m, "wants")] += amt
        by_merchant[m] += amt
    subs = {m: by_merchant[m] for m in ("Netflix", "Spotify", "Disney+", "Gym")}
    takeaway = by_merchant["Uber Eats"] + by_merchant["Deliveroo"]
    return {"income": INCOME, "spent": round(sum(a for _, a in TXNS)),
            "pct_of_income": {k: round(v / INCOME * 100) for k, v in by_bucket.items()},
            "target_50_30_20": {"needs": 50, "wants": 30, "savings": 20},
            "top_wants": sorted(((m, a) for m, a in by_merchant.items() if CATEGORY.get(m, "wants") == "wants"), key=lambda x: -x[1])[:5],
            "subscriptions_total": sum(subs.values()), "takeaway_total": takeaway}


SYSTEM = (
    "You are a warm, practical personal finance coach inside a banking app. Using the analysis, give: a 2-line summary "
    "vs the 50/30/20 rule, 4 specific saving tips with estimated monthly savings, a suggested monthly budget table, and one "
    "encouraging closing line. No product sales, no investment advice."
)


def main():
    banner("35 - Personal Finance Coach (LangChain)")
    a = analyse()
    section("Spending analysis", json.dumps(a, indent=2))
    section("Coaching", run_chain(SYSTEM, "Analysis:\n{a}", a=json.dumps(a, indent=2)))


if __name__ == "__main__":
    main()
