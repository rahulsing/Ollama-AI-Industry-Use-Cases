# 28 · Investor Risk Profiling Agent

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Chain-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📈 Wealth & Investment Management

## 🏦 The business problem (new to banking? start here)

**In the business today:** Before giving investment advice, banks must assess a client's risk profile, usually through a questionnaire, and explain the result to the client.

**Who does this work:** Advisers / RMs.

**Why it's hard:** Answers are often contradictory (e.g. wants high growth but cannot tolerate losses), and these need a conversation.

### Key terms
- **Risk profile**: How much investment risk a client is willing and able to take, usually from a questionnaire.
- **Suitability**: The rule that a recommended product must fit the client's risk profile, knowledge, goals and time horizon.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Scores a risk questionnaire and explains the resulting risk profile to the client.

### How it works
Questionnaire answers are scored in Python; the LLM writes a profile summary and flags inconsistencies.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/28_risk_profiling_agent/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
