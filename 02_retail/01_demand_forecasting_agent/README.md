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

```mermaid
flowchart LR
    QU["💬 Your question"] --> AG["🤖 LangChain agent<br/>decides which tool to call"]
    AG <-->|"🔧 calls & results"| T["🐍 Python tools<br/>list_products()<br/>forecast_demand()<br/>reorder_plan()"]
    IN["📄 Sales history + stock levels"] --> T
    AG <-.->|"💬 reasoning"| LLM(["🦙 Ollama"])
    AG --> OUT["📝 Reorder plan + stock-out risks"]
    OUT --> HU["🧑‍⚖️ Human review"]
    classDef data fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    classDef rules fill:#d1fae5,stroke:#059669,color:#064e3b
    classDef ai fill:#ede9fe,stroke:#7c3aed,color:#3b0764
    classDef llm fill:#1f2937,stroke:#111827,color:#ffffff
    classDef out fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef human fill:#f3f4f6,stroke:#6b7280,color:#111827
    class IN,QU data
    class T rules
    class AG ai
    class LLM llm
    class OUT out
    class HU human
```

<sub>🟦 data · 🟩 Python: maths & rules (auditable) · 🟪 AI: reasoning & writing · ⬛ local LLM · 🟨 result</sub>

## 💬 Sample conversation

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** Review all products: what should we reorder this week and why?

**🦙 Ollama:**

Based on the analysis of the products, here is the summary of the reorder plan and recommendations for this week:

| SKU | Product                | Weeks of Cover | Order Now? | Order Units | Stock-Out Risk | Demand Status                  |
|-----|------------------------|----------------|------------|-------------|----------------|--------------------------------|
| SKU-101 | Organic oat milk 1L    | 1.9            | No         | 0           | No             | Steady                         |
| SKU-102 | Sunscreen SPF50 200ml  | 1.0            | Yes        | 1224        | Yes            | Growing Demand (do not discount)|
| SKU-103 | Wool scarf (grey)      | 12+            | No         | 0           | No             | Slow Seller / Overstock (consider markdown or cancelling open orders) |

### Stock-Out Risks:
- **Sunscreen SPF50 200ml (SKU-102)**: There is a high risk of stock-out before delivery due to the low weeks of cover (1.0) and growing demand. Immediate action is needed to reorder to avoid stock-outs.

### Trends and Promotions:
- **Sunscreen SPF50 200ml (SKU-102)**: The product is experiencing growing demand, and there is a promotion next week. This indicates a positive trend, and it's important to ensure adequate stock to meet the increased demand.

### Slow Sellers:
- **Wool scarf (grey) (SKU-103)**: The product is a slow seller, with a high weeks of cover (12+). Consider markdowns or cancelling open orders to reduce inventory and free up space for faster-moving items.

### Recommendations:
- **Organic oat milk 1L (SKU-101)**: The product is steady, and there is no immediate need to reorder. Continue monitoring the trend.
- **Sunscreen SPF50 200ml (SKU-102)**: Reorder now to ensure there is enough stock to meet the growing demand and avoid stock-outs.
- **Wool scarf (grey) (SKU-103)**: Consider markdowns or cancelling open orders to reduce overstock and improve cash flow.

By taking these actions, you can optimize inventory levels and ensure that you meet customer demand while managing stock efficiently.


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
