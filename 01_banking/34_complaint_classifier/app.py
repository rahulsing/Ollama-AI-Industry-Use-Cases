"""Complaint Classifier & Router — LangChain structured output + Ollama.

Run:  python 01_banking/34_complaint_classifier/app.py
"""

import sys
from pathlib import Path
from typing import Literal

sys.path.append(str(Path(__file__).resolve().parents[2]))
from pydantic import BaseModel, Field

from common import banner, run_structured, section

COMPLAINTS = [
    "I was charged a 35 overdraft fee twice for the same transaction and nobody at the branch could explain why. Refund it!",
    "My father has dementia and someone at your bank sold him a 10-year insurance-linked investment. He doesn't understand it.",
    "The mobile app keeps logging me out when I try to pay bills. Very annoying.",
    "Money was taken from my account for a purchase I never made in another country, and my card is still with me.",
    "Your loan agent called me 6 times a day and threatened to tell my employer about my missed EMI.",
]

ROUTING = {"fees_charges": "Retail Ops - Fees", "mis_selling": "Conduct & Compliance", "digital_banking": "Digital Support",
           "fraud_dispute": "Fraud Operations", "collections_conduct": "Collections Oversight", "other": "Customer Service"}
SLA_DAYS = {"low": 15, "medium": 10, "high": 3, "critical": 1}


class Complaint(BaseModel):
    product: Literal["current_account", "credit_card", "debit_card", "loan", "investment_insurance", "mobile_app", "other"]
    category: Literal["fees_charges", "mis_selling", "digital_banking", "fraud_dispute", "collections_conduct", "other"]
    severity: Literal["low", "medium", "high", "critical"]
    vulnerable_customer: bool
    regulatory_reportable: bool = Field(description="True for mis-selling, harassment, unauthorised transactions")
    sentiment: Literal["neutral", "frustrated", "angry", "distressed"]
    summary: str = Field(description="One-sentence summary")


def main():
    banner("34 - Complaint Classifier & Router (LangChain structured output)")
    system = (
        "Classify the banking complaint. Categories: fees_charges = disputed fees/interest; mis_selling = a product "
        "sold that was unsuitable or not understood; digital_banking = app/online issues; fraud_dispute = unauthorised "
        "transactions or scams; collections_conduct = debt collection behaviour. Vulnerable customers, harassment and "
        "fraud are at least 'high' severity."
    )
    for text in COMPLAINTS:
        c = run_structured(system, text, Complaint)
        section(text[:70] + "...", f"{c.model_dump_json(indent=2)}\n-> Route: {ROUTING[c.category]} | SLA: {SLA_DAYS[c.severity]} day(s)"
                + (" | FLAG: regulatory log" if c.regulatory_reportable else ""))


if __name__ == "__main__":
    main()
