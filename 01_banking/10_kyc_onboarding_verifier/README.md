# 10 · KYC Onboarding Verifier

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🕵️ Financial Crime & Compliance

## 🏦 The business problem (new to banking? start here)

**In the business today:** Before opening an account, the bank must verify identity and address documents and check they match the application.

**Who does this work:** KYC / onboarding operations teams.

**Why it's hard:** Checks are repetitive; small mismatches (spelling, expired IDs) are easy to miss and delay customers.

### Key terms
- **KYC (Know Your Customer)**: Verifying who a customer is (ID, address) and understanding what they do, before and during the relationship.
- **CDD / EDD**: Customer Due Diligence (standard checks) and Enhanced Due Diligence (deeper checks for high-risk customers, such as source of wealth).

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Checks customer onboarding data for completeness, document validity and consistency.

### How it works
Agent uses `check_document_expiry`, `validate_id_format` and `compare_fields` tools and returns a KYC checklist with pass/fail.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/10_kyc_onboarding_verifier/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
