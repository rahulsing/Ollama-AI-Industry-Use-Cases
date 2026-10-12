# 04 · Credit Card Limit Optimizer

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Chain-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏦 Credit & Lending

## 🏦 The business problem (new to banking? start here)

**In the business today:** Card issuers regularly review limits: raise them for good customers who need more room, and reduce them for customers showing signs of stress, to manage risk.

**Who does this work:** Card portfolio managers (Cards / Unsecured Lending).

**Why it's hard:** Limit changes affect revenue, risk and customer trust. Each one needs a clear reason, especially a decrease.

### Key terms
- **Credit limit / utilisation**: The maximum a customer can borrow on a card or line, and how much of it they are using (balance / limit).
- **Credit score / bureau score**: A number (e.g. 300-900) from a credit bureau summarising a person's repayment history. Higher means lower risk.
- **Credit risk**: The risk that a borrower does not pay back what they owe. Managing it is the core skill of any lender.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Recommends credit-limit increases or decreases per card holder with an explainable reason.

### How it works
Rule-based eligibility and utilisation bands feed an LLM chain that produces a recommended limit and customer-friendly explanation.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/04_credit_limit_optimizer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
