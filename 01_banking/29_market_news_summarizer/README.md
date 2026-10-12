# 29 · Market News Briefing for RMs

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📈 Wealth & Investment Management

## 🏦 The business problem (new to banking? start here)

**In the business today:** Every morning, relationship managers need to know what happened in markets and which of their clients are affected, so they can call them proactively.

**Who does this work:** Relationship managers, investment strategists.

**Why it's hard:** News volume is huge; linking it to each client's holdings by hand is impossible at scale.

### Key terms
- **Relationship Manager (RM)**: The banker who owns a client relationship and is their main point of contact.
- **Asset allocation**: How a portfolio is split between asset classes (equity, bonds, gold, cash). The biggest driver of risk and return.
- **Guidance**: Management's forecast of future results. Investors watch closely for upgrades, downgrades or softer wording.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Summarises market news and maps it to client holdings for relationship managers.

### How it works
Market Analyst agent summarises themes; RM Briefing agent links them to each client's portfolio with talking points.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/29_market_news_summarizer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
