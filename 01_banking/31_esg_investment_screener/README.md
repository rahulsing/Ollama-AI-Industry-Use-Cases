# 31 · ESG Investment Screener

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📈 Wealth & Investment Management

## 🏦 The business problem (new to banking? start here)

**In the business today:** More clients want investments that match their values, such as no tobacco or weapons and low carbon. Advisers screen funds and explain the trade-offs.

**Who does this work:** Investment advisers and ESG / product teams.

**Why it's hard:** ESG data is messy and greenwashing is a regulatory risk.

### Key terms
- **ESG**: Environmental, Social and Governance factors used to screen investments for sustainability.
- **Asset allocation**: How a portfolio is split between asset classes (equity, bonds, gold, cash). The biggest driver of risk and return.
- **Suitability**: The rule that a recommended product must fit the client's risk profile, knowledge, goals and time horizon.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Screens a fund universe against ESG preferences and exclusions.

### How it works
Python applies exclusions and score thresholds; ESG Analyst and Advisor agents explain trade-offs and shortlist funds.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/31_esg_investment_screener/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
