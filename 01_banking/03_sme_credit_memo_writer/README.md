# 03 · SME Credit Memo Writer

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏦 Credit & Lending

## 🏦 The business problem (new to banking? start here)

**In the business today:** Before lending to a small or mid-sized business, a relationship manager and credit analyst write a 'credit memo': who the business is, how it is performing, whether it can repay, and what protections the bank will take.

**Who does this work:** Corporate/SME relationship managers and credit analysts.

**Why it's hard:** Writing a memo takes days of spreadsheet work and drafting; analysts spend more time writing than analysing.

### Key terms
- **Credit memo**: The written paper a credit committee reads before approving a business loan: who the borrower is, the numbers, risks and recommendation.
- **DSCR (Debt Service Coverage Ratio)**: Cash profit (EBITDA) divided by loan repayments due. Below 1.0x the business cannot cover its debt from operations.
- **EBITDA / EBIT**: Earnings before interest, tax, depreciation and amortisation (EBITDA), or before interest and tax (EBIT): a measure of operating profit.
- **Leverage (debt-to-equity)**: How much a company relies on borrowing. Higher leverage means higher risk if earnings fall.
- **Covenant**: A promise in a loan agreement, e.g. 'keep debt below 3x EBITDA'. Breaking it lets the bank act early.
- **Collateral**: An asset the bank can take if the loan is not repaid, e.g. property or stock.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Turns SME financials into a bank-style credit memo (business profile, ratios, risks, mitigants).

### How it works
Ratios (DSCR, current ratio, leverage, margins) are computed in Python; a Financial Analyst agent analyses them and a Credit Writer agent drafts the memo.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/03_sme_credit_memo_writer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
