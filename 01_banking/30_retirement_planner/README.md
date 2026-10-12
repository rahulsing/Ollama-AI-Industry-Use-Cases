# 30 · Retirement Planning Assistant

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📈 Wealth & Investment Management

## 🏦 The business problem (new to banking? start here)

**In the business today:** Customers ask 'can I retire at 60?'. Advisers estimate the savings needed, project current savings forward and work out the gap.

**Who does this work:** Financial planners and digital advice tools.

**Why it's hard:** The maths (inflation, returns, years in retirement) is unfamiliar to most customers; clear what-ifs help them act.

### Key terms
- **Retirement corpus**: The total savings needed at retirement to fund living costs for the rest of one's life.
- **SIP**: Systematic Investment Plan: investing a fixed amount every month into a fund.
- **Asset allocation**: How a portfolio is split between asset classes (equity, bonds, gold, cash). The biggest driver of risk and return.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Projects a retirement corpus, gap and required monthly savings.

### How it works
Agent uses a `retirement_plan` tool (corpus needed, projection, gap, extra saving) and re-runs it for what-if questions.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/30_retirement_planner/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
