"""IFRS 9 ECL Calculator & Explainer — LangChain tool-calling agent + Ollama.

Run:  python 01_banking/23_ifrs9_ecl_calculator/app.py
      python 01_banking/23_ifrs9_ecl_calculator/app.py "Why is LN-3 in stage 2?"
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from langchain_core.tools import tool

from common import banner, run_agent, section

LOANS = {
    "LN-1": {"ead": 500_000, "dpd": 0, "pd_12m": 0.010, "pd_lifetime": 0.040, "pd_12m_at_origination": 0.009, "lgd": 0.35, "watchlist": False, "forborne": False},
    "LN-2": {"ead": 250_000, "dpd": 45, "pd_12m": 0.060, "pd_lifetime": 0.180, "pd_12m_at_origination": 0.020, "lgd": 0.40, "watchlist": False, "forborne": False},
    "LN-3": {"ead": 800_000, "dpd": 10, "pd_12m": 0.035, "pd_lifetime": 0.120, "pd_12m_at_origination": 0.012, "lgd": 0.45, "watchlist": True, "forborne": False},
    "LN-4": {"ead": 120_000, "dpd": 120, "pd_12m": 1.000, "pd_lifetime": 1.000, "pd_12m_at_origination": 0.030, "lgd": 0.60, "watchlist": False, "forborne": True},
}


@tool
def list_loans() -> list:
    """List all loan ids in the portfolio."""
    return list(LOANS)


@tool
def stage_loan(loan_id: str) -> dict:
    """Determine the IFRS 9 stage of a loan and the triggers that caused it."""
    l = LOANS[loan_id]
    triggers = []
    if l["dpd"] > 90 or l["pd_12m"] >= 1:
        return {"loan": loan_id, "stage": 3, "triggers": ["Credit-impaired: >90 DPD / default"]}
    if l["dpd"] > 30: triggers.append(">30 DPD backstop")
    if l["pd_12m"] / l["pd_12m_at_origination"] >= 2.5: triggers.append("PD increased >=2.5x since origination (SICR)")
    if l["watchlist"]: triggers.append("On credit watchlist")
    if l["forborne"]: triggers.append("Forbearance granted")
    return {"loan": loan_id, "stage": 2 if triggers else 1, "triggers": triggers or ["No SICR"]}


@tool
def calculate_ecl(loan_id: str, stage: int) -> dict:
    """Calculate ECL = PD x LGD x EAD (12-month PD for stage 1, lifetime PD for stages 2 and 3)."""
    l = LOANS[loan_id]
    pd = l["pd_12m"] if stage == 1 else l["pd_lifetime"]
    ecl = pd * l["lgd"] * l["ead"]
    return {"loan": loan_id, "stage": stage, "pd_used": pd, "lgd": l["lgd"], "ead": l["ead"],
            "ecl": round(ecl), "coverage": f"{ecl / l['ead'] * 100:.2f}%"}


@tool
def portfolio_ecl() -> dict:
    """Stage every loan and calculate ECL for the whole portfolio, including totals. Use for portfolio questions."""
    rows = []
    for loan_id in LOANS:
        s = stage_loan.invoke({"loan_id": loan_id})
        e = calculate_ecl.invoke({"loan_id": loan_id, "stage": s["stage"]})
        rows.append({**e, "triggers": s["triggers"]})
    total_ead = sum(r["ead"] for r in rows)
    total_ecl = sum(r["ecl"] for r in rows)
    return {"loans": rows, "total_ecl": total_ecl, "total_ead": total_ead,
            "portfolio_coverage": f"{total_ecl / total_ead * 100:.2f}%"}


SYSTEM = (
    "You are an IFRS 9 impairment analyst. For whole-portfolio questions call portfolio_ecl; for a single loan use "
    "stage_loan and calculate_ecl. Copy numbers exactly from tool results - never add or recompute them yourself. "
    "Present a table: loan, stage, triggers, ECL, coverage %. State the total ECL from the tool, then explain "
    "12-month vs lifetime ECL (both are forward-looking) and the main drivers in plain language."
)


def main():
    banner("23 - IFRS 9 ECL Calculator & Explainer (LangChain agent)")
    q = sys.argv[1] if len(sys.argv) > 1 else "Calculate the ECL for the whole portfolio and explain it."
    section("Question", q)
    section("Answer", run_agent(SYSTEM, [portfolio_ecl, list_loans, stage_loan, calculate_ecl], q))


if __name__ == "__main__":
    main()
