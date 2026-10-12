# 43 · Reconciliation Exception Agent

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 💱 Treasury, Payments & Operations

## 🏦 The business problem (new to banking? start here)

**In the business today:** Operations teams match every entry in the bank's ledger against bank statements daily. Anything that does not match (a 'break') must be investigated.

**Who does this work:** Reconciliation / operations teams.

**Why it's hard:** Breaks pile up quickly; unresolved ones can hide errors, fraud or losses.

### Key terms
- **Reconciliation**: Matching the bank's internal ledger against external statements to make sure every entry agrees. Mismatches are 'breaks'.
- **Nostro account**: An account a bank holds with another bank in a foreign currency, used to settle payments.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Matches ledger vs. bank statement entries and investigates the breaks.

### How it works
Python matches by amount/reference/date; a Recon Analyst agent classifies breaks and an Ops Lead agent assigns actions.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/43_reconciliation_exception_agent/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
