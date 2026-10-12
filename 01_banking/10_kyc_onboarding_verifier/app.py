"""KYC Onboarding Verifier — LangChain tool-calling agent + Ollama.

Run:  python 01_banking/10_kyc_onboarding_verifier/app.py
"""

import re
import sys
from datetime import date
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from langchain_core.tools import tool

from common import banner, run_agent, section

APPLICATION = {
    "form": {"full_name": "Ananya R. Iyer", "dob": "1991-04-22", "address": "14 Lake View Rd, Bengaluru 560001",
             "pan": "AKPPI4521L", "occupation": "Architect", "source_of_funds": "Salary"},
    "id_document": {"type": "Passport", "number": "Z4829175", "name": "ANANYA RAMESH IYER",
                    "dob": "1991-04-22", "expiry": "2026-08-30"},
    "address_proof": {"type": "Utility bill", "address": "14 Lakeview Road, Bangalore 560001", "issue_date": "2026-06-10"},
}

ID_FORMATS = {"PAN": r"^[A-Z]{5}[0-9]{4}[A-Z]$", "Passport": r"^[A-Z][0-9]{7}$"}


@tool
def get_application() -> dict:
    """Return the onboarding application: form data, ID document and address proof."""
    return APPLICATION


@tool
def validate_id_format(id_type: str, number: str) -> str:
    """Validate the format of an ID number. id_type is PAN or Passport."""
    pat = ID_FORMATS.get(id_type)
    if not pat:
        return f"No format rule for {id_type}"
    return f"{id_type} {number}: {'VALID' if re.match(pat, number) else 'INVALID'} format"


@tool
def check_document_expiry(expiry: str) -> str:
    """Check whether a document (YYYY-MM-DD expiry) is still valid today."""
    days = (date.fromisoformat(expiry) - date.today()).days
    return f"Expired {abs(days)} days ago" if days < 0 else f"Valid, {days} days remaining"


@tool
def address_proof_recency(issue_date: str, max_age_days: int = 90) -> str:
    """Check the address proof was issued within max_age_days."""
    age = (date.today() - date.fromisoformat(issue_date)).days
    return f"Issued {age} days ago - {'OK' if age <= max_age_days else 'TOO OLD'} (limit {max_age_days})"


SYSTEM = (
    "You are a KYC analyst. Use the tools to verify the application. Check: ID format, ID expiry, name match "
    "between form and ID (allow middle-name/initial differences), DOB match, address match (allow spelling and "
    "abbreviation variants like Bangalore/Bengaluru), and address-proof recency. Output a checklist with "
    "PASS / FAIL / REVIEW per item and a final status: APPROVED, PENDING (list documents needed) or REJECTED."
)


def main():
    banner("10 - KYC Onboarding Verifier (LangChain agent)")
    tools = [get_application, validate_id_format, check_document_expiry, address_proof_recency]
    section("KYC result", run_agent(SYSTEM, tools, "Verify the current onboarding application."))


if __name__ == "__main__":
    main()
