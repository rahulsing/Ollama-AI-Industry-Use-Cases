# 12 · SAR Narrative Generator

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🕵️ Financial Crime & Compliance

## 🏦 The business problem (new to banking? start here)

**In the business today:** When an investigation concludes activity is suspicious, the bank files a SAR with a written narrative explaining who, what, when, where and why.

**Who does this work:** AML investigators and the MLRO.

**Why it's hard:** Narratives must be precise, factual and complete; writing them takes hours per case.

### Key terms
- **SAR / STR**: Suspicious Activity (or Transaction) Report: what a bank files with the financial intelligence unit when it suspects money laundering.
- **MLRO**: Money Laundering Reporting Officer: the senior person accountable for deciding whether to file SARs.
- **Typology**: A known pattern of financial crime, e.g. structuring, mule accounts or trade-based laundering.
- **Money mule**: A person whose account is used to receive and quickly pass on stolen money, often recruited with 'easy money' offers.
- **APP fraud**: Authorised Push Payment fraud: victims are tricked into sending money themselves, e.g. a fake investment.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Drafts a Suspicious Activity Report narrative (who, what, when, where, why) from case facts.

### How it works
A Case Analyst agent builds the timeline and a SAR Writer agent produces the regulator-ready narrative.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/12_sar_narrative_generator/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
