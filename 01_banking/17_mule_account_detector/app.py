"""Money Mule Account Detector — CrewAI + Ollama.

Run:  python 01_banking/17_mule_account_detector/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

ACCOUNTS = [  # 30-day aggregates
    {"acct": "A-100", "age_days": 21, "inflow": 18400, "outflow": 18100, "unique_senders": 27, "avg_hold_hours": 3,
     "age_of_holder": 19, "device_shared_with": 2, "crypto_or_cash_out_pct": 85},
    {"acct": "A-101", "age_days": 1400, "inflow": 5200, "outflow": 4700, "unique_senders": 2, "avg_hold_hours": 240,
     "age_of_holder": 41, "device_shared_with": 0, "crypto_or_cash_out_pct": 5},
    {"acct": "A-102", "age_days": 60, "inflow": 9100, "outflow": 8900, "unique_senders": 11, "avg_hold_hours": 12,
     "age_of_holder": 22, "device_shared_with": 1, "crypto_or_cash_out_pct": 60},
    {"acct": "A-103", "age_days": 700, "inflow": 30000, "outflow": 12000, "unique_senders": 4, "avg_hold_hours": 500,
     "age_of_holder": 55, "device_shared_with": 0, "crypto_or_cash_out_pct": 0},
]


def mule_score(a: dict) -> dict:
    pass_through = a["outflow"] / a["inflow"] if a["inflow"] else 0
    s = 0
    s += 25 if pass_through > 0.9 else 0
    s += 20 if a["age_days"] < 90 else 0
    s += 15 if a["unique_senders"] > 10 else 0
    s += 15 if a["avg_hold_hours"] < 24 else 0
    s += 10 if a["age_of_holder"] < 25 else 0
    s += 10 if a["device_shared_with"] > 0 else 0
    s += 5 if a["crypto_or_cash_out_pct"] > 50 else 0
    return {"acct": a["acct"], "pass_through_ratio": round(pass_through, 2), "mule_score": s,
            "tier": "HIGH" if s >= 70 else "MEDIUM" if s >= 40 else "LOW"}


def main():
    banner("17 - Money Mule Account Detector (CrewAI)")
    scores = sorted((mule_score(a) for a in ACCOUNTS), key=lambda x: -x["mule_score"])
    section("Mule scores", json.dumps(scores, indent=2))

    analyst = make_agent("Fraud Analyst", "Explain why accounts look like money mules",
                         "Specialist in mule networks recruited via social media 'easy money' scams.")
    investigator = make_agent("Fraud Investigator", "Recommend proportionate actions per account",
                              "You balance stopping fraud with avoiding harm to genuine customers and young people being exploited.")
    t1 = make_task("Account data:\n{accounts}\n\nScores:\n{scores}\n\nExplain the mule indicators for each account.",
                   "Per-account explanation.", analyst)
    t2 = make_task("Recommend actions per account (e.g. freeze outbound, contact customer, close & report, "
                   "safeguarding message for possibly-exploited young holders, network link analysis).",
                   "Prioritised action list.", investigator, context=[t1])
    section("Recommendations", run_crew([analyst, investigator], [t1, t2],
                                        {"accounts": json.dumps(ACCOUNTS, indent=2), "scores": json.dumps(scores, indent=2)}))


if __name__ == "__main__":
    main()
