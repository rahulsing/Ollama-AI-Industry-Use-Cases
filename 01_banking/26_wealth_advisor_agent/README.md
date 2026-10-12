# 26 · AI Wealth Advisor

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📈 Wealth & Investment Management

## 🏦 The business problem (new to banking? start here)

**In the business today:** Wealth advisers understand a client's goals (education, retirement, a home), assess their risk tolerance, recommend a portfolio and document why it is suitable.

**Who does this work:** Financial advisers / relationship managers, checked by compliance.

**Why it's hard:** Good advice is personal and time-consuming, so it is usually only available to wealthier clients.

### Key terms
- **Wealth management**: Advice and investment services for individuals, from mass affluent to private banking clients.
- **Asset allocation**: How a portfolio is split between asset classes (equity, bonds, gold, cash). The biggest driver of risk and return.
- **Risk profile**: How much investment risk a client is willing and able to take, usually from a questionnaire.
- **Suitability**: The rule that a recommended product must fit the client's risk profile, knowledge, goals and time horizon.
- **SIP**: Systematic Investment Plan: investing a fixed amount every month into a fund.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Builds a goals-based investment plan for a client with suitability checks.

### How it works
Client Profiler, Portfolio Strategist and Compliance Reviewer agents collaborate to produce a personalised plan.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/26_wealth_advisor_agent/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
