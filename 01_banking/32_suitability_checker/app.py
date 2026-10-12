"""Suitability & Mis-selling Checker — rules + LangChain structured output.

Run:  python 01_banking/32_suitability_checker/app.py
"""

import json
import sys
from pathlib import Path
from typing import Literal

sys.path.append(str(Path(__file__).resolve().parents[2]))
from pydantic import BaseModel

from common import banner, run_structured, section

CLIENT = {"name": "Mrs. Lata Desai", "age": 71, "risk_profile": "Conservative (2/5)", "horizon_years": 2,
          "liquid_net_worth": 3_000_000, "income_need": "Regular monthly income", "experience": "Fixed deposits only"}

PROPOSALS = [
    {"product": "Structured note linked to small-cap index, capital at risk, 5-year lock-in", "risk_rating": 5, "lock_in_years": 5, "amount": 1_800_000},
    {"product": "Senior citizen savings scheme (government-backed)", "risk_rating": 1, "lock_in_years": 5, "amount": 1_000_000},
    {"product": "Short-duration high-quality debt fund", "risk_rating": 2, "lock_in_years": 0, "amount": 800_000},
]


def rules(p: dict) -> list[str]:
    client_risk = 2
    issues = []
    if p["risk_rating"] > client_risk: issues.append(f"Product risk {p['risk_rating']} > client risk {client_risk}")
    if p["lock_in_years"] > CLIENT["horizon_years"]: issues.append(f"Lock-in {p['lock_in_years']}y exceeds horizon {CLIENT['horizon_years']}y")
    if p["amount"] / CLIENT["liquid_net_worth"] > 0.5: issues.append("Concentration >50% of liquid net worth")
    if "structured" in p["product"].lower() and "Fixed deposits only" in CLIENT["experience"]:
        issues.append("Complex product for inexperienced client")
    return issues


class Verdict(BaseModel):
    verdict: Literal["SUITABLE", "SUITABLE_WITH_CONDITIONS", "NOT_SUITABLE"]
    vulnerable_customer: bool
    reasons: list[str]
    required_actions: list[str]


def main():
    banner("32 - Suitability & Mis-selling Checker (LangChain structured output)")
    system = ("You are a suitability reviewer at a bank. Consider the rule findings, client vulnerability (age, experience), "
              "liquidity needs and complexity. Rule breaches on risk or horizon should normally mean NOT_SUITABLE.")
    for p in PROPOSALS:
        findings = rules(p)
        v = run_structured(system, json.dumps({"client": CLIENT, "proposal": p, "rule_findings": findings}), Verdict)
        section(p["product"], f"Rule findings: {findings or 'none'}\n{v.model_dump_json(indent=2)}")


if __name__ == "__main__":
    main()
