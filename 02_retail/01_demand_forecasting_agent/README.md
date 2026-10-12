# 01 · Demand Forecasting & Replenishment Agent

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🛒 Retail · **Category:** 📦 Supply Chain & Inventory

## 🛒 The business problem (new to retail? start here)

**In the business today:** Every week, replenishment analysts decide how much of each product to order from suppliers, based on recent sales, trends and upcoming promotions.

**Who does this work:** Replenishment / inventory analysts in the supply chain team.

**Why it's hard:** Large retailers manage tens of thousands of products. Seasonal products (sunscreen in summer, scarves in winter) change fast, and both empty shelves and overstock cost money.

### Key terms
- **Demand forecasting**: Predicting how many units will sell in future weeks, using past sales, trends, seasons and promotions.
- **Replenishment**: Re-ordering stock from suppliers so shelves don't run empty.
- **Lead time**: How long a supplier takes to deliver after an order is placed.
- **Weeks of cover**: How many weeks current stock will last at forecast sales.
- **Safety stock**: Extra stock held to protect against forecast errors and late deliveries.
- **Reorder point**: The stock level at which a new order must be placed to arrive before running out.
- **Stock-out**: When a product is unavailable: a lost sale and an unhappy customer.
- **Promotion uplift**: The extra sales a promotion generates over normal demand.

More terms: [Retail Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Forecasts weekly demand per product and recommends what to reorder, flagging stock-out risks.

### How it works
Tools compute trend-based forecasts with promotion uplift, weeks of cover, safety stock and order quantities in full cases; the agent explains priorities and actions for slow sellers.

## Run
```bash
# from the repo root, with Ollama running
python 02_retail/01_demand_forecasting_agent/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Retail use cases](../README.md#-use-cases) · [All industries](../../README.md)
