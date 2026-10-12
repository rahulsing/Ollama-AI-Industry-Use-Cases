"""Reconciliation Exception Agent — CrewAI + Ollama.

Run:  python 01_banking/43_reconciliation_exception_agent/app.py
"""

import json
import sys
from datetime import date
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

LEDGER = [
    {"id": "GL-1", "date": "2026-10-01", "ref": "INV-1001", "amount": 12500.00},
    {"id": "GL-2", "date": "2026-10-02", "ref": "INV-1002", "amount": 8400.00},
    {"id": "GL-3", "date": "2026-10-03", "ref": "INV-1003", "amount": 3150.00},
    {"id": "GL-4", "date": "2026-10-03", "ref": "PAY-SUP-77", "amount": -9200.00},
    {"id": "GL-5", "date": "2026-10-05", "ref": "INV-1005", "amount": 4999.00},
]
BANK = [
    {"id": "BK-1", "date": "2026-10-01", "ref": "INV-1001", "amount": 12500.00},
    {"id": "BK-2", "date": "2026-10-04", "ref": "INV1002", "amount": 8400.00},
    {"id": "BK-3", "date": "2026-10-03", "ref": "INV-1003", "amount": 3135.00},
    {"id": "BK-4", "date": "2026-10-04", "ref": "PAY-SUP-77", "amount": -9200.00},
    {"id": "BK-5", "date": "2026-10-04", "ref": "PAY-SUP-77", "amount": -9200.00},
    {"id": "BK-6", "date": "2026-10-06", "ref": "BANK CHARGES", "amount": -45.00},
]


def norm(ref: str) -> str:
    return ref.replace("-", "").upper()


def reconcile():
    matched, unmatched_bank = [], list(BANK)
    breaks = []
    for g in LEDGER:
        hit = next((b for b in unmatched_bank if norm(b["ref"]) == norm(g["ref"]) and b["amount"] == g["amount"]), None)
        if hit:
            lag = (date.fromisoformat(hit["date"]) - date.fromisoformat(g["date"])).days
            matched.append({"gl": g["id"], "bank": hit["id"], "date_lag_days": lag})
            unmatched_bank.remove(hit)
            continue
        near = next((b for b in unmatched_bank if norm(b["ref"]) == norm(g["ref"])), None)
        if near:
            breaks.append({"type": "AMOUNT_MISMATCH", "gl": g, "bank": near, "difference": round(g["amount"] - near["amount"], 2)})
            unmatched_bank.remove(near)
        else:
            breaks.append({"type": "MISSING_IN_BANK", "gl": g})
    breaks += [{"type": "MISSING_IN_LEDGER", "bank": b} for b in unmatched_bank]
    return matched, breaks


def main():
    banner("43 - Reconciliation Exception Agent (CrewAI)")
    matched, breaks = reconcile()
    section("Auto-matched", json.dumps(matched, indent=2))
    section("Breaks", json.dumps(breaks, indent=2))
    analyst = make_agent("Reconciliation Analyst", "Explain the probable root cause of every break",
                         "Bank operations analyst who knows duplicates, FX/fee deductions, timing and reference errors.")
    lead = make_agent("Operations Team Lead", "Assign resolution actions, owners and priorities",
                      "You run the nostro/GL reconciliation team and manage aged breaks.")
    t1 = make_task("Breaks:\n{breaks}\n\nClassify each break's root cause (duplicate debit, short payment / fee, unrecorded bank charge, "
                   "timing, reference format) with evidence.", "Per-break root cause.", analyst)
    t2 = make_task("Propose resolution per break: journal entry or bank claim, owner, priority, and an overall recon summary.\n\n"
                   "Breaks with exact amounts (quote these; never invent numbers):\n{breaks}",
                   "Action table and summary.", lead, context=[t1])
    section("Resolution plan", run_crew([analyst, lead], [t1, t2], {"breaks": json.dumps(breaks, indent=2)}))


if __name__ == "__main__":
    main()
