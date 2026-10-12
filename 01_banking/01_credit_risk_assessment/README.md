# 01 · Credit Risk Assessment Agent

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏦 Credit & Lending

## 🏦 The business problem (new to banking? start here)

**In the business today:** When someone applies for a personal loan, the bank must decide: will this person pay us back? Credit analysts look at income, existing debts, credit bureau history and the bank's lending policy, then a more senior approver signs off.

**Who does this work:** Retail credit analysts and credit approvers (Risk department).

**Why it's hard:** Thousands of applications arrive daily. Decisions must be fast, consistent and explainable to the customer and the regulator.

### Key terms
- **Credit risk**: The risk that a borrower does not pay back what they owe. Managing it is the core skill of any lender.
- **DTI (Debt-to-Income)**: Monthly debt payments divided by monthly income. A DTI of 40% means 40% of income already goes to repayments.
- **LTI (Loan-to-Income)**: Loan amount divided by annual income. Caps how big a loan is relative to what the borrower earns.
- **EMI**: Equated Monthly Instalment: the fixed monthly repayment on a loan, covering interest and principal.
- **Credit score / bureau score**: A number (e.g. 300-900) from a credit bureau summarising a person's repayment history. Higher means lower risk.
- **Risk grade**: An internal rating (A, B, C...) that groups borrowers by riskiness and drives approval and pricing.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Scores a retail loan applicant and writes a credit decision memo with risk grade and conditions.

### How it works
Python computes DTI, LTI, PD-style score and policy breaches; a Credit Analyst agent interprets the numbers and a Chief Risk Officer agent issues approve / decline / refer with rationale.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/01_credit_risk_assessment/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
