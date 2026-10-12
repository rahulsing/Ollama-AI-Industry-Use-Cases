"""ESG Investment Screener — CrewAI + Ollama.

Run:  python 01_banking/31_esg_investment_screener/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

FUNDS = [  # fictional fund universe
    {"fund": "Global Clean Energy Fund", "esg_score": 82, "carbon_intensity": 45, "fossil_fuel_pct": 0, "weapons_pct": 0, "tobacco_pct": 0, "ter_pct": 0.85, "return_5y_pct": 9.1},
    {"fund": "World Index Tracker", "esg_score": 58, "carbon_intensity": 140, "fossil_fuel_pct": 6, "weapons_pct": 1, "tobacco_pct": 1, "ter_pct": 0.12, "return_5y_pct": 10.4},
    {"fund": "ESG Leaders Equity", "esg_score": 76, "carbon_intensity": 70, "fossil_fuel_pct": 1, "weapons_pct": 0, "tobacco_pct": 0, "ter_pct": 0.30, "return_5y_pct": 9.8},
    {"fund": "Emerging Markets Value", "esg_score": 41, "carbon_intensity": 310, "fossil_fuel_pct": 14, "weapons_pct": 0, "tobacco_pct": 3, "ter_pct": 0.55, "return_5y_pct": 7.2},
    {"fund": "Green Bond Fund", "esg_score": 79, "carbon_intensity": 30, "fossil_fuel_pct": 0, "weapons_pct": 0, "tobacco_pct": 0, "ter_pct": 0.25, "return_5y_pct": 3.4},
    {"fund": "Aerospace & Defence Opportunities", "esg_score": 49, "carbon_intensity": 120, "fossil_fuel_pct": 0, "weapons_pct": 35, "tobacco_pct": 0, "ter_pct": 0.65, "return_5y_pct": 12.0},
]
PREFS = {"min_esg_score": 70, "max_carbon_intensity": 100, "exclude": ["weapons", "tobacco"], "max_fossil_fuel_pct": 2,
         "client_goal": "Long-term growth with balanced risk; values climate action"}


def screen(f: dict):
    reasons = []
    if f["esg_score"] < PREFS["min_esg_score"]: reasons.append(f"ESG score {f['esg_score']} < {PREFS['min_esg_score']}")
    if f["carbon_intensity"] > PREFS["max_carbon_intensity"]: reasons.append(f"carbon intensity {f['carbon_intensity']}")
    for x in PREFS["exclude"]:
        if f[f"{x}_pct"] > 0: reasons.append(f"{x} exposure {f[f'{x}_pct']}%")
    if f["fossil_fuel_pct"] > PREFS["max_fossil_fuel_pct"]: reasons.append(f"fossil fuel {f['fossil_fuel_pct']}%")
    return {"fund": f["fund"], "passes": not reasons, "fail_reasons": reasons}


def main():
    banner("31 - ESG Investment Screener (CrewAI)")
    results = [screen(f) for f in FUNDS]
    section("Screening", json.dumps(results, indent=2))
    esg = make_agent("ESG Analyst", "Explain ESG screening outcomes and trade-offs",
                     "Sustainable-investing analyst who knows SFDR, exclusions vs best-in-class and greenwashing risks.")
    advisor = make_agent("Investment Advisor", "Build a shortlist that meets the client's values and financial goals",
                         "You balance values, diversification, cost and expected return.")
    t1 = make_task("Funds:\n{funds}\n\nPreferences:\n{prefs}\n\nScreening:\n{results}\n\n"
                   "Explain why funds passed/failed and the return/cost trade-offs of applying these exclusions.",
                   "ESG analysis.", esg)
    t2 = make_task("Recommend a shortlist and a simple allocation among passing funds only, noting diversification gaps.\n\n"
                   "Screening results (only funds with passes=true may be recommended):\n{results}",
                   "Shortlist with allocation %, rationale, and trade-offs to discuss with the client.", advisor, context=[t1])
    section("Recommendation", run_crew([esg, advisor], [t1, t2], {
        "funds": json.dumps(FUNDS, indent=2), "prefs": json.dumps(PREFS, indent=2), "results": json.dumps(results, indent=2)}))


if __name__ == "__main__":
    main()
