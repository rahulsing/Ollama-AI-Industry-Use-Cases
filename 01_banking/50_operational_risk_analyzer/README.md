# 50 · Operational Risk Incident Analyzer

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Structured%20extraction-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏢 Enterprise Analytics & Audit

## 🏦 The business problem (new to banking? start here)

**In the business today:** Every operational loss or near miss (an IT outage, a keying error, a forged signature) is logged, classified and analysed to prevent repeats.

**Who does this work:** Operational risk teams (Risk department).

**Why it's hard:** Inconsistent classification makes loss data unreliable for reporting and capital calculations.

### Key terms
- **Operational risk**: Losses from failed processes, people, systems or external events, e.g. IT outages, errors, fraud, floods.
- **Basel event types**: The 7 standard categories of operational loss (internal fraud, external fraud, system failures, process errors...).

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Classifies operational-loss incidents into Basel event types and suggests root cause and controls.

### How it works
Each incident is mapped to a structured schema (Basel event type, root cause, severity, control).

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/50_operational_risk_analyzer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
