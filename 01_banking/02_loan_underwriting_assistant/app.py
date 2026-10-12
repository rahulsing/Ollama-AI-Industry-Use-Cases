"""Loan Underwriting Assistant — LangChain tool-calling agent + Ollama.

Run:  python 01_banking/02_loan_underwriting_assistant/app.py
      python 01_banking/02_loan_underwriting_assistant/app.py "Can APP-1002 be approved?"
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from langchain_core.tools import tool

from common import banner, run_agent, section

APPLICATIONS = {
    "APP-1001": {"monthly_income": 9500, "monthly_debt": 1800, "loan_amount": 320000,
                 "property_value": 400000, "credit_score": 728, "employment_years": 5, "loan_type": "mortgage"},
    "APP-1002": {"monthly_income": 6000, "monthly_debt": 2600, "loan_amount": 285000,
                 "property_value": 300000, "credit_score": 655, "employment_years": 1, "loan_type": "mortgage"},
}

POLICY = {"max_dti": 0.43, "max_ltv": 0.80, "min_score": 680, "min_employment_years": 2}


@tool
def get_application(app_id: str) -> dict:
    """Fetch a loan application by id, e.g. APP-1001."""
    return APPLICATIONS.get(app_id.upper(), {"error": f"{app_id} not found"})


@tool
def calculate_dti(monthly_debt: float, monthly_income: float, new_monthly_payment: float = 0) -> str:
    """Debt-to-income ratio including an optional new monthly payment."""
    dti = (monthly_debt + new_monthly_payment) / monthly_income
    return f"DTI = {dti:.1%} (policy max {POLICY['max_dti']:.0%})"


@tool
def calculate_ltv(loan_amount: float, property_value: float) -> str:
    """Loan-to-value ratio for secured lending."""
    ltv = loan_amount / property_value
    return f"LTV = {ltv:.1%} (policy max {POLICY['max_ltv']:.0%}; above this requires mortgage insurance)"


@tool
def check_policy(app_id: str) -> dict:
    """Run all underwriting policy rules for an application; returns value, threshold and pass/fail per rule."""
    a = APPLICATIONS.get(app_id.upper())
    if not a:
        return {"error": "not found"}
    dti = a["monthly_debt"] / a["monthly_income"]
    ltv = a["loan_amount"] / a["property_value"]
    return {
        "dti": {"value": round(dti, 3), "max": POLICY["max_dti"], "pass": dti <= POLICY["max_dti"]},
        "ltv": {"value": round(ltv, 3), "max": POLICY["max_ltv"], "pass": ltv <= POLICY["max_ltv"]},
        "credit_score": {"value": a["credit_score"], "min": POLICY["min_score"],
                         "pass": a["credit_score"] >= POLICY["min_score"]},
        "employment_years": {"value": a["employment_years"], "min": POLICY["min_employment_years"],
                             "pass": a["employment_years"] >= POLICY["min_employment_years"]},
    }


SYSTEM = (
    "You are a mortgage underwriting assistant at a bank. Always use the tools to fetch data and "
    "compute ratios - never guess numbers. Give: a summary table of ratios, which policy rules pass "
    "or fail, a recommendation (Approve / Approve with conditions / Decline) and any conditions."
)


def main():
    banner("02 - Loan Underwriting Assistant (LangChain agent)")
    question = sys.argv[1] if len(sys.argv) > 1 else "Underwrite APP-1001 and APP-1002 and compare them."
    section("Question", question)
    section("Answer", run_agent(SYSTEM, [get_application, calculate_dti, calculate_ltv, check_policy], question))


if __name__ == "__main__":
    main()
