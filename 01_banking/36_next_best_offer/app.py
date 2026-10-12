"""Next Best Offer / Cross-sell — CrewAI + Ollama.

Run:  python 01_banking/36_next_best_offer/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

CUSTOMERS = [
    {"id": "R-1", "age": 27, "products": ["savings"], "salary_credit": True, "avg_balance": 6200, "card_spend_m": 0,
     "events": ["Salary increased 20%"], "travel_spend_pct": 0},
    {"id": "R-2", "age": 35, "products": ["savings", "credit_card"], "salary_credit": True, "avg_balance": 28000, "card_spend_m": 1800,
     "events": ["Searched 'home loan' in app twice"], "travel_spend_pct": 8},
    {"id": "R-3", "age": 52, "products": ["savings", "fixed_deposit"], "salary_credit": False, "avg_balance": 95000, "card_spend_m": 0,
     "events": ["FD of 60,000 maturing in 10 days"], "travel_spend_pct": 0},
]

PRODUCTS = ["credit_card", "travel_card", "home_loan", "mutual_fund_sip", "term_insurance", "personal_loan"]


def propensity(c: dict) -> dict:
    s = {p: 0.1 for p in PRODUCTS if p not in c["products"]}
    if "credit_card" in s and c["salary_credit"] and c["age"] < 40: s["credit_card"] += 0.5
    if "home_loan" in s and any("home loan" in e for e in c["events"]): s["home_loan"] += 0.7
    if "mutual_fund_sip" in s and (c["avg_balance"] > 20000 or any("FD" in e for e in c["events"])): s["mutual_fund_sip"] += 0.5
    if "travel_card" in s and c["travel_spend_pct"] > 5: s["travel_card"] += 0.4
    if "term_insurance" in s and 25 <= c["age"] <= 50: s["term_insurance"] += 0.3
    if any("Salary increased" in e for e in c["events"]): s["mutual_fund_sip"] = s.get("mutual_fund_sip", 0.1) + 0.3
    return dict(sorted(((k, round(v, 2)) for k, v in s.items()), key=lambda x: -x[1])[:3])


def main():
    banner("36 - Next Best Offer (CrewAI)")
    scores = {c["id"]: propensity(c) for c in CUSTOMERS}
    section("Propensity (top 3)", json.dumps(scores, indent=2))
    marketer = make_agent("Marketing Analyst", "Pick the single best offer per customer and the best channel and timing",
                          "CRM analytics lead; you prioritise customer need over product push.")
    writer = make_agent("Compliance-aware Copywriter", "Write short personalised, fair and non-pushy offer messages",
                        "You write bank marketing copy that is clear, not misleading and includes key terms.")
    t1 = make_task("Customers:\n{customers}\n\nPropensity scores:\n{scores}\n\nChoose next best offer, channel (app push, email, RM call) and timing.",
                   "Per customer: offer, why, channel, timing.", marketer)
    t2 = make_task("Write the message for each customer (max 40 words, include an opt-out note).",
                   "Per customer message ready to send.", writer, context=[t1])
    section("Campaign", run_crew([marketer, writer], [t1, t2], {"customers": json.dumps(CUSTOMERS, indent=2),
                                                                 "scores": json.dumps(scores, indent=2)}))


if __name__ == "__main__":
    main()
