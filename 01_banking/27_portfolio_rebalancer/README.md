# 27 · Portfolio Rebalancing Agent

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📈 Wealth & Investment Management

## 🏦 The business problem (new to banking? start here)

**In the business today:** Markets move, so a client's portfolio drifts away from its agreed mix (e.g. too much in equities after a rally). Advisers rebalance by selling some winners and buying underweight assets, minding taxes.

**Who does this work:** Portfolio managers and advisers.

**Why it's hard:** Rebalancing too little lets risk creep up; doing it carelessly triggers unnecessary taxes and costs.

### Key terms
- **Rebalancing**: Buying and selling to bring a portfolio back to its target allocation after markets move it.
- **Asset allocation**: How a portfolio is split between asset classes (equity, bonds, gold, cash). The biggest driver of risk and return.
- **Capital gains tax**: Tax on profit from selling an investment. Often lower for long-term holdings, so trade timing matters.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Detects drift from target allocation and proposes tax-aware rebalancing trades.

### How it works
Agent uses `current_allocation` and `rebalance_trades` tools and explains each trade.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/27_portfolio_rebalancer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
