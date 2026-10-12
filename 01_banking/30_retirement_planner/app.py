"""Retirement Planning Assistant — LangChain tool-calling agent + Ollama.

Run:  python 01_banking/30_retirement_planner/app.py
      python 01_banking/30_retirement_planner/app.py "I'm 45, have 300k saved, save 1500/month, spend 4000/month. Retire at 60?"
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from langchain_core.tools import tool

from common import banner, run_agent, section


@tool
def retirement_plan(current_age: int, retire_age: int, current_savings: float, monthly_saving: float,
                    monthly_expense_today: float, annual_return_pct: float = 7.0, inflation_pct: float = 3.0,
                    post_retirement_return_pct: float = 5.0, years_in_retirement: int = 25) -> dict:
    """Full retirement calculation: required corpus, projected corpus, gap and the monthly saving needed.
    Call again with different inputs for what-if questions (e.g. a later retire_age)."""
    years = retire_age - current_age
    r, n = annual_return_pct / 1200, years * 12
    growth = (1 + r) ** n
    projected = current_savings * growth + monthly_saving * (growth - 1) / r

    first_year_expense = monthly_expense_today * 12 * (1 + inflation_pct / 100) ** years
    real = (1 + post_retirement_return_pct / 100) / (1 + inflation_pct / 100) - 1
    required = first_year_expense * (1 - (1 + real) ** -years_in_retirement) / real * (1 + real)

    required_total_saving = max(required - current_savings * growth, 0) * r / (growth - 1)
    return {
        "years_to_retirement": years,
        "required_corpus": round(required),
        "projected_corpus": round(projected),
        "gap": round(max(required - projected, 0)),
        "on_track": projected >= required,
        "required_total_monthly_saving": round(required_total_saving),
        "extra_monthly_saving_needed": round(max(required_total_saving - monthly_saving, 0)),
        "assumptions": f"{annual_return_pct}% return before retirement, {post_retirement_return_pct}% after, "
                       f"{inflation_pct}% inflation, {years_in_retirement} years in retirement",
    }


SYSTEM = (
    "You are a retirement planning assistant. Call retirement_plan for every calculation and copy its numbers exactly - "
    "never do arithmetic yourself. First answer the user's exact scenario (their stated retirement age): required "
    "corpus, projected corpus, gap, extra monthly saving needed. Then give 3 "
    "practical levers (retire later, save more, adjust allocation); you may call retirement_plan again to quantify a "
    "lever such as a later retirement age. Note assumptions and that this is not personal advice."
)


def main():
    banner("30 - Retirement Planning Assistant (LangChain agent)")
    q = sys.argv[1] if len(sys.argv) > 1 else (
        "I'm 40, have 150,000 saved, save 1,000 a month and spend 3,500 a month. Can I retire at 60?")
    section("Question", q)
    section("Plan", run_agent(SYSTEM, [retirement_plan], q))


if __name__ == "__main__":
    main()
