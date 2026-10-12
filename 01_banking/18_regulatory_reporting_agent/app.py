"""Regulatory Reporting Agent — CrewAI + Ollama.

Validates a (simplified) capital & liquidity return, explains quarter-on-quarter
movements and drafts the submission commentary.

Run:  python 01_banking/18_regulatory_reporting_agent/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

# Figures in millions
RETURN = {
    "Q2-2026": {"cet1_capital": 4_850, "at1_capital": 600, "tier2_capital": 900, "rwa_credit": 31_200, "rwa_market": 2_100,
                "rwa_operational": 3_900, "hqla": 9_800, "net_outflows_30d": 7_000, "total_loans": 52_000, "npl": 1_560},
    "Q3-2026": {"cet1_capital": 4_910, "at1_capital": 600, "tier2_capital": 880, "rwa_credit": 34_900, "rwa_market": 2_600,
                "rwa_operational": 3_900, "hqla": 9_100, "net_outflows_30d": 7_600, "total_loans": 57_300, "npl": 1_830},
}
MINIMUMS = {"cet1_ratio": 7.0, "tier1_ratio": 8.5, "total_capital_ratio": 10.5, "lcr": 100}
ADJ = {"Q3-2026": ["Large corporate loan growth in construction sector", "New FX trading desk launched in August"]}


def metrics(d: dict) -> dict:
    rwa = d["rwa_credit"] + d["rwa_market"] + d["rwa_operational"]
    t1 = d["cet1_capital"] + d["at1_capital"]
    return {"total_rwa": rwa, "cet1_ratio": round(d["cet1_capital"] / rwa * 100, 2),
            "tier1_ratio": round(t1 / rwa * 100, 2), "total_capital_ratio": round((t1 + d["tier2_capital"]) / rwa * 100, 2),
            "lcr": round(d["hqla"] / d["net_outflows_30d"] * 100, 1), "npl_ratio": round(d["npl"] / d["total_loans"] * 100, 2)}


def validate(d: dict, m: dict) -> list[str]:
    issues = [f"{k} {m[k]} below minimum {v}" for k, v in MINIMUMS.items() if m[k] < v]
    if any(v < 0 for v in d.values()):
        issues.append("Negative values present")
    if d["npl"] > d["total_loans"]:
        issues.append("NPL exceeds total loans")
    return issues or ["All validation checks passed"]


def main():
    banner("18 - Regulatory Reporting Agent (CrewAI)")
    m = {q: metrics(d) for q, d in RETURN.items()}
    q0, q1 = list(RETURN)
    variance = {k: round(m[q1][k] - m[q0][k], 2) for k in m[q1]}
    checks = validate(RETURN[q1], m[q1])
    section("Metrics", json.dumps(m, indent=2))
    section("QoQ variance", json.dumps(variance, indent=2))
    section("Validation", "\n".join(checks))

    dq = make_agent("Regulatory Data Quality Analyst", "Confirm the return is complete, consistent and within thresholds",
                    "You run pre-submission controls on prudential returns and flag anything a regulator would query.")
    reporter = make_agent("Regulatory Reporting Manager", "Write the submission commentary for the regulator and CFO sign-off",
                          "Experienced in Basel III / COREP-style reporting; precise, neutral tone.")
    t1 = make_task("Return data:\n{data}\n\nMetrics:\n{metrics}\n\nVariance:\n{variance}\n\nValidation:\n{checks}\n\n"
                   "Business events this quarter:\n{events}\n\nReview data quality and identify movements needing explanation (>5% or ratio change >0.25pp).",
                   "List of material movements and data-quality observations.", dq)
    t2 = make_task("Draft the regulatory submission commentary.\n\nExact metrics by quarter (quote these; never invent "
                   "or recalculate numbers):\n{metrics}\n\nQoQ variance:\n{variance}\n\nMinimums: CET1 7.0%, Tier 1 8.5%, "
                   "Total capital 10.5%, LCR 100%.",
                   "Commentary: 1. Executive summary 2. Capital adequacy (ratios vs minimums & drivers) "
                   "3. Liquidity (LCR) 4. Asset quality 5. Data quality statement 6. Items for CFO attention.",
                   reporter, context=[t1])
    section("Submission commentary", run_crew([dq, reporter], [t1, t2], {
        "data": json.dumps(RETURN, indent=2), "metrics": json.dumps(m, indent=2), "variance": json.dumps(variance, indent=2),
        "checks": "\n".join(checks), "events": json.dumps(ADJ, indent=2)}))


if __name__ == "__main__":
    main()
