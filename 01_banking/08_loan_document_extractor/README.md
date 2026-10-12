# 08 · Loan Document Extractor

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Structured%20extraction-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏦 Credit & Lending

## 🏦 The business problem (new to banking? start here)

**In the business today:** Loan processors read payslips and bank statements to verify income and existing debts, and re-type the figures into the loan system.

**Who does this work:** Loan operations / processing teams.

**Why it's hard:** Manual data entry is slow and error-prone, and mismatches between documents can signal fraud.

### Key terms
- **Underwriting**: Checking a loan application against the bank's rules and deciding whether to lend, how much and at what price.
- **EMI**: Equated Monthly Instalment: the fixed monthly repayment on a loan, covering interest and principal.
- **DTI (Debt-to-Income)**: Monthly debt payments divided by monthly income. A DTI of 40% means 40% of income already goes to repayments.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Extracts structured fields from payslips and bank statements for loan processing.

### How it works
`with_structured_output` maps unstructured text into a Pydantic schema; Python cross-checks salary vs. statement credits.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/08_loan_document_extractor/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
