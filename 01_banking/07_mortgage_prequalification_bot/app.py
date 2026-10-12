"""Mortgage Pre-Qualification Bot — LangChain tool-calling agent + Ollama.

Run:  python 01_banking/07_mortgage_prequalification_bot/app.py
      python 01_banking/07_mortgage_prequalification_bot/app.py "I earn 7000/month, pay 500 car loan. How much can I borrow?"
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from langchain_core.tools import tool

from common import banner, run_agent, section

MAX_DTI = 0.40
DEFAULT_RATE = 6.5
DEFAULT_YEARS = 30


@tool
def monthly_emi(loan_amount: float, annual_rate_pct: float = DEFAULT_RATE, years: int = DEFAULT_YEARS) -> str:
    """Monthly repayment for a loan amount, annual interest rate (%) and term in years."""
    r, n = annual_rate_pct / 1200, years * 12
    pay = loan_amount * r * (1 + r) ** n / ((1 + r) ** n - 1)
    return f"Monthly payment: {pay:,.0f} for {loan_amount:,.0f} at {annual_rate_pct}% over {years} years"


@tool
def max_affordable_loan(monthly_income: float, monthly_debts: float = 0,
                        annual_rate_pct: float = DEFAULT_RATE, years: int = DEFAULT_YEARS) -> str:
    """Maximum loan a customer can afford, keeping total debt payments within the bank's 40% DTI limit."""
    budget = monthly_income * MAX_DTI - monthly_debts
    if budget <= 0:
        return "Existing debts already exceed the 40% DTI limit; no additional borrowing capacity."
    r, n = annual_rate_pct / 1200, years * 12
    loan = budget * ((1 + r) ** n - 1) / (r * (1 + r) ** n)
    return f"Max loan ~{loan:,.0f} (monthly payment budget {budget:,.0f}, {annual_rate_pct}% over {years}y)"


SYSTEM = (
    "You are a friendly mortgage pre-qualification assistant. Use the tools for every calculation. "
    "State assumptions (rate, term, 40% DTI) clearly, mention this is an indicative estimate and not a "
    "loan offer, and suggest a sensible down payment (20%) to estimate an affordable property price."
)


def main():
    banner("07 - Mortgage Pre-Qualification Bot (LangChain agent)")
    q = sys.argv[1] if len(sys.argv) > 1 else (
        "I earn 8,500 a month and pay 650 a month on a car loan. How much can I borrow, and what would "
        "the monthly payment be on a 25 year term at 6.2%?")
    section("Customer", q)
    section("Assistant", run_agent(SYSTEM, [max_affordable_loan, monthly_emi], q))


if __name__ == "__main__":
    main()
