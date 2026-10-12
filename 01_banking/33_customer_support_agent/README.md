# 33 · Banking Customer Support Agent

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🙋 Retail Banking & Customer Experience

## 🏦 The business problem (new to banking? start here)

**In the business today:** Contact centres handle millions of simple requests: balances, recent transactions, blocking a lost card, branch hours.

**Who does this work:** Contact centre / customer service.

**Why it's hard:** Simple requests clog queues; customers want 24/7 instant help, done securely.

### Key terms
- **Retail banking**: Banking for individuals: accounts, cards, loans, mortgages and savings.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Answers balance, transaction and card questions and can block a lost card.

### How it works
Agent uses `get_balance`, `recent_transactions`, `block_card` and `branch_hours` tools over a mock core-banking API.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/33_customer_support_agent/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
