# 32 · Suitability & Mis-selling Checker

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Structured%20extraction-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📈 Wealth & Investment Management

## 🏦 The business problem (new to banking? start here)

**In the business today:** Before a product is sold, a check confirms it suits the client's risk profile, knowledge, time horizon and need for cash.

**Who does this work:** Sales supervisors and compliance / conduct teams.

**Why it's hard:** Mis-selling (especially to elderly or vulnerable customers) leads to compensation and fines.

### Key terms
- **Suitability**: The rule that a recommended product must fit the client's risk profile, knowledge, goals and time horizon.
- **Mis-selling**: Selling a product that is unsuitable or not properly explained. Leads to compensation and regulatory fines.
- **Vulnerable customer**: Someone more likely to suffer harm (e.g. due to age, illness, bereavement). Banks must take extra care with them.
- **Risk profile**: How much investment risk a client is willing and able to take, usually from a questionnaire.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Checks whether a recommended product is suitable for a client's profile before sale.

### How it works
Rules compare product risk vs. client risk, horizon and concentration; LLM returns a structured suitability verdict.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/32_suitability_checker/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
