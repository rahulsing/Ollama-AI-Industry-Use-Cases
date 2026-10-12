"""Invoice & Cheque Data Extractor — LangChain structured output + Ollama.

Input is OCR text (plug in Tesseract / a vision model upstream).

Run:  python 01_banking/46_invoice_cheque_extractor/app.py
"""

import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from pydantic import BaseModel, Field

from common import banner, run_structured, section

CHEQUE_OCR = """
STATE BANK OF INDIA   MG ROAD BRANCH   IFSC: SBIN0001234
                                                     Date: 1 2 1 0 2 0 2 6
Pay  RAVI KUMAR ENTERPRISES                                  or Bearer
Rupees  Forty Five Thousand Six Hundred Only                 Rs. 45,600/-
A/c No. 30012345678
                                             For SUNRISE TRADERS  (Authorised Signatory)
Cheque No. 004512
"""

INVOICE_OCR = """
TAX INVOICE  No: SRT/26-27/0193   Date: 05/10/2026
Seller: Sunrise Traders, GSTIN 27AAACS1234F1Z5
Buyer: Ravi Kumar Enterprises, GSTIN 27AABCR5678K1Z2
1. Steel brackets  200 x 150.00 = 30,000.00
2. Fasteners box    40 x 236.00 =  9,440.00
Taxable value 39,440.00   CGST 9% 3,549.60   SGST 9% 3,549.60
Invoice Total 46,539.20
"""


class Cheque(BaseModel):
    bank: str
    ifsc: str
    cheque_number: str
    date: str = Field(description="DD-MM-YYYY")
    payee: str
    amount_in_words: str
    amount_in_figures: float
    account_number: str


class Invoice(BaseModel):
    invoice_number: str
    date: str
    seller_gstin: str
    buyer_gstin: str
    taxable_value: float
    total_tax: float
    invoice_total: float


WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
         "eleven": 11, "twelve": 12, "fifteen": 15, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
         "seventy": 70, "eighty": 80, "ninety": 90}
SCALES = {"hundred": 100, "thousand": 1000, "lakh": 100_000, "crore": 10_000_000}


def words_to_number(text: str) -> int:
    total = cur = 0
    for w in re.findall(r"[a-z]+", text.lower()):
        if w in WORDS:
            cur += WORDS[w]
        elif w == "hundred":
            cur *= 100
        elif w in SCALES:
            total += cur * SCALES[w]
            cur = 0
    return total + cur


def main():
    banner("46 - Invoice & Cheque Data Extractor (LangChain structured output)")
    sys_prompt = "Extract fields exactly as printed. Remove spaces inside dates. Amounts as plain numbers."
    c = run_structured(sys_prompt, CHEQUE_OCR, Cheque)
    i = run_structured(sys_prompt, INVOICE_OCR, Invoice)
    section("Cheque", c.model_dump_json(indent=2))
    section("Invoice", i.model_dump_json(indent=2))

    checks = {
        "cheque_words_match_figures": words_to_number(c.amount_in_words) == round(c.amount_in_figures),
        "ifsc_format_valid": bool(re.fullmatch(r"[A-Z]{4}0[A-Z0-9]{6}", c.ifsc)),
        "gstin_format_valid": all(re.fullmatch(r"\d{2}[A-Z]{5}\d{4}[A-Z]\d[Z][A-Z0-9]", g) for g in (i.seller_gstin, i.buyer_gstin)),
        "invoice_total_adds_up": abs(i.taxable_value + i.total_tax - i.invoice_total) < 1,
        "cheque_vs_invoice_difference": round(i.invoice_total - c.amount_in_figures, 2),
    }
    section("Validation", checks)


if __name__ == "__main__":
    main()
