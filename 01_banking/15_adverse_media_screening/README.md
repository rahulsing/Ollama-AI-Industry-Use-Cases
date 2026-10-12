# 15 · Adverse Media Screening

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Structured%20extraction-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🕵️ Financial Crime & Compliance

## 🏦 The business problem (new to banking? start here)

**In the business today:** During onboarding and periodic reviews, banks search news for negative stories about customers (fraud, corruption, investigations).

**Who does this work:** KYC / Enhanced Due Diligence analysts.

**Why it's hard:** Searches return many irrelevant hits, including people who just share a name. Reading them all is time-consuming.

### Key terms
- **Adverse media**: Negative news linking a customer to crime (fraud, bribery, laundering). Checked during onboarding and reviews.
- **CDD / EDD**: Customer Due Diligence (standard checks) and Enhanced Due Diligence (deeper checks for high-risk customers, such as source of wealth).
- **KYC (Know Your Customer)**: Verifying who a customer is (ID, address) and understanding what they do, before and during the relationship.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Classifies news articles about a customer for financial-crime relevance and severity.

### How it works
Each article is classified into a Pydantic schema (relevant, category, severity, summary) and aggregated.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/15_adverse_media_screening/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
