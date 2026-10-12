# 14 · Trade-Based Money Laundering Detector

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🕵️ Financial Crime & Compliance

## 🏦 The business problem (new to banking? start here)

**In the business today:** Trade finance teams check that goods, prices and shipping routes make commercial sense, because criminals use fake trade invoices to move money across borders.

**Who does this work:** Trade finance operations and financial crime specialists.

**Why it's hard:** Requires knowing what goods normally cost and how they normally ship; red flags are subtle.

### Key terms
- **TBML (Trade-Based Money Laundering)**: Disguising criminal money as trade, e.g. invoicing goods at fake prices to move value across borders.
- **Trade finance**: Bank services that help importers and exporters trade safely, e.g. Letters of Credit and guarantees.
- **Letter of Credit (LC)**: A bank's promise to pay an exporter if they present documents that exactly match the LC's terms.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Flags over/under-invoicing and suspicious trade routes in trade finance transactions.

### How it works
Python compares unit prices to benchmarks; a Trade Finance Analyst and a TBML Specialist agent assess red flags.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/14_tbml_detector/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
