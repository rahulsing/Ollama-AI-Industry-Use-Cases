# 48 · Earnings Call Analyzer

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏢 Enterprise Analytics & Audit

## 🏦 The business problem (new to banking? start here)

**In the business today:** After quarterly results, management hold an earnings call. Analysts and investors listen for changes in outlook and signs of trouble.

**Who does this work:** Equity research, investor relations and credit analysts.

**Why it's hard:** Calls are long and the important signals are often subtle changes in wording.

### Key terms
- **Guidance**: Management's forecast of future results. Investors watch closely for upgrades, downgrades or softer wording.
- **NIM (Net Interest Margin)**: A bank's interest income minus interest paid, as a % of assets. The core measure of lending profitability.
- **Delinquency / NPA / NPL**: A delinquent loan is behind on payments. After about 90 DPD it becomes a Non-Performing Asset / Loan.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Extracts guidance, sentiment and risks from an earnings call transcript.

### How it works
Transcript Analyst agent extracts key points; Sentiment Analyst agent rates management tone and risks.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/48_earnings_call_analyzer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
