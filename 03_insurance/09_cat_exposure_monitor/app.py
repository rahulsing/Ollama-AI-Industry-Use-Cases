"""Catastrophe Exposure Monitor — CrewAI + Ollama.

Python adds up the home insurance book by zone, runs 1-in-200 windstorm and flood scenarios through the
reinsurance programme and checks them against the risk appetite; agents explain the drivers and write the
actions before the winter storm season.

Run:  python 03_insurance/09_cat_exposure_monitor/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

# Home insurance book by zone. tiv = total insured value; damage ratio = share of tiv a 1-in-200 event destroys
# (from the catastrophe model); limit = most tiv the risk appetite allows in the zone; growth = last 12 months
ZONES = [
    {"zone": "Z1 Coastal East", "main_hazard": "windstorm and storm surge", "policies": 18_000,
     "tiv": 5_400_000_000, "limit": 5_000_000_000, "growth_12m": 0.06, "windstorm_dr": 0.015, "flood_dr": 0.004},
    {"zone": "Z2 River Valley", "main_hazard": "river flood", "policies": 9_500,
     "tiv": 2_850_000_000, "limit": 2_500_000_000, "growth_12m": 0.11, "windstorm_dr": 0.004, "flood_dr": 0.022},
    {"zone": "Z3 Inland Urban", "main_hazard": "surface water flooding", "policies": 42_000,
     "tiv": 10_500_000_000, "limit": 14_000_000_000, "growth_12m": 0.03, "windstorm_dr": 0.003, "flood_dr": 0.002},
    {"zone": "Z4 Upland Rural", "main_hazard": "windstorm", "policies": 6_000,
     "tiv": 1_500_000_000, "limit": 2_500_000_000, "growth_12m": 0.01, "windstorm_dr": 0.008, "flood_dr": 0.001},
]
# Catastrophe excess-of-loss reinsurance: we pay the first 25m of an event, reinsurers the next 100m
RETENTION, RI_LIMIT = 25_000_000, 100_000_000
CAPITAL = 400_000_000
APPETITE = 30_000_000    # the most the board accepts losing (after reinsurance) from one 1-in-200 event


def m(x: float) -> str:
    return f"{x / 1e9:.2f}bn" if x >= 1e9 else f"{x / 1e6:.1f}m"


def scenarios() -> tuple[list[dict], list[dict]]:
    zones = [{"zone": z["zone"], "main_hazard": z["main_hazard"], "policies": z["policies"], "tiv": m(z["tiv"]),
              "appetite_limit": m(z["limit"]), "limit_used": f"{z['tiv'] / z['limit']:.0%}",
              "over_limit_by": m(z["tiv"] - z["limit"]) if z["tiv"] > z["limit"] else None,
              "growth_12m": f"{z['growth_12m']:+.0%}",
              "windstorm_loss": m(z["tiv"] * z["windstorm_dr"]), "flood_loss": m(z["tiv"] * z["flood_dr"])}
             for z in ZONES]
    events = []
    for peril in ("windstorm", "flood"):
        losses = {z["zone"]: z["tiv"] * z[f"{peril}_dr"] for z in ZONES}
        gross = sum(losses.values())
        recovered = min(max(gross - RETENTION, 0), RI_LIMIT)
        net = gross - recovered
        top = max(losses, key=losses.get)
        events.append({"scenario": f"1-in-200 {peril}", "gross_loss": m(gross), "reinsurance_recovery": m(recovered),
                       "net_loss": m(net), "net_loss_share_of_capital": f"{net / CAPITAL:.1%}", "appetite": m(APPETITE),
                       "within_appetite": net <= APPETITE,
                       "reinsurance_exhausted_by": m(gross - RETENTION - RI_LIMIT) if gross > RETENTION + RI_LIMIT else None,
                       "extra_reinsurance_limit_needed": m(net - APPETITE) if net > APPETITE else None,
                       "biggest_zone": f"{top} ({losses[top] / gross:.0%} of the loss)"})
    return zones, events


def main():
    banner("Insurance 09 - Catastrophe Exposure Monitor (CrewAI)")
    zones, events = scenarios()
    facts = {"zones": zones, "scenarios": events,
             "reinsurance": f"{m(RI_LIMIT)} excess of {m(RETENTION)} per event", "capital": m(CAPITAL)}
    section("Exposure & scenarios", json.dumps(facts, indent=2))

    analyst = make_agent("Exposure Analyst", "Explain where the catastrophe exposure comes from and what is driving it",
                         "Catastrophe risk analyst who turns model results into plain explanations for underwriters.")
    cuo = make_agent("Chief Underwriting Officer", "Decide the actions that bring exposure back within appetite",
                     "You own the home insurance book: you protect the company's capital without abandoning customers.")
    t1 = make_task("Exposure facts (exact figures):\n{facts}\n\nExplain which zones and perils drive the 1-in-200 "
                   "losses, which zones are over their appetite limit, and how recent growth contributed.",
                   "Findings: by scenario and by zone.", analyst)
    t2 = make_task("Exposure facts (exact figures; quote these, never recalculate):\n{facts}\n\n"
                   "Write the actions memo for the board risk committee.",
                   "Memo, with no date, signature or placeholder lines and no currency symbols: the position in 2-3 "
                   "sentences covering both scenarios against appetite; for each zone over its limit, 2-3 actions "
                   "that fit its main hazard (e.g. slow new business, price for the hazard, require roof and window "
                   "standards for windstorm or flood resilience measures for flood at renewal; never cancel existing "
                   "customers mid-term); the reinsurance action for any scenario outside appetite, quoting "
                   "reinsurance_exhausted_by and extra_reinsurance_limit_needed; and what to monitor monthly.",
                   cuo, context=[t1])
    section("Actions memo", run_crew([analyst, cuo], [t1, t2], {"facts": json.dumps(facts, indent=2)}))


if __name__ == "__main__":
    main()
