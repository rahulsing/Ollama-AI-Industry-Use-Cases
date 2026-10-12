# 35 · Personal Finance Coach

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Chain-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🙋 Retail Banking & Customer Experience

## 🏦 The business problem (new to banking? start here)

**In the business today:** Banks increasingly help customers manage money, analysing spending and suggesting budgets and savings inside the banking app.

**Who does this work:** Digital banking / customer engagement teams.

**Why it's hard:** Customers want personal, practical advice, not generic tips.

### Key terms
- **50/30/20 rule**: A budgeting rule: 50% of income on needs, 30% on wants, 20% on savings.
- **Retail banking**: Banking for individuals: accounts, cards, loans, mortgages and savings.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Analyses spending and gives personalised saving tips and a budget.

### How it works
Transactions are categorised and summarised in Python; the LLM coaches against the 50/30/20 rule.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/35_personal_finance_coach/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
