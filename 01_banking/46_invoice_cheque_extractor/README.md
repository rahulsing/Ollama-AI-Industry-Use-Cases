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

```mermaid
flowchart LR
    IN["📄 OCR text of cheque & invoice"] --> EX["🧾 LangChain structured output<br/>text → Pydantic schema"]
    EX -->|"validated fields"| PY["🐍 Python<br/>Words vs. figures · dates · IFSC"]
    PY --> OUT["📝 Validated payment data"]
    EX <-.->|"💬"| LLM(["🦙 Ollama"])
    OUT --> HU["🧑‍⚖️ Human review"]
    classDef data fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    classDef rules fill:#d1fae5,stroke:#059669,color:#064e3b
    classDef ai fill:#ede9fe,stroke:#7c3aed,color:#3b0764
    classDef llm fill:#1f2937,stroke:#111827,color:#ffffff
    classDef out fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef human fill:#f3f4f6,stroke:#6b7280,color:#111827
    class IN data
    class PY rules
    class EX ai
    class LLM llm
    class OUT out
    class HU human
```

<sub>🟦 data · 🟩 Python: maths & rules (auditable) · 🟪 AI: reasoning & writing · ⬛ local LLM · 🟨 result</sub>

## 💬 Sample response

Real output from `qwen2.5:7b-instruct` running locally on a laptop. LLM wording changes from run to run; the numbers from
Python stay the same.

<details>
<summary><b>Show the full output</b></summary>

````text
--- Cheque ---
{
  "bank": "STATE BANK OF INDIA",
  "ifsc": "SBIN0001234",
  "cheque_number": "004512",
  "date": "12102026",
  "payee": "RAVI KUMAR ENTERPRISES",
  "amount_in_words": "Forty Five Thousand Six Hundred Only",
  "amount_in_figures": 45600.0,
  "account_number": "30012345678"
}


--- Invoice ---
{
  "invoice_number": "SRT/26-27/0193",
  "date": "05/10/2026",
  "seller_gstin": "27AAACS1234F1Z5",
  "buyer_gstin": "27AABCR5678K1Z2",
  "taxable_value": 39440.0,
  "total_tax": 7099.2,
  "invoice_total": 46539.2
}


--- Validation ---
{'cheque_words_match_figures': True, 'ifsc_format_valid': True, 'gstin_format_valid': True, 'invoice_total_adds_up': True, 'cheque_vs_invoice_difference': 939.2}
````

</details>

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
