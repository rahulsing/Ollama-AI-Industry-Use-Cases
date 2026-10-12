"""SWIFT Payment Repair Assistant — Python validation + LangChain chain.

Run:  python 01_banking/41_swift_payment_validator/app.py
"""

import json
import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, run_chain, section

MT103 = """{1:F01BANKGB2LAXXX0000000000}{2:I103DEUTDEFFXXXXN}{4:
:20:REF20261012-001
:23B:CRED
:32A:261012EUR15000,5
:50K:/GB29NWBK60161331926819
ACME TRADING LTD
1 HIGH STREET LONDON
:59:/DE89370400440532013001
MULLER MASCHINENBAU GMBH
:57A:DEUTDEFFX
:70:INVOICE 4471 MACHINE PARTS
:71A:SHAR
-}"""


def iban_valid(iban: str) -> bool:
    s = iban[4:] + iban[:4]
    digits = "".join(str(int(c, 36)) for c in s)
    return int(digits) % 97 == 1


def validate(msg: str) -> dict:
    fields = dict(re.findall(r":(\d{2}[A-Z]?):([^:]*?)(?=\n:|\n-})", msg, re.S))
    issues = []
    for tag in ["20", "23B", "32A", "50K", "59", "71A"]:
        if tag not in fields:
            issues.append(f"Mandatory field :{tag}: missing")
    m = re.match(r"(\d{6})([A-Z]{3})([\d,]+)$", fields.get("32A", "").strip())
    if not m:
        issues.append(":32A: format must be YYMMDD + CCY + amount")
    elif m.group(2) == "EUR" and len(m.group(3).split(",")[-1]) > 2:
        issues.append(f":32A: amount {m.group(3)} has more than 2 decimals")
    if bic := fields.get("57A", "").strip():
        if not re.fullmatch(r"[A-Z]{6}[A-Z0-9]{2}([A-Z0-9]{3})?", bic):
            issues.append(f":57A: BIC '{bic}' must be 8 or 11 characters (got {len(bic)})")
    for tag in ["50K", "59"]:
        acct = fields.get(tag, "").strip().splitlines()[0].lstrip("/") if tag in fields else ""
        if acct and not iban_valid(acct):
            issues.append(f":{tag}: IBAN {acct} fails checksum")
    if fields.get("71A", "").strip() not in {"OUR", "SHA", "BEN"}:
        issues.append(f":71A: charges code '{fields.get('71A', '').strip()}' invalid (OUR/SHA/BEN)")
    return {"fields": {k: v.strip() for k, v in fields.items()}, "issues": issues}


SYSTEM = (
    "You are a payments operations specialist. For each validation issue explain why the MT103 would fail STP and "
    "propose the exact corrected field value. Only obvious typos are safe to repair without the customer "
    "(e.g. 'SHAR' -> 'SHA', a BIC with one stray character). Never change who bears charges, amounts, accounts or "
    "IBANs: mark those 'Needs customer confirmation'. Finish with the repaired field list."
)


def main():
    banner("41 - SWIFT Payment Repair Assistant (LangChain)")
    v = validate(MT103)
    section("Validation", json.dumps(v, indent=2))
    if v["issues"]:
        section("Repair suggestions", run_chain(SYSTEM, "Message:\n{msg}\n\nIssues:\n{issues}", msg=MT103, issues="\n".join(v["issues"])))


if __name__ == "__main__":
    main()
