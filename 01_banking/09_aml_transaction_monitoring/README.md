# 09 · AML Transaction Monitoring Agent

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🕵️ Financial Crime & Compliance

## 🏦 The business problem (new to banking? start here)

**In the business today:** Banks must monitor transactions for money laundering. Rules generate alerts (e.g. repeated cash deposits just under the reporting limit); investigators review each alert and decide whether to report it.

**Who does this work:** AML transaction monitoring analysts and the MLRO (Compliance / Financial Crime).

**Why it's hard:** Most alerts are false positives, yet missing a real case can bring huge fines. Investigation is slow and manual.

### Key terms
- **AML (Anti-Money Laundering)**: Laws and controls that stop criminals disguising illegal money as legitimate. Banks must monitor and report suspicious activity.
- **Money laundering stages**: Placement (getting cash into the system), layering (moving it to hide the trail), integration (using it as 'clean' money).
- **Structuring (smurfing)**: Splitting cash deposits into amounts just under a reporting threshold to avoid triggering a report. Itself an offence.
- **CTR (Currency Transaction Report)**: A report banks file for large cash transactions (e.g. 10,000 or more).
- **SAR / STR**: Suspicious Activity (or Transaction) Report: what a bank files with the financial intelligence unit when it suspects money laundering.
- **MLRO**: Money Laundering Reporting Officer: the senior person accountable for deciding whether to file SARs.
- **False positive**: An alert that turns out to be innocent, e.g. a name that looks like a sanctioned person but is someone else. Usually most alerts are false positives.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Detects structuring, rapid movement and high-risk-geography patterns and triages the alert.

### How it works
Python rules raise alerts; an AML Investigator agent reviews the evidence and a Compliance Officer agent decides close / escalate / file SAR.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/09_aml_transaction_monitoring/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
