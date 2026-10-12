"""Credit Card Limit Optimizer — LangChain chain + Ollama.

Rules decide the action and the new limit; the LLM explains it.

Run:  python 01_banking/04_credit_limit_optimizer/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, run_chain, section

CARDHOLDERS = [
    {"id": "C-201", "limit": 5000, "avg_balance_6m": 4300, "on_time_payments_12m": 12, "income": 85000, "bureau_score": 760, "months_on_book": 30},
    {"id": "C-202", "limit": 8000, "avg_balance_6m": 900, "on_time_payments_12m": 12, "income": 60000, "bureau_score": 710, "months_on_book": 48},
    {"id": "C-203", "limit": 6000, "avg_balance_6m": 5900, "on_time_payments_12m": 8, "income": 40000, "bureau_score": 640, "months_on_book": 14},
]


def recommend(c: dict) -> dict:
    util = c["avg_balance_6m"] / c["limit"]
    max_limit = c["income"] * 0.25  # exposure cap: 25% of annual income
    if c["on_time_payments_12m"] < 10 or c["bureau_score"] < 660:
        # never cut below the current balance; if that means no cut, freeze further increases
        new = min(c["limit"], max(c["avg_balance_6m"], c["limit"] * 0.8))
        action = "DECREASE" if new < c["limit"] else "FREEZE"
    elif util > 0.7 and c["months_on_book"] >= 12:
        action, new = "INCREASE", min(c["limit"] * 1.5, max_limit)
    elif util < 0.2:
        action, new = "HOLD", c["limit"]
    else:
        action, new = "INCREASE", min(c["limit"] * 1.2, max_limit)
    return {**c, "utilisation_pct": round(util * 100), "action": action, "new_limit": round(new, -2)}


SYSTEM = (
    "You are a card portfolio manager. For each card holder, explain the limit decision in 2 sentences "
    "for the internal file, then write one friendly, compliant sentence for the customer notification. "
    "Do not change the decided numbers."
)


def main():
    banner("04 - Credit Card Limit Optimizer (LangChain)")
    decisions = [recommend(c) for c in CARDHOLDERS]
    section("Rule-based decisions", json.dumps(decisions, indent=2))
    section("Explanations", run_chain(SYSTEM, "Decisions:\n{decisions}", decisions=json.dumps(decisions, indent=2)))


if __name__ == "__main__":
    main()
