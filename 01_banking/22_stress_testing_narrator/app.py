"""Stress Testing Scenario Narrator — CrewAI + Ollama.

Run:  python 01_banking/22_stress_testing_narrator/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

PORTFOLIO = {  # EAD (millions), baseline PD, LGD
    "Residential mortgages": (12_000, 0.008, 0.20),
    "Commercial real estate": (3_000, 0.020, 0.40),
    "SME loans": (6_000, 0.030, 0.45),
    "Large corporate": (14_000, 0.012, 0.40),
    "Credit cards": (2_500, 0.045, 0.80),
}
CET1, RWA, PPNR = 3_900, 40_000, 650  # capital, RWA, pre-provision net revenue

SCENARIOS = {
    "Baseline": {"gdp": 2.5, "unemployment": 4.5, "house_prices": 3, "pd_mult": 1.0, "lgd_add": 0.00, "ppnr_mult": 1.0},
    "Adverse": {"gdp": -1.5, "unemployment": 7.5, "house_prices": -12, "pd_mult": 2.0, "lgd_add": 0.05, "ppnr_mult": 0.8},
    "Severely adverse": {"gdp": -4.0, "unemployment": 10.0, "house_prices": -25, "pd_mult": 3.5, "lgd_add": 0.10, "ppnr_mult": 0.6},
}


def run_scenario(s: dict) -> dict:
    losses = {k: ead * min(pd * s["pd_mult"], 1) * min(lgd + s["lgd_add"], 1) for k, (ead, pd, lgd) in PORTFOLIO.items()}
    total = sum(losses.values())
    cet1_after = CET1 - total + PPNR * s["ppnr_mult"]
    return {"losses_by_portfolio": {k: round(v) for k, v in losses.items()}, "total_credit_loss": round(total),
            "cet1_ratio_start": round(CET1 / RWA * 100, 2), "cet1_ratio_end": round(cet1_after / RWA * 100, 2),
            "hurdle_pct": 7.0}


def main():
    banner("22 - Stress Testing Scenario Narrator (CrewAI)")
    results = {name: {"macro": {k: v for k, v in s.items() if k in ("gdp", "unemployment", "house_prices")},
                      **run_scenario(s)} for name, s in SCENARIOS.items()}
    section("Stress results", json.dumps(results, indent=2))
    table = ["| Scenario | Credit loss (m) | CET1 start | CET1 end | vs 7% hurdle |", "|---|---|---|---|---|"]
    for name, r in results.items():
        verdict = "PASS" if r["cet1_ratio_end"] >= r["hurdle_pct"] else "FAIL"
        table.append(f"| {name} | {r['total_credit_loss']:,} | {r['cet1_ratio_start']}% | {r['cet1_ratio_end']}% | {verdict} |")
    table = "\n".join(table)
    section("Results table", table)

    economist = make_agent("Chief Economist", "Describe macro scenarios in plain business language",
                           "You design stress scenarios and explain their transmission to bank portfolios.")
    reporter = make_agent("Stress Testing Lead", "Write the board-level stress testing summary",
                          "You present ICAAP stress results to the board risk committee.")
    t1 = make_task("Scenario results:\n{results}\n\nDescribe each scenario's narrative and how it hits each portfolio.",
                   "Scenario narratives with transmission channels.", economist)
    t2 = make_task("Write the board summary. The results table below is final and is shown to the board separately: "
                   "do not reproduce or recalculate it, just refer to its figures.\n\n{table}\n\n"
                   "Losses by portfolio (millions) per scenario:\n{results}",
                   "Sections: Key messages, Most vulnerable portfolios (cite their loss amounts), "
                   "Management actions (capital, risk appetite, hedging).", reporter, context=[t1])
    section("Board summary", run_crew([economist, reporter], [t1, t2],
                                      {"results": json.dumps(results, indent=2), "table": table}))


if __name__ == "__main__":
    main()
