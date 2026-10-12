"""Claims Triage & Fraud Detection — CrewAI + Ollama.

Python applies triage and fraud red-flag rules (auditable); agents assess and decide.

Run:  python 03_insurance/01_claims_triage_fraud/app.py
"""

import json
import sys
from datetime import date
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

CLAIMS = [
    {"id": "CLM-501", "type": "Home - escape of water", "policy_start": "2021-03-01", "loss_date": "2026-09-28",
     "reported": "2026-09-29", "amount": 1_850, "sum_insured": 250_000, "prior_claims_3y": 0,
     "description": "Washing machine hose burst, kitchen floor and cabinet plinths damaged. Plumber invoice attached."},
    {"id": "CLM-502", "type": "Home - theft", "policy_start": "2026-08-20", "loss_date": "2026-09-12",
     "reported": "2026-10-03", "amount": 14_200, "sum_insured": 15_000, "prior_claims_3y": 2,
     "description": "Burglary while on holiday. Laptop, two watches and jewellery taken. No receipts, no sign of forced entry."},
    {"id": "CLM-503", "type": "Motor - collision", "policy_start": "2024-06-10", "loss_date": "2026-10-01",
     "reported": "2026-10-01", "amount": 6_400, "sum_insured": 18_000, "prior_claims_3y": 1,
     "description": "Rear-ended at traffic lights. Third party admitted fault at scene; dashcam footage available."},
]


def triage(c: dict) -> dict:
    flags = []
    policy_age = (date.fromisoformat(c["loss_date"]) - date.fromisoformat(c["policy_start"])).days
    delay = (date.fromisoformat(c["reported"]) - date.fromisoformat(c["loss_date"])).days
    if policy_age < 60: flags.append(f"Loss {policy_age} days after policy start")
    if delay > 14: flags.append(f"Reported {delay} days after loss")
    if c["amount"] > 0.8 * c["sum_insured"]: flags.append("Claim close to sum insured")
    if c["prior_claims_3y"] >= 2: flags.append(f"{c['prior_claims_3y']} prior claims in 3 years")
    if "no receipts" in c["description"].lower(): flags.append("No proof of ownership")
    if "no sign of forced entry" in c["description"].lower(): flags.append("No forced entry on a burglary claim")
    fraud_score = min(len(flags) * 20, 100)
    if fraud_score >= 60:
        route = "SIU referral"
    elif c["amount"] < 2_500 and not flags:
        route = "Fast-track payment"
    else:
        route = "Adjuster review"
    recovery = "third party admitted fault" in c["description"].lower()
    handling = {"Fast-track payment": "PAY", "Adjuster review": "ADJUSTER REVIEW, THEN PAY IF VALID",
                "SIU referral": "REFER TO SIU"}[route]
    return {"id": c["id"], "fraud_score": fraud_score, "red_flags": flags or ["none"], "route": route,
            "final_handling": handling, "subrogation_opportunity": recovery}


def main():
    banner("Insurance 01 - Claims Triage & Fraud Detection (CrewAI)")
    results = [triage(c) for c in CLAIMS]
    section("Triage (rules)", json.dumps(results, indent=2))

    adjuster = make_agent("Claims Adjuster", "Assess each claim's validity, coverage questions and next steps",
                          "Experienced property and motor adjuster who treats honest customers fairly and quickly.")
    siu = make_agent("SIU Investigator", "Decide the handling of each claim, especially suspected fraud",
                     "Special Investigations Unit lead; you never accuse customers, you gather evidence proportionately.")
    t1 = make_task("Claims:\n{claims}\n\nRule-based triage (final, do not change the scores or routes):\n{triage}\n\n"
                   "For each claim: summarise it, note coverage questions and the evidence needed.",
                   "Per-claim assessment.", adjuster)
    t2 = make_task("Triage (exact; final_handling is already decided by the rules and must be copied unchanged):\n"
                   "{triage}\n\nFor each claim state its final_handling, then the evidence to request, a polite customer "
                   "message (never mention fraud or suspicion), and a recovery action against the third party only "
                   "where subrogation_opportunity is true. Claims with no red flags must not be treated as suspicious.",
                   "Per claim: final_handling (copied), evidence list, customer message, recovery action.", siu, context=[t1])
    section("Claims decisions", run_crew([adjuster, siu], [t1, t2], {"claims": json.dumps(CLAIMS, indent=2),
                                                                     "triage": json.dumps(results, indent=2)}))


if __name__ == "__main__":
    main()
