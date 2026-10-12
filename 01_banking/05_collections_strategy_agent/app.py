"""Collections & Recovery Strategist — CrewAI + Ollama.

Run:  python 01_banking/05_collections_strategy_agent/app.py
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

ACCOUNTS = [
    {"id": "L-01", "dpd": 12, "outstanding": 2400, "promises_broken": 0, "contact_rate": 0.9, "hardship_flag": False},
    {"id": "L-02", "dpd": 45, "outstanding": 8100, "promises_broken": 2, "contact_rate": 0.4, "hardship_flag": False},
    {"id": "L-03", "dpd": 75, "outstanding": 15200, "promises_broken": 1, "contact_rate": 0.2, "hardship_flag": True},
    {"id": "L-04", "dpd": 5, "outstanding": 900, "promises_broken": 0, "contact_rate": 1.0, "hardship_flag": False},
    {"id": "L-05", "dpd": 120, "outstanding": 22000, "promises_broken": 3, "contact_rate": 0.1, "hardship_flag": False},
    {"id": "L-06", "dpd": 35, "outstanding": 4300, "promises_broken": 0, "contact_rate": 0.7, "hardship_flag": True},
]


def bucket(dpd: int) -> str:
    return "1-29 (early)" if dpd < 30 else "30-59" if dpd < 60 else "60-89" if dpd < 90 else "90+ (NPA)"


def propensity(a: dict) -> str:
    p = 0.8 - a["dpd"] / 200 - a["promises_broken"] * 0.1 + a["contact_rate"] * 0.2
    return "High" if p > 0.6 else "Medium" if p > 0.35 else "Low"


def segment(accounts: list) -> dict:
    seg = defaultdict(list)
    for a in accounts:
        seg[f"{bucket(a['dpd'])} | PTP {propensity(a)}"].append(
            {"id": a["id"], "outstanding": a["outstanding"], "hardship": a["hardship_flag"]})
    return dict(seg)


def main():
    banner("05 - Collections & Recovery Strategist (CrewAI)")
    segments = segment(ACCOUNTS)
    section("Segments", json.dumps(segments, indent=2))

    strategist = make_agent("Collections Strategist", "Design the most effective treatment per segment",
                            "You run a collections department and optimise recovery and cost-to-collect.")
    conduct = make_agent("Conduct & Fair Treatment Reviewer", "Ensure strategies treat customers fairly",
                         "You apply consumer-duty and fair debt collection principles, protecting vulnerable customers.")
    t1 = make_task(
        "Segments (DPD bucket | propensity-to-pay):\n{segments}\n\n"
        "For each segment propose channel, contact frequency, offer (e.g. payment plan, settlement), and escalation.",
        "Table-like list per segment: channel, frequency, offer, escalation trigger.", strategist)
    t2 = make_task(
        "Review the strategy for fair treatment. Accounts flagged hardship=true need special handling. "
        "Amend anything aggressive and produce the final strategy.",
        "Final strategy per segment plus a 'Conduct notes' section.", conduct, context=[t1])
    section("Collections strategy", run_crew([strategist, conduct], [t1, t2], {"segments": json.dumps(segments, indent=2)}))


if __name__ == "__main__":
    main()
