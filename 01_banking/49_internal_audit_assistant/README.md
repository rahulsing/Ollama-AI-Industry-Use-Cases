# 49 · Internal Audit Assistant

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏢 Enterprise Analytics & Audit

## 🏦 The business problem (new to banking? start here)

**In the business today:** Internal auditors test samples of transactions to check controls worked, e.g. that a different person approved each payment within their authority.

**Who does this work:** Internal audit.

**Why it's hard:** Testing and report writing are labour-intensive; findings must follow a strict format for the audit committee.

### Key terms
- **Internal audit**: The independent team that tests whether the bank's controls work and reports to the board's audit committee.
- **Maker-checker**: A control where one person enters a transaction and a different person approves it (segregation of duties).

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Tests a sample of transactions against controls and drafts audit findings.

### How it works
Python runs control tests (maker-checker, limits, SoD); Auditor and Audit Manager agents write findings with risk ratings.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/49_internal_audit_assistant/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
