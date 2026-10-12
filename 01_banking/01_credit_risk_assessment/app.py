"""Credit Risk Assessment Agent — CrewAI + Ollama.

Python computes the hard numbers (DTI, LTI, score, policy breaches) so they are
auditable; two agents interpret them and issue a decision memo.

Run:  python 01_banking/01_credit_risk_assessment/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

APPLICANT = {
    "name": "Priya Sharma",
    "age": 34,
    "employment": "Salaried - IT services, 6 years",
    "annual_income": 1_800_000,
    "existing_monthly_emi": 18_000,
    "requested_loan": 1_200_000,
    "tenure_months": 60,
    "interest_rate_pct": 11.5,
    "credit_score": 742,
    "delinquencies_24m": 0,
    "credit_utilisation_pct": 38,
    "purpose": "Home renovation",
}

POLICY = {"max_dti_pct": 50, "max_lti": 5, "min_score": 680, "max_delinquencies": 1}


def emi(principal: float, annual_rate_pct: float, months: int) -> float:
    r = annual_rate_pct / 12 / 100
    return principal * r * (1 + r) ** months / ((1 + r) ** months - 1)


def assess(a: dict) -> dict:
    new_emi = emi(a["requested_loan"], a["interest_rate_pct"], a["tenure_months"])
    monthly_income = a["annual_income"] / 12
    dti = (a["existing_monthly_emi"] + new_emi) / monthly_income * 100
    lti = a["requested_loan"] / a["annual_income"]

    # Simple, transparent scorecard (0-100). Replace with your PD model.
    score = 50
    score += (a["credit_score"] - 650) / 5
    score -= max(0, dti - 35) * 0.8
    score -= a["delinquencies_24m"] * 10
    score -= max(0, a["credit_utilisation_pct"] - 30) * 0.3
    score = round(max(0, min(100, score)), 1)
    grade = "A" if score >= 75 else "B" if score >= 60 else "C" if score >= 45 else "D"

    breaches = []
    if dti > POLICY["max_dti_pct"]:
        breaches.append(f"DTI {dti:.1f}% > {POLICY['max_dti_pct']}%")
    if lti > POLICY["max_lti"]:
        breaches.append(f"LTI {lti:.2f}x > {POLICY['max_lti']}x")
    if a["credit_score"] < POLICY["min_score"]:
        breaches.append(f"Bureau score {a['credit_score']} < {POLICY['min_score']}")
    if a["delinquencies_24m"] > POLICY["max_delinquencies"]:
        breaches.append("Too many delinquencies in 24 months")

    def headroom(value: float, limit: float) -> str:
        used = value / limit
        return "BREACH" if used > 1 else "NEAR LIMIT" if used > 0.85 else "WITHIN LIMIT (comfortable)"

    return {
        "policy_assessment": {
            "dti": f"{dti:.1f}% vs max {POLICY['max_dti_pct']}% -> {headroom(dti, POLICY['max_dti_pct'])}",
            "lti": f"{lti:.2f}x vs max {POLICY['max_lti']}x -> {headroom(lti, POLICY['max_lti'])}",
            "credit_score": f"{a['credit_score']} vs min {POLICY['min_score']} -> "
                            f"{'PASS' if a['credit_score'] >= POLICY['min_score'] else 'FAIL'}",
        },
        "new_emi": round(new_emi),
        "dti_pct": round(dti, 1),
        "lti": round(lti, 2),
        "risk_score": score,
        "risk_grade": grade,
        "policy_breaches": breaches or ["None"],
    }


def main():
    banner("01 - Credit Risk Assessment Agent (CrewAI)")
    metrics = assess(APPLICANT)
    section("Computed metrics", json.dumps(metrics, indent=2))

    analyst = make_agent(
        "Retail Credit Analyst",
        "Analyse applicant data and computed risk metrics objectively",
        "10 years of retail lending experience; you explain risk drivers clearly and never invent data.",
    )
    cro = make_agent(
        "Chief Risk Officer",
        "Make a final, policy-compliant credit decision",
        "You chair the credit committee and balance growth with prudent risk management.",
    )

    analysis = make_task(
        "Applicant:\n{applicant}\n\nComputed metrics:\n{metrics}\n\nBank policy:\n{policy}\n\n"
        "Identify the key strengths, weaknesses and risk drivers of this application.",
        "Bullet list of strengths, weaknesses and key risk drivers referencing the numbers.",
        analyst,
    )
    decision = make_task(
        "Using the analyst's review, issue a credit decision memo.\n\n"
        "Exact computed metrics (quote these; never invent numbers):\n{metrics}\n\n"
        "Bank policy limits (compare each metric to its limit before judging it):\n{policy}",
        "Memo with: Decision (APPROVE / APPROVE WITH CONDITIONS / REFER / DECLINE), risk grade, "
        "3-line rationale, conditions or covenants, and recommended pricing adjustment.",
        cro,
        context=[analysis],
    )

    result = run_crew(
        [analyst, cro],
        [analysis, decision],
        {"applicant": json.dumps(APPLICANT, indent=2), "metrics": json.dumps(metrics, indent=2),
         "policy": json.dumps(POLICY, indent=2)},
    )
    section("Credit decision memo", result)


if __name__ == "__main__":
    main()
