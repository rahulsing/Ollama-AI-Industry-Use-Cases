"""Internal Audit Assistant — CrewAI + Ollama.

Run:  python 01_banking/49_internal_audit_assistant/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

APPROVAL_LIMITS = {"officer": 50_000, "manager": 250_000, "head": 1_000_000}
SAMPLE = [  # payments released in the quarter (sample)
    {"id": "P-01", "amount": 42_000, "maker": "u12", "checker": "u31", "checker_role": "officer", "vendor_in_master": True, "weekend": False},
    {"id": "P-02", "amount": 180_000, "maker": "u12", "checker": "u12", "checker_role": "manager", "vendor_in_master": True, "weekend": False},
    {"id": "P-03", "amount": 310_000, "maker": "u18", "checker": "u44", "checker_role": "manager", "vendor_in_master": True, "weekend": False},
    {"id": "P-04", "amount": 49_900, "maker": "u20", "checker": "u31", "checker_role": "officer", "vendor_in_master": False, "weekend": True},
    {"id": "P-05", "amount": 49_800, "maker": "u20", "checker": "u31", "checker_role": "officer", "vendor_in_master": False, "weekend": True},
    {"id": "P-06", "amount": 75_000, "maker": "u15", "checker": "u44", "checker_role": "manager", "vendor_in_master": True, "weekend": False},
]


def test_controls(rows):
    exc = []
    for r in rows:
        if r["maker"] == r["checker"]:
            exc.append({"id": r["id"], "control": "Maker-checker / segregation of duties", "detail": "Same user made and approved"})
        if r["amount"] > APPROVAL_LIMITS[r["checker_role"]]:
            exc.append({"id": r["id"], "control": "Delegation of authority", "detail": f"{r['amount']:,} > {r['checker_role']} limit"})
        if not r["vendor_in_master"]:
            exc.append({"id": r["id"], "control": "Vendor master", "detail": "Payee not in approved vendor master"})
    near = [r["id"] for r in rows if 0.95 * APPROVAL_LIMITS["officer"] <= r["amount"] < APPROVAL_LIMITS["officer"]]
    if len(near) >= 2:
        exc.append({"id": ",".join(near), "control": "Limit splitting", "detail": "Multiple payments just below officer limit"})
    return {"sample_size": len(rows), "exceptions": exc}


def main():
    banner("49 - Internal Audit Assistant (CrewAI)")
    results = test_controls(SAMPLE)
    section("Control testing", json.dumps(results, indent=2))
    auditor = make_agent("Internal Auditor", "Evaluate control exceptions and their root causes",
                         "IIA-certified auditor focusing on payments and fraud risk.")
    manager = make_agent("Audit Manager", "Write audit findings with ratings and agreed actions",
                         "You write findings in Condition / Criteria / Cause / Effect / Recommendation format.")
    t1 = make_task("Sample:\n{sample}\n\nResults:\n{results}\n\nEvaluate each exception, note patterns (e.g. same users), possible fraud indicators.",
                   "Exception evaluation.", auditor)
    t2 = make_task("Write the audit findings.\n\nControl test exceptions (quote these exactly):\n{results}", "Findings (Condition, Criteria, Cause, Effect, Recommendation, Rating High/Medium/Low), "
                   "overall control environment opinion (Satisfactory / Needs improvement / Unsatisfactory).", manager, context=[t1])
    section("Audit report", run_crew([auditor, manager], [t1, t2], {"sample": json.dumps(SAMPLE, indent=2), "results": json.dumps(results, indent=2)}))


if __name__ == "__main__":
    main()
