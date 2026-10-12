# 02 · Loan Underwriting Assistant

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏦 Credit & Lending

## 🏦 The business problem (new to banking? start here)

**In the business today:** Mortgage underwriters check every application against a rulebook: can the borrower afford the payments, is the deposit big enough, is their job stable? They then approve, decline or approve with conditions.

**Who does this work:** Mortgage underwriters (Retail Lending).

**Why it's hard:** Rules are detailed and easy to misapply under time pressure; every decision must be traceable to a rule.

### Key terms
- **Underwriting**: Checking a loan application against the bank's rules and deciding whether to lend, how much and at what price.
- **DTI (Debt-to-Income)**: Monthly debt payments divided by monthly income. A DTI of 40% means 40% of income already goes to repayments.
- **LTV (Loan-to-Value)**: Loan amount divided by the value of the property. 80% LTV means a 20% deposit; higher LTV means less cushion if prices fall.
- **Credit score / bureau score**: A number (e.g. 300-900) from a credit bureau summarising a person's repayment history. Higher means lower risk.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Underwriter copilot that checks DTI, LTV and policy rules through tools before recommending a decision.

### How it works
A LangChain agent calls `calculate_dti`, `calculate_ltv` and `check_policy` tools against the application and explains which rules pass or fail.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/02_loan_underwriting_assistant/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
