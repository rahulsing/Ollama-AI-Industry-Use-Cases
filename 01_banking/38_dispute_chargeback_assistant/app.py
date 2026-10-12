"""Dispute & Chargeback Assistant — LangChain tool-calling agent + Ollama.

Run:  python 01_banking/38_dispute_chargeback_assistant/app.py
      python 01_banking/38_dispute_chargeback_assistant/app.py "I cancelled my gym membership but TX-903 still charged me"
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from langchain_core.tools import tool

from common import banner, run_agent, section

TRANSACTIONS = {
    "TX-901": {"date": "2026-09-18", "merchant": "SkyHigh Airlines", "amount": 640.00, "network": "Visa", "status": "posted"},
    "TX-902": {"date": "2026-09-22", "merchant": "TechMart Online", "amount": 899.00, "network": "Mastercard", "status": "posted"},
    "TX-903": {"date": "2026-10-01", "merchant": "FitLife Gym", "amount": 49.99, "network": "Visa", "status": "posted"},
}

REASON_CODES = {  # simplified
    "goods_not_received": {"Visa": "13.1", "Mastercard": "4855", "evidence": "Expected delivery date, merchant contact attempts", "window_days": 120},
    "cancelled_recurring": {"Visa": "13.2", "Mastercard": "4841", "evidence": "Cancellation confirmation/date", "window_days": 120},
    "not_as_described": {"Visa": "13.3", "Mastercard": "4853", "evidence": "Description vs. received item, return proof", "window_days": 120},
    "duplicate_charge": {"Visa": "12.6.1", "Mastercard": "4834", "evidence": "Both transaction references", "window_days": 120},
    "fraud_card_absent": {"Visa": "10.4", "Mastercard": "4837", "evidence": "Customer declaration, card blocked", "window_days": 120},
}


@tool
def lookup_transaction(txn_id: str) -> dict:
    """Look up a card transaction by id (e.g. TX-901)."""
    return TRANSACTIONS.get(txn_id.upper(), {"error": "not found"})


@tool
def reason_code_rules(dispute_type: str, network: str) -> dict:
    """Get chargeback reason code, required evidence and time window. dispute_type is one of:
    goods_not_received, cancelled_recurring, not_as_described, duplicate_charge, fraud_card_absent."""
    r = REASON_CODES.get(dispute_type)
    return {"reason_code": r[network], "evidence_required": r["evidence"], "window_days": r["window_days"]} if r else {"error": "unknown type"}


SYSTEM = (
    "You are a card disputes specialist. Look up the transaction, classify the dispute type, get the reason code rules, "
    "then reply with: dispute type, reason code, evidence the customer must provide, whether a temporary credit applies, "
    "and a short dispute case summary for the back office. If the merchant should be contacted first, say so."
)


def main():
    banner("38 - Dispute & Chargeback Assistant (LangChain agent)")
    q = sys.argv[1] if len(sys.argv) > 1 else (
        "I ordered a laptop from TechMart Online (TX-902) on 22 Sept, it was due 29 Sept and never arrived. The merchant ignores my emails.")
    section("Customer", q)
    section("Assistant", run_agent(SYSTEM, [lookup_transaction, reason_code_rules], q))


if __name__ == "__main__":
    main()
