# 42 · Corporate Cash Flow Forecaster

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 💱 Treasury, Payments & Operations

## 🏦 The business problem (new to banking? start here)

**In the business today:** Corporate bankers help business clients forecast cash for the coming weeks to spot shortfalls and arrange funding in time.

**Who does this work:** Corporate relationship managers and transaction banking / treasury advisers.

**Why it's hard:** Running out of cash, even for a week, can sink a profitable business.

### Key terms
- **Cash flow forecasting**: Projecting future cash in and out (often 13 weeks) so a company can plan funding.
- **Working capital**: Money tied up in day-to-day operations (stock, receivables minus payables). Banks fund it with overdrafts and credit lines.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Forecasts a corporate client's 13-week cash position and highlights funding gaps.

### How it works
Agent uses `forecast_cash` and `funding_gap` tools on historical inflows/outflows.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/42_cash_flow_forecaster/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
