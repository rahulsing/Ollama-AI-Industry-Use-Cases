"""Claims Leakage Auditor — CrewAI + Ollama.

Python re-checks a sample of closed claims for overpayment (excess not taken, unapproved repair overruns, no
wear-and-tear deduction, duplicate invoices) and missed recoveries from at-fault third parties; agents explain
the findings and write the recovery and process-fix plan.

Run:  python 03_insurance/10_claims_leakage_auditor/app.py
"""

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

# Claims closed last month. approved = repair estimate the handler authorised; wear_and_tear = deduction due on
# old items (contents cover pays the item's value, not new for old); third_party_at_fault = cost can be recovered
CLOSED = [
    {"claim": "C-101", "team": "Home", "approved": 3_800, "invoice": 3_750, "invoice_no": "INV-4410", "excess": 500,
     "excess_taken": True, "extra_approved": False, "wear_and_tear": 0, "paid": 3_250,
     "third_party_at_fault": False, "recovery_started": False},
    {"claim": "C-102", "team": "Home", "approved": 2_600, "invoice": 2_600, "invoice_no": "INV-4502", "excess": 500,
     "excess_taken": False, "extra_approved": False, "wear_and_tear": 0, "paid": 2_600,
     "third_party_at_fault": False, "recovery_started": False},
    {"claim": "C-103", "team": "Motor", "approved": 4_100, "invoice": 5_050, "invoice_no": "INV-7713", "excess": 300,
     "excess_taken": True, "extra_approved": False, "wear_and_tear": 0, "paid": 4_750,
     "third_party_at_fault": False, "recovery_started": False},
    {"claim": "C-104", "team": "Home", "approved": 1_800, "invoice": 1_800, "invoice_no": "INV-4533", "excess": 250,
     "excess_taken": True, "extra_approved": False, "wear_and_tear": 900, "paid": 1_550,
     "third_party_at_fault": False, "recovery_started": False},
    {"claim": "C-105", "team": "Motor", "approved": 6_400, "invoice": 6_400, "invoice_no": "INV-7790", "excess": 0,
     "excess_taken": True, "extra_approved": False, "wear_and_tear": 0, "paid": 6_400,
     "third_party_at_fault": True, "recovery_started": False},
    {"claim": "C-106", "team": "Motor", "approved": 1_200, "invoice": 1_200, "invoice_no": "INV-7802", "excess": 0,
     "excess_taken": True, "extra_approved": False, "wear_and_tear": 0, "paid": 1_200,
     "third_party_at_fault": True, "recovery_started": True},
    {"claim": "C-107", "team": "Motor", "approved": 1_200, "invoice": 1_200, "invoice_no": "INV-7802", "excess": 0,
     "excess_taken": True, "extra_approved": False, "wear_and_tear": 0, "paid": 1_200,
     "third_party_at_fault": False, "recovery_started": False},
    {"claim": "C-108", "team": "Home", "approved": 5_200, "invoice": 5_600, "invoice_no": "INV-4560", "excess": 500,
     "excess_taken": True, "extra_approved": False, "wear_and_tear": 0, "paid": 5_100,
     "third_party_at_fault": False, "recovery_started": False},
]
OVERRUN_TOLERANCE = 0.10   # invoices up to 10% over the approved estimate can be paid without extra approval
RECOVERY_ACTION = {"duplicate invoice": "ask the repairer for a refund",
                   "repair overrun": "ask the repairer to justify or credit the extra cost",
                   "missed recovery": "send the claim to the at-fault driver's insurer"}


def audit(claims: list[dict]) -> tuple[list[dict], dict]:
    seen = Counter(c["invoice_no"] for c in claims)
    first = {}
    findings, by_issue, by_team, recover, write_off = [], Counter(), defaultdict(int), [], []
    for c in claims:
        issues = []  # (kind, detail, amount)
        cost = c["invoice"]
        if cost > c["approved"] * (1 + OVERRUN_TOLERANCE) and not c["extra_approved"]:
            issues.append(("repair overrun", f"invoice {cost:,} is {cost / c['approved'] - 1:.0%} over the approved "
                                             f"{c['approved']:,} with no extra approval", cost - c["approved"]))
            cost = c["approved"]
        should_pay = cost - c["excess"] - c["wear_and_tear"]
        if not c["excess_taken"]:
            issues.append(("excess not deducted", f"excess of {c['excess']} not deducted", c["excess"]))
        if c["wear_and_tear"] and c["paid"] > should_pay:
            issues.append(("wear and tear not deducted", f"wear-and-tear deduction of {c['wear_and_tear']} not "
                                                         "applied (paid new for old)", c["wear_and_tear"]))
        if seen[c["invoice_no"]] > 1 and c["invoice_no"] in first:
            issues.append(("duplicate invoice", f"invoice {c['invoice_no']} was already paid on "
                                                f"{first[c['invoice_no']]}", c["paid"]))
            should_pay = 0
        first.setdefault(c["invoice_no"], c["claim"])
        over = max(c["paid"] - should_pay, 0)
        missed = c["paid"] if c["third_party_at_fault"] and not c["recovery_started"] else 0
        if missed:
            issues.append(("missed recovery", "third party at fault but no recovery started", missed))
        for kind, _, amount in issues:
            if kind in RECOVERY_ACTION:
                recover.append(f"{c['claim']} ({kind}): {RECOVERY_ACTION[kind]}, {amount:,}")
            else:
                write_off.append(f"{c['claim']} ({kind}): {amount:,}")
        by_issue.update(kind for kind, _, _ in issues)
        by_team[c["team"]] += over + missed
        findings.append({"claim": c["claim"], "team": c["team"], "paid": c["paid"], "should_have_paid": should_pay,
                         "overpaid": over, "missed_recovery": missed,
                         "issues": [f"{kind}: {detail}" for kind, detail, _ in issues] or ["none"]})

    paid = sum(f["paid"] for f in findings)
    over = sum(f["overpaid"] for f in findings)
    missed = sum(f["missed_recovery"] for f in findings)
    summary = {"claims_reviewed": len(findings), "total_paid": paid, "total_overpaid": over,
               "overpaid_share_of_paid": f"{over / paid:.1%}", "total_missed_recovery": missed,
               "claims_with_issues": sum(1 for f in findings if f["issues"] != ["none"]),
               "issues_by_type": dict(by_issue), "overpaid_plus_missed_recovery_by_team": dict(by_team),
               "recover_now": recover,
               "not_recoverable": write_off,
               "not_recoverable_note": "don't chase customers for our own mistakes: fix the process instead"}
    return findings, summary


def main():
    banner("Insurance 10 - Claims Leakage Auditor (CrewAI)")
    findings, summary = audit(CLOSED)
    facts = {"findings": findings, "summary": summary}
    section("Audit checks", json.dumps(facts, indent=2))

    auditor = make_agent("Claims Auditor", "Explain each leakage finding and its likely root cause",
                         "Claims quality auditor. You look for process gaps, not people to blame.")
    manager = make_agent("Claims Manager", "Turn the audit findings into a recovery and process-fix plan",
                         "You run the home and motor claims teams and care about fair, accurate payments.")
    t1 = make_task("Audit facts (exact figures):\n{facts}\n\nFor each claim with issues, explain the finding in 1-2 "
                   "sentences and the likely root cause (e.g. a missing system check, an unclear approval limit).",
                   "Findings per claim.", auditor)
    t2 = make_task("Audit facts (exact figures; quote these, never recalculate):\n{facts}\n\n"
                   "Write the audit report and action plan for the claims leadership team.",
                   "Report with no date, signature or placeholder lines: headline (total overpaid, its share of paid, "
                   "total missed recovery); 'Recover now': every recover_now line copied exactly; 'Not recoverable': "
                   "the not_recoverable lines with not_recoverable_note; 3-4 process fixes, each with an owner role "
                   "(e.g. an automatic excess check in the "
                   "claims system, duplicate-invoice blocking, an approval step for overruns, a recovery checklist when "
                   "the third party is at fault); and team coaching points without naming individuals.",
                   manager, context=[t1])
    section("Audit report", run_crew([auditor, manager], [t1, t2], {"facts": json.dumps(facts, indent=2)}))


if __name__ == "__main__":
    main()
