# 11 · Sanctions Screening Assistant

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Chain-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🕵️ Financial Crime & Compliance

## 🏦 The business problem (new to banking? start here)

**In the business today:** Every customer and international payment is screened against sanctions lists. A similar name triggers an alert that an analyst must clear or escalate before money moves.

**Who does this work:** Sanctions screening analysts (Financial Crime Compliance).

**Why it's hard:** Name matching produces many false positives that delay payments, while a missed true match is a serious legal breach.

### Key terms
- **Sanctions screening**: Checking customers and payments against government lists of banned people, companies and countries.
- **False positive**: An alert that turns out to be innocent, e.g. a name that looks like a sanctioned person but is someone else. Usually most alerts are false positives.
- **PEP**: Politically Exposed Person: someone with a prominent public role (or their family/associates). Higher bribery and corruption risk, so EDD is required.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Reduces false positives in name screening by adjudicating fuzzy matches with secondary identifiers.

### How it works
`difflib` fuzzy-matches against a watchlist; the LLM compares DOB, nationality and address to recommend true match / false positive.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/11_sanctions_screening_assistant/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
