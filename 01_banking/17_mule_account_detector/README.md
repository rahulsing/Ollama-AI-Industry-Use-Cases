# 17 · Money Mule Account Detector

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🕵️ Financial Crime & Compliance

## 🏦 The business problem (new to banking? start here)

**In the business today:** Fraudsters use 'mule' accounts to receive stolen money and pass it on quickly. Banks look for accounts where money comes in from many people and leaves almost immediately.

**Who does this work:** Fraud and financial crime teams.

**Why it's hard:** Mules are often young people being exploited, so action must stop the fraud and also protect them.

### Key terms
- **Money mule**: A person whose account is used to receive and quickly pass on stolen money, often recruited with 'easy money' offers.
- **APP fraud**: Authorised Push Payment fraud: victims are tricked into sending money themselves, e.g. a fake investment.
- **Typology**: A known pattern of financial crime, e.g. structuring, mule accounts or trade-based laundering.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Identifies likely mule accounts from pass-through behaviour and new-account signals.

### How it works
Python computes pass-through ratio, account age and counterparties; Fraud Analyst and Investigator agents rank and recommend actions.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/17_mule_account_detector/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
