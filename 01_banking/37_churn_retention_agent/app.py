"""Customer Churn Retention Agent — CrewAI + Ollama.

Run:  python 01_banking/37_churn_retention_agent/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

CUSTOMERS = [
    {"id": "C-11", "tenure_years": 8, "balance_trend_3m_pct": -62, "salary_credit_stopped": True, "logins_trend_pct": -70,
     "complaints_90d": 2, "products": 3, "value_segment": "Affluent", "note": "Complained about FX fees twice"},
    {"id": "C-12", "tenure_years": 2, "balance_trend_3m_pct": 5, "salary_credit_stopped": False, "logins_trend_pct": 10,
     "complaints_90d": 0, "products": 2, "value_segment": "Mass", "note": ""},
    {"id": "C-13", "tenure_years": 4, "balance_trend_3m_pct": -35, "salary_credit_stopped": False, "logins_trend_pct": -40,
     "complaints_90d": 1, "products": 1, "value_segment": "Mass affluent", "note": "Asked about mortgage rates, then went quiet"},
]


def churn_risk(c: dict) -> dict:
    s = 0
    s += 30 if c["salary_credit_stopped"] else 0
    s += min(25, max(0, -c["balance_trend_3m_pct"]) * 0.4)
    s += min(20, max(0, -c["logins_trend_pct"]) * 0.25)
    s += c["complaints_90d"] * 10
    s += 10 if c["products"] <= 1 else 0
    return {"id": c["id"], "churn_score": round(s), "risk": "HIGH" if s >= 60 else "MEDIUM" if s >= 30 else "LOW"}


def main():
    banner("37 - Customer Churn Retention Agent (CrewAI)")
    risks = [churn_risk(c) for c in CUSTOMERS]
    section("Churn risk", json.dumps(risks, indent=2))
    analyst = make_agent("Retention Analyst", "Diagnose likely churn reasons per customer",
                         "Customer analytics specialist who reads behavioural signals.")
    success = make_agent("Customer Success Manager", "Design personalised save actions within budget",
                         "You decide retention offers (fee waivers, rate matches, RM outreach) proportional to customer value.")
    t1 = make_task("Customers:\n{customers}\n\nRisk:\n{risks}\n\nDiagnose likely churn drivers for MEDIUM/HIGH risk customers.",
                   "Per-customer diagnosis.", analyst)
    t2 = make_task("Design a retention play per at-risk customer: action, offer, owner, channel, script opener (1 sentence), success metric.",
                   "Retention plan.", success, context=[t1])
    section("Retention plan", run_crew([analyst, success], [t1, t2], {"customers": json.dumps(CUSTOMERS, indent=2),
                                                                       "risks": json.dumps(risks, indent=2)}))


if __name__ == "__main__":
    main()
