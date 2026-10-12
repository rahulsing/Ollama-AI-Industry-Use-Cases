"""Customer Risk Rating (CRR) — weighted factor model + LangChain justification.

Run:  python 01_banking/16_customer_risk_rating/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, run_chain, section

FACTORS = {  # factor -> (weight, {value: score 1-3})
    "occupation": (0.25, {"salaried": 1, "self_employed": 2, "jeweller": 3, "real_estate": 3, "money_service_business": 3}),
    "geography": (0.25, {"domestic": 1, "fatf_compliant": 1, "medium_risk": 2, "high_risk": 3}),
    "product": (0.20, {"savings": 1, "credit_card": 1, "current_account": 2, "trade_finance": 3, "private_banking": 3}),
    "channel": (0.10, {"branch": 1, "digital_verified": 2, "non_face_to_face": 3}),
    "pep": (0.20, {"no": 1, "domestic_pep": 3, "foreign_pep": 3, "pep_associate": 2}),
}

CUSTOMERS = [
    {"id": "K-01", "occupation": "salaried", "geography": "domestic", "product": "savings", "channel": "branch", "pep": "no"},
    {"id": "K-02", "occupation": "jeweller", "geography": "medium_risk", "product": "current_account", "channel": "digital_verified", "pep": "no"},
    {"id": "K-03", "occupation": "real_estate", "geography": "high_risk", "product": "private_banking", "channel": "non_face_to_face", "pep": "foreign_pep"},
]


def rate(c: dict) -> dict:
    breakdown = {f: FACTORS[f][1][c[f]] for f in FACTORS}
    score = sum(FACTORS[f][0] * s for f, s in breakdown.items())
    rating = "HIGH" if score >= 2.2 or c["pep"] != "no" else "MEDIUM" if score >= 1.6 else "LOW"
    review = {"HIGH": "12 months", "MEDIUM": "24 months", "LOW": "36 months"}[rating]
    return {"id": c["id"], "factor_scores": breakdown, "weighted_score": round(score, 2), "rating": rating, "next_review": review}


SYSTEM = (
    "You are a KYC/AML analyst. For each customer write a 3-4 sentence risk-rating justification for the KYC file, "
    "naming the main drivers, and list due-diligence measures (SDD / CDD / EDD, source of wealth, senior approval for PEPs)."
)


def main():
    banner("16 - Customer Risk Rating (LangChain)")
    ratings = [rate(c) for c in CUSTOMERS]
    section("Ratings", json.dumps(ratings, indent=2))
    section("Justifications", run_chain(SYSTEM, "Customers:\n{c}\n\nRatings:\n{r}",
                                        c=json.dumps(CUSTOMERS, indent=2), r=json.dumps(ratings, indent=2)))


if __name__ == "__main__":
    main()
