# 41 · SWIFT Payment Repair Assistant

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Chain-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 💱 Treasury, Payments & Operations

## 🏦 The business problem (new to banking? start here)

**In the business today:** International payments travel as SWIFT messages. If a field is wrong (bad BIC, invalid IBAN), the payment fails automatic processing and someone must repair it by hand.

**Who does this work:** Payments operations teams.

**Why it's hard:** Manual repairs are slow and costly, and some repairs need customer confirmation.

### Key terms
- **SWIFT / MT103**: SWIFT is the network banks use for international payments; MT103 is the message format for a customer transfer.
- **STP (Straight-Through Processing)**: A payment that is processed end-to-end with no manual intervention. Failures need costly manual repair.
- **BIC / IBAN / IFSC**: Bank and account identifiers: BIC (bank code, 8 or 11 characters), IBAN (international account number with a checksum), IFSC (Indian branch code).
- **Charges code (OUR/SHA/BEN)**: Who pays the transfer fees: OUR = sender, SHA = shared, BEN = beneficiary.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Validates MT103 payment messages and suggests repairs for failed STP.

### How it works
Python parses fields and validates BIC/IBAN/amount format; the LLM explains failures and proposes repairs.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/41_swift_payment_validator/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
