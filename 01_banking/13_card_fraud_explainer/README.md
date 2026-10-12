# 13 · Card Fraud Detection Explainer

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Chain-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🕵️ Financial Crime & Compliance

## 🏦 The business problem (new to banking? start here)

**In the business today:** Card transactions are scored for fraud in real time. Suspicious ones are blocked or held, and the customer is asked to confirm.

**Who does this work:** Fraud operations analysts.

**Why it's hard:** Blocking genuine spending annoys customers; letting fraud through costs money. Analysts need to see why a transaction was flagged.

### Key terms
- **Card fraud / CNP**: Unauthorised card use. Card-Not-Present (online/phone) fraud is the most common type.
- **MCC**: Merchant Category Code: a 4-digit code describing what kind of business a card merchant is, e.g. 5411 grocery, 7995 gambling.
- **False positive**: An alert that turns out to be innocent, e.g. a name that looks like a sanctioned person but is someone else. Usually most alerts are false positives.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Scores card transactions for fraud and explains each alert for analysts and customers.

### How it works
Feature-based risk score (velocity, geo-jump, MCC, amount z-score) plus an LLM explanation and suggested action.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/13_card_fraud_explainer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
