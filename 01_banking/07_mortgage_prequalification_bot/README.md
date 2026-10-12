# 07 · Mortgage Pre-Qualification Bot

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏦 Credit & Lending

## 🏦 The business problem (new to banking? start here)

**In the business today:** Before a full mortgage application, customers want a quick answer to 'how much can I borrow?' so they know which homes to look at.

**Who does this work:** Mortgage advisers, branch staff and digital channels.

**Why it's hard:** Customers expect instant answers at any hour; staff time is better spent on serious applications.

### Key terms
- **Pre-qualification**: A quick, non-binding estimate of how much a customer could borrow, before a full application.
- **DTI (Debt-to-Income)**: Monthly debt payments divided by monthly income. A DTI of 40% means 40% of income already goes to repayments.
- **EMI**: Equated Monthly Instalment: the fixed monthly repayment on a loan, covering interest and principal.
- **LTV (Loan-to-Value)**: Loan amount divided by the value of the property. 80% LTV means a 20% deposit; higher LTV means less cushion if prices fall.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Conversational assistant that estimates how much a customer can borrow and the monthly EMI.

### How it works
Agent uses `max_affordable_loan` and `monthly_emi` tools and answers in plain language with assumptions stated.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/07_mortgage_prequalification_bot/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
