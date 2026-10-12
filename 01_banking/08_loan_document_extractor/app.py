"""Loan Document Extractor — LangChain structured output + Ollama.

Run:  python 01_banking/08_loan_document_extractor/app.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from pydantic import BaseModel, Field

from common import banner, run_structured, section

PAYSLIP = """
ACME TECHNOLOGIES LTD          PAYSLIP FOR THE MONTH OF AUGUST 2026
Employee Name: Rohan Mehta     Employee ID: E10442    Designation: Senior Engineer
Date of Joining: 14-Mar-2019   PAN: ABCPM1234K
Basic: 60,000   HRA: 24,000   Special Allowance: 21,000   Gross Earnings: 105,000
PF: 7,200  Professional Tax: 200  Income Tax: 12,600   Total Deductions: 20,000
NET PAY: 85,000   Paid to A/c XXXX4521 HDFC Bank
"""

STATEMENT = """
HDFC BANK - Statement of Account  A/c No: XXXX4521  Name: ROHAN MEHTA  Period: 01-Aug-2026 to 31-Aug-2026
Opening balance 142,300.55
01-Aug  SALARY ACME TECHNOLOGIES   CR 85,000.00
03-Aug  HOME LOAN EMI ICICI        DR 32,500.00
05-Aug  CREDIT CARD PAYMENT        DR 18,240.00
12-Aug  UPI-GROCERY                DR 6,410.00
20-Aug  SIP MUTUAL FUND            DR 10,000.00
28-Aug  ATM WITHDRAWAL             DR 5,000.00
Closing balance 155,150.55
"""


class Payslip(BaseModel):
    employee_name: str
    employer: str = Field(description="Company name printed in the payslip header, not the employee ID")
    month: str = Field(description="Pay month and year, e.g. 'August 2026'")
    gross_salary: float
    total_deductions: float
    net_pay: float
    date_of_joining: str = Field(description="As written on the payslip")


class BankStatement(BaseModel):
    account_holder: str
    period: str
    opening_balance: float
    closing_balance: float
    salary_credits: float = Field(description="Sum of salary credits")
    existing_emi_debits: float = Field(description="Sum of loan EMI debits only")


def main():
    banner("08 - Loan Document Extractor (LangChain structured output)")
    sys_prompt = "Extract the fields exactly from the document. Numbers as plain floats without commas."
    p = run_structured(sys_prompt, PAYSLIP, Payslip)
    s = run_structured(sys_prompt, STATEMENT, BankStatement)
    section("Payslip", p.model_dump_json(indent=2))
    section("Bank statement", s.model_dump_json(indent=2))

    checks = {
        "name_match": p.employee_name.lower() == s.account_holder.lower(),
        "salary_credit_matches_net_pay": abs(p.net_pay - s.salary_credits) < 1,
        "existing_emi_to_net_pay_pct": round(s.existing_emi_debits / p.net_pay * 100, 1),
    }
    section("Cross-document checks", checks)


if __name__ == "__main__":
    main()
