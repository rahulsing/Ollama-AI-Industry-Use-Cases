# 37 · Customer Churn Retention Agent

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🙋 Retail Banking & Customer Experience

## 🏦 The business problem (new to banking? start here)

**In the business today:** Banks watch for customers about to leave (salary stops arriving, balances drop, complaints rise) and try to keep the valuable ones.

**Who does this work:** Customer analytics and retention / customer success teams.

**Why it's hard:** Winning back a customer after they leave is much harder than keeping them.

### Key terms
- **Churn / attrition**: Customers leaving the bank or moving their main banking elsewhere.
- **Retail banking**: Banking for individuals: accounts, cards, loans, mortgages and savings.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Identifies customers likely to leave and designs retention actions.

### How it works
Churn signals scored in Python; Retention Analyst and Customer Success agents propose save offers.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/37_churn_retention_agent/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
