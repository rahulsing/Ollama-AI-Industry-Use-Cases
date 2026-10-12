# 45 · FX Hedging Advisor

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 💱 Treasury, Payments & Operations

## 🏦 The business problem (new to banking? start here)

**In the business today:** Companies that buy or sell abroad face currency risk. Bank FX sales teams help them measure it and lock in rates with forwards or options.

**Who does this work:** FX sales / treasury advisers for corporate clients.

**Why it's hard:** Clients need clear explanations of risk in their own currency, and advice must be about protection, not speculation.

### Key terms
- **FX exposure / hedging**: Risk that currency moves change the home-currency value of foreign receipts or payments; hedging locks in a rate.
- **FX forward**: A contract to exchange currency at a fixed rate on a future date. Removes uncertainty for a known cash flow.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Measures a corporate's FX exposure and suggests a hedging approach.

### How it works
Agent uses `net_exposure` and `forward_rate` tools and compares forward vs. unhedged outcomes.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/45_fx_hedging_advisor/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
