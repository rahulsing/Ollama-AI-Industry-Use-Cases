"""AML Transaction Monitoring Agent — CrewAI + Ollama.

Deterministic AML rules raise alerts (auditable); agents investigate and triage.

Run:  python 01_banking/09_aml_transaction_monitoring/app.py
"""

import json
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

CUSTOMER = {"id": "CUST-7781", "name": "Marco Rinaldi", "occupation": "Restaurant owner",
            "expected_monthly_turnover": 15_000, "risk_rating": "Medium", "country": "IT"}

TXNS = [  # date, type, amount, counterparty, country
    ("2026-09-01", "cash_deposit", 9_500, "Branch 12", "IT"),
    ("2026-09-02", "cash_deposit", 9_800, "Branch 07", "IT"),
    ("2026-09-03", "cash_deposit", 9_700, "Branch 12", "IT"),
    ("2026-09-04", "wire_out", 27_000, "Oceanic Trading FZE", "AE"),
    ("2026-09-10", "card_payment", 230, "Metro Cash&Carry", "IT"),
    ("2026-09-15", "wire_in", 48_000, "Lindell Holdings Ltd", "VG"),
    ("2026-09-16", "wire_out", 47_500, "Kestrel Imports", "HK"),
    ("2026-09-20", "cash_deposit", 3_200, "Branch 12", "IT"),
]

HIGH_RISK = {"VG", "KY", "PA", "IR", "KP"}
CTR_THRESHOLD = 10_000


def detect(txns) -> list[dict]:
    alerts, rows = [], [dict(zip(["date", "type", "amount", "cp", "country"], t)) for t in txns]
    for r in rows:
        r["d"] = datetime.fromisoformat(r["date"])

    # 1. Structuring: >=3 cash deposits just under the threshold in 7 days
    near = [r for r in rows if r["type"] == "cash_deposit" and 0.9 * CTR_THRESHOLD <= r["amount"] < CTR_THRESHOLD]
    if len(near) >= 3 and near[-1]["d"] - near[0]["d"] <= timedelta(days=7):
        alerts.append({"rule": "STRUCTURING", "evidence": [(r["date"], r["amount"]) for r in near]})

    # 2. Rapid movement: inbound wire followed by >=90% outbound within 2 days
    for i in (r for r in rows if r["type"] == "wire_in"):
        for o in (r for r in rows if r["type"] == "wire_out"):
            if timedelta(0) <= o["d"] - i["d"] <= timedelta(days=2) and o["amount"] >= 0.9 * i["amount"]:
                alerts.append({"rule": "RAPID_PASS_THROUGH", "evidence": [(i["date"], i["amount"], i["cp"]),
                                                                           (o["date"], o["amount"], o["cp"])]})

    # 3. High-risk jurisdiction
    hr = [(r["date"], r["amount"], r["country"]) for r in rows if r["country"] in HIGH_RISK]
    if hr:
        alerts.append({"rule": "HIGH_RISK_JURISDICTION", "evidence": hr})

    # 4. Turnover vs. profile
    monthly = defaultdict(float)
    for r in rows:
        monthly[r["date"][:7]] += r["amount"]
    for m, v in monthly.items():
        if v > 3 * CUSTOMER["expected_monthly_turnover"]:
            alerts.append({"rule": "PROFILE_DEVIATION", "evidence": f"{m} turnover {v:,.0f} vs expected "
                                                                    f"{CUSTOMER['expected_monthly_turnover']:,}"})
    return alerts


def main():
    banner("09 - AML Transaction Monitoring Agent (CrewAI)")
    alerts = detect(TXNS)
    section("Rule alerts", json.dumps(alerts, indent=2))

    investigator = make_agent("AML Investigator", "Investigate alerts and assess whether activity is suspicious",
                              "Certified AML specialist (CAMS) experienced in typologies: structuring, layering, trade-based ML.")
    officer = make_agent("MLRO / Compliance Officer", "Decide the alert outcome in line with regulation",
                         "Money Laundering Reporting Officer accountable for SAR filing decisions.")
    t1 = make_task(
        "Customer profile:\n{customer}\n\nTransactions:\n{txns}\n\nAlerts:\n{alerts}\n\n"
        "Investigate. Link the alerts into a coherent picture, list typologies, and note any innocent explanations to check.",
        "Investigation summary with typologies, risk indicators and open questions for the customer.", investigator)
    t2 = make_task(
        "Decide the outcome.",
        "First line 'Decision: <CODE>' where CODE is exactly one of CLOSE_FALSE_POSITIVE, ENHANCED_MONITORING, FILE_SAR "
        "(if a SAR is filed the account is also monitored, so choose FILE_SAR). Then risk score 1-10, "
        "justification and next steps (RFI to customer, EDD, account restrictions).", officer, context=[t1])
    section("Alert triage", run_crew([investigator, officer], [t1, t2], {
        "customer": json.dumps(CUSTOMER, indent=2), "txns": json.dumps(TXNS, indent=2),
        "alerts": json.dumps(alerts, indent=2)}))


if __name__ == "__main__":
    main()
