# 46 · Invoice & Cheque Data Extractor

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Structured%20extraction-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 💱 Treasury, Payments & Operations

## 🏦 The business problem (new to banking? start here)

**In the business today:** Banks and their business clients process piles of invoices and cheques, reading the details and checking them before paying or clearing.

**Who does this work:** Payments / clearing operations, trade and accounts-payable teams.

**Why it's hard:** Manual keying is slow, and mismatched amounts are a common source of errors and fraud.

### Key terms
- **Cheque truncation / OCR**: Processing cheques from scanned images; OCR reads the printed and handwritten fields.
- **BIC / IBAN / IFSC**: Bank and account identifiers: BIC (bank code, 8 or 11 characters), IBAN (international account number with a checksum), IFSC (Indian branch code).
- **GSTIN**: India's 15-character Goods and Services Tax identification number for a business.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Extracts fields from invoices and cheques (OCR text) and validates them.

### How it works
Pydantic schema extraction with Python validation (amount-in-words vs. figures, dates, IFSC).

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/46_invoice_cheque_extractor/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
