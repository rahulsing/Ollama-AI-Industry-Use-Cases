"""AI Wealth Advisor — CrewAI + Ollama.

Three agents: Client Profiler -> Portfolio Strategist -> Compliance Reviewer.

Run:  python 01_banking/26_wealth_advisor_agent/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

CLIENT = {
    "name": "Arjun & Meera Nair", "ages": [38, 36], "dependants": "2 children (6 and 9)",
    "annual_household_income": 6_000_000, "monthly_expenses": 150_000,
    "assets": {"savings_account": 900_000, "fixed_deposits": 1_500_000, "equity_stocks": 1_200_000,
               "employer_provident_fund": 2_100_000, "gold": 600_000},
    "liabilities": {"home_loan_outstanding": 4_800_000, "home_loan_emi": 52_000},
    "insurance": {"term_life_cover": 10_000_000, "health_cover": 1_000_000},
    "goals": [{"goal": "Children's higher education", "years": 10, "today_cost": 4_000_000},
              {"goal": "Retirement corpus", "years": 22, "today_cost": 30_000_000},
              {"goal": "Family vacation home", "years": 10, "today_cost": 5_000_000}],
    "risk_questionnaire_score": 62, "investment_experience": "5 years in direct equity and mutual funds",
    "preferences": "No tobacco/alcohol companies; prefers low-cost index funds",
}

MODEL_PORTFOLIOS = {
    "Conservative (score <40)": {"equity": 25, "debt": 60, "gold": 10, "cash": 5},
    "Moderate (40-65)": {"equity": 50, "debt": 35, "gold": 10, "cash": 5},
    "Growth (65-80)": {"equity": 70, "debt": 20, "gold": 5, "cash": 5},
    "Aggressive (>80)": {"equity": 85, "debt": 10, "gold": 5, "cash": 0},
}


def future_value(cost: float, years: int, inflation: float = 0.06) -> float:
    return cost * (1 + inflation) ** years


def monthly_sip(target: float, years: int, annual_return: float) -> float:
    """Monthly investment needed to reach `target` in `years` at `annual_return`."""
    r, n = annual_return / 12, years * 12
    return target * r / ((1 + r) ** n - 1)


def main():
    banner("26 - AI Wealth Advisor (CrewAI)")
    goals = []
    for g in CLIENT["goals"]:
        target = future_value(g["today_cost"], g["years"])
        expected_return = 0.10 if g["years"] > 7 else 0.08  # equity-heavy for long horizons
        goals.append({**g, "inflated_cost": round(target), "assumed_return_pct": expected_return * 100,
                      "required_monthly_sip": round(monthly_sip(target, g["years"], expected_return))})
    surplus = CLIENT["annual_household_income"] / 12 * 0.7 - CLIENT["monthly_expenses"] - CLIENT["liabilities"]["home_loan_emi"]
    required = sum(g["required_monthly_sip"] for g in goals)
    net_worth = sum(CLIENT["assets"].values()) - CLIENT["liabilities"]["home_loan_outstanding"]
    facts = {"goals": goals, "net_worth": net_worth, "est_monthly_investable_surplus_post_tax": round(surplus),
             "total_required_monthly_sip": required, "monthly_shortfall": round(max(required - surplus, 0)),
             "existing_investable_assets": sum(v for k, v in CLIENT["assets"].items() if k != "savings_account"),
             "emergency_fund_months": round(CLIENT["assets"]["savings_account"] / CLIENT["monthly_expenses"], 1)}
    section("Computed facts", json.dumps(facts, indent=2))

    profiler = make_agent("Client Profiler", "Build a precise financial and risk profile of the client",
                          "Certified financial planner who reads between the lines of client data.")
    strategist = make_agent("Portfolio Strategist", "Design a goals-based asset allocation and SIP plan",
                            "Investment strategist who favours diversified, low-cost, tax-efficient portfolios.")
    compliance = make_agent("Compliance Reviewer", "Ensure advice is suitable, balanced and properly disclosed",
                            "You check suitability, concentration, risk disclosures and that no returns are guaranteed.")
    t1 = make_task("Client:\n{client}\n\nComputed facts:\n{facts}\n\nProfile the client: net worth, cash flow, "
                   "protection adequacy, risk capacity vs. tolerance.", "Client profile summary.", profiler)
    t2 = make_task("Model portfolios:\n{models}\n\nComputed facts (use these figures; never do your own arithmetic):\n{facts}\n\n"
                   "The goals need more than the client can save (see monthly_shortfall). Prioritise the goals, decide how "
                   "to use existing assets and the monthly surplus, suggest which goals to resize or delay, and recommend "
                   "an allocation per goal. Also immediate actions (emergency fund, insurance, debt).",
                   "Prioritised goal-wise plan with allocations, using only the computed figures.", strategist, context=[t1])
    t3 = make_task("Review the plan for suitability and produce the final client-ready advice letter with risk disclosures.\n\n"
                   "Exact computed facts (quote these; never invent numbers):\n{facts}",
                   "Final advice letter: summary, plan per goal, actions, risks & disclaimers.", compliance, context=[t1, t2])
    section("Advice", run_crew([profiler, strategist, compliance], [t1, t2, t3], {
        "client": json.dumps(CLIENT, indent=2), "facts": json.dumps(facts, indent=2), "models": json.dumps(MODEL_PORTFOLIOS, indent=2)}))


if __name__ == "__main__":
    main()
