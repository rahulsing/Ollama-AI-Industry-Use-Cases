# 03 · Dynamic Pricing Advisor

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🛒 Retail · **Category:** 🏷️ Merchandising & Pricing

## 🛒 The business problem (new to retail? start here)

**In the business today:** Pricing teams regularly review prices against competitors and stock levels: raise prices where there is room, cut to clear overstock, and protect margin.

**Who does this work:** Pricing analysts and category managers.

**Why it's hard:** Every price change trades volume against margin, and customers notice price swings. Decisions must respect margin rules and be explainable.

### Key terms
- **Gross margin**: (Price - cost) / price. A 30% margin means 30p of every 1 of sales is left after paying for the product.
- **Price elasticity**: How much volume changes when price changes. Elasticity of -2 means a 1% price cut lifts volume about 2%.
- **Competitive price index**: Our price compared to competitors' average for the same product.
- **Markdown**: A permanent price cut, usually to clear excess or seasonal stock.
- **Category manager**: The person who owns a product category's range, pricing and profit.

More terms: [Retail Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Recommends price changes from competitor prices, stock levels and elasticity, within margin guardrails.

### How it works
Python proposes prices (30% margin floor, max 10% move) and estimates profit impact; a Pricing Analyst agent explains them and a Category Manager agent approves or adjusts and writes the pricing memo.

## Run
```bash
# from the repo root, with Ollama running
python 02_retail/03_dynamic_pricing_advisor/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Retail use cases](../README.md#-use-cases) · [All industries](../../README.md)
