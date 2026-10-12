"""Operational Risk Incident Analyzer — LangChain structured output + Ollama.

Run:  python 01_banking/50_operational_risk_analyzer/app.py
"""

import sys
from collections import Counter
from pathlib import Path
from typing import Literal

sys.path.append(str(Path(__file__).resolve().parents[2]))
from pydantic import BaseModel, Field

from common import banner, run_structured, section

INCIDENTS = [
    ("INC-101", 42_000, "Teller processed a withdrawal on a forged signature; customer reported unauthorised debit next day."),
    ("INC-102", 180_000, "Core banking batch job failed overnight; 12,000 salary credits delayed by 6 hours, compensation paid."),
    ("INC-103", 7_500, "Wrong FX rate keyed manually for a corporate remittance; difference absorbed by the bank."),
    ("INC-104", 0, "Phishing email led an employee to enter credentials; account locked by SOC within 20 minutes, no loss."),
    ("INC-105", 250_000, "Regulator fined the bank for late filing of currency transaction reports for two quarters."),
    ("INC-106", 15_000, "Branch ATM damaged by flood water; cash written off and repairs required."),
]


class Incident(BaseModel):
    basel_event_type: Literal["Internal Fraud", "External Fraud", "Employment Practices & Workplace Safety",
                              "Clients, Products & Business Practices", "Damage to Physical Assets",
                              "Business Disruption & System Failures", "Execution, Delivery & Process Management"]
    root_cause: Literal["people", "process", "systems", "external"]
    severity: Literal["low", "medium", "high"]
    near_miss: bool = Field(description="True if no financial loss occurred")
    control_failure: str = Field(description="Which control failed, one sentence")
    recommended_control: str = Field(description="Preventive or detective control to add, one sentence")


def main():
    banner("50 - Operational Risk Incident Analyzer (LangChain structured output)")
    system = (
        "You are an operational risk analyst. Classify the incident using the Basel II level-1 event types:\n"
        "- Internal Fraud: dishonest acts by employees for personal gain\n"
        "- External Fraud: theft, forgery, hacking or scams by third parties\n"
        "- Employment Practices & Workplace Safety: HR, discrimination, injury\n"
        "- Clients, Products & Business Practices: mis-selling, regulatory breaches, fines\n"
        "- Damage to Physical Assets: natural disasters, fire, flood, vandalism\n"
        "- Business Disruption & System Failures: IT outages, batch failures, utilities\n"
        "- Execution, Delivery & Process Management: keying errors, failed processing, data entry mistakes\n"
        "Honest mistakes and outages are never fraud. Describe the control failure in words, not yes/no."
    )
    results = []
    for iid, loss, text in INCIDENTS:
        r = run_structured(system, f"Loss: {loss}. {text}", Incident)
        results.append((iid, loss, r))
        section(f"{iid} (loss {loss:,})", f"{text}\n{r.model_dump_json(indent=2)}")

    by_type = Counter(r.basel_event_type for _, _, r in results)
    loss_by_type = Counter()
    for _, loss, r in results:
        loss_by_type[r.basel_event_type] += loss
    section("Summary", "\n".join(f"{t}: {n} incident(s), loss {loss_by_type[t]:,}" for t, n in by_type.most_common()))


if __name__ == "__main__":
    main()
