"""Regulatory Change Impact Analyzer — CrewAI + Ollama.

Run:  python 01_banking/21_regulatory_change_tracker/app.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

CIRCULAR = """
CIRCULAR 2026/14 - Strengthening Digital Lending and Customer Protection (fictional, for demo)
1. Regulated entities shall provide a Key Fact Statement (KFS) with the all-in annual percentage rate (APR)
   to every digital loan applicant before contract execution.
2. Loan disbursements and repayments shall flow only between the borrower's account and the lender's account;
   no pass-through via third-party lending service provider (LSP) accounts.
3. A cooling-off period of at least 3 days shall be given during which the borrower may exit by repaying principal
   and proportionate APR without penalty.
4. Each lender shall appoint a nodal grievance redressal officer for digital lending; complaints not resolved in
   30 days may be escalated to the Ombudsman.
5. Lenders shall report all digital lending apps (DLAs) used, including those of LSPs, to the regulator quarterly.
Effective date: 1 April 2027.
"""

PROCESS_INVENTORY = """
- Retail Lending (personal loans via mobile app, partner LSP 'QuickCred' collects EMIs into its escrow)
- Loan Origination System (generates sanction letter; no APR shown, shows flat interest rate)
- Customer Service (complaint SLA currently 45 days)
- Compliance (quarterly regulatory returns; no DLA register exists)
- Product team (no cooling-off feature; prepayment penalty 3%)
"""


def main():
    banner("21 - Regulatory Change Impact Analyzer (CrewAI)")
    reg = make_agent("Regulatory Analyst", "Extract each obligation precisely from a regulatory circular",
                     "You turn legal text into clear, atomic, testable obligations.")
    impact = make_agent("Compliance Impact Assessor", "Map obligations to bank processes and identify gaps",
                        "You run regulatory change programmes and assign owners, actions and deadlines.")
    t1 = make_task("Circular:\n{circular}\n\nExtract obligations.",
                   "Numbered obligations with ID, requirement, effective date.", reg)
    t2 = make_task("Bank process inventory:\n{inventory}\n\nMap each obligation to impacted processes.",
                   "Gap table: Obligation | Impacted unit | Current state | Gap | Action | Owner | Priority (H/M/L); "
                   "then a 5-line executive summary.", impact, context=[t1])
    section("Impact assessment", run_crew([reg, impact], [t1, t2], {"circular": CIRCULAR, "inventory": PROCESS_INVENTORY}))


if __name__ == "__main__":
    main()
