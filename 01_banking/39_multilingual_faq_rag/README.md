# 39 · Multilingual Banking FAQ (RAG)

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-RAG-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🙋 Retail Banking & Customer Experience

## 🏦 The business problem (new to banking? start here)

**In the business today:** Customers ask the same product questions (fees, limits, PIN reset) in many languages.

**Who does this work:** Customer service and digital channels.

**Why it's hard:** Maintaining FAQs and staff in every language is expensive.

### Key terms
- **Retail banking**: Banking for individuals: accounts, cards, loans, mortgages and savings.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Answers product FAQs in the customer's language (e.g. Hindi, Spanish, French).

### How it works
Translates the question to English, retrieves matching FAQ content, and answers in the language the question was asked in.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/39_multilingual_faq_rag/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
