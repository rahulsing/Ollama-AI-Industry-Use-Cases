# 47 · Financial Statement Analyzer

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏢 Enterprise Analytics & Audit

## 🏦 The business problem (new to banking? start here)

**In the business today:** Before lending to or investing in a company, analysts study its financial statements to judge profitability, debt and cash generation.

**Who does this work:** Credit analysts and equity / credit research analysts.

**Why it's hard:** Headline growth can hide weak cash flow or rising debt; spotting this takes careful ratio analysis.

### Key terms
- **Financial statements**: Income statement (profit), balance sheet (what is owned and owed) and cash flow statement.
- **EBITDA / EBIT**: Earnings before interest, tax, depreciation and amortisation (EBITDA), or before interest and tax (EBIT): a measure of operating profit.
- **Margins**: Profit as a % of revenue (gross, operating, net). Falling margins signal pricing pressure or rising costs.
- **Leverage (debt-to-equity)**: How much a company relies on borrowing. Higher leverage means higher risk if earnings fall.
- **Liquidity ratios (current ratio)**: Current assets / current liabilities: can the company pay its bills due within a year?
- **Free cash flow**: Operating cash flow minus capital expenditure: the cash really available to repay debt or pay dividends.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Analyses a company's income statement and balance sheet and writes an equity-style summary.

### How it works
Ratios and YoY growth computed in Python; Financial Analyst and Report Writer agents interpret them.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/47_financial_statement_analyzer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
