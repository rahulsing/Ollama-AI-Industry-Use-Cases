# 44 · Letter of Credit Document Checker

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 💱 Treasury, Payments & Operations

## 🏦 The business problem (new to banking? start here)

**In the business today:** Under a Letter of Credit, the bank pays the exporter only if their documents exactly match the LC terms. Checkers examine every document line by line.

**Who does this work:** Trade finance document checkers and trade operations managers.

**Why it's hard:** Checking is meticulous manual work; missing a discrepancy means paying when the bank should not.

### Key terms
- **Letter of Credit (LC)**: A bank's promise to pay an exporter if they present documents that exactly match the LC's terms.
- **UCP 600**: The international rules (from the ICC) that govern how Letters of Credit work and how documents are checked.
- **Discrepancy**: A mismatch between presented documents and LC terms. Any discrepancy lets the bank refuse to pay.
- **Bill of Lading (B/L)**: The shipping document issued by the carrier: a receipt for goods and proof of shipment. A 'clean' B/L has no damage notes.
- **Incoterms (e.g. CIF)**: Standard trade terms defining who pays for shipping and insurance. CIF = seller pays Cost, Insurance and Freight.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Checks LC presentation documents for discrepancies against UCP 600 terms.

### How it works
Python compares invoice, bill of lading and LC fields; Document Checker and Trade Ops agents classify discrepancies.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/44_trade_finance_lc_checker/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
