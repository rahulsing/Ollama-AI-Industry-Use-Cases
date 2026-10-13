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

```mermaid
flowchart LR
    IN["📄 Prices, competitors & stock"] --> PY["🐍 Python<br/>Guard-railed prices: 30% margin floor, max 10% move"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🧑‍💼 Pricing Analyst"]
        A2["👔 Category Manager"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Pricing memo"]
    OUT --> HU["🧑‍⚖️ Human review"]
    classDef data fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    classDef rules fill:#d1fae5,stroke:#059669,color:#064e3b
    classDef ai fill:#ede9fe,stroke:#7c3aed,color:#3b0764
    classDef llm fill:#1f2937,stroke:#111827,color:#ffffff
    classDef out fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef human fill:#f3f4f6,stroke:#6b7280,color:#111827
    class IN data
    class PY rules
    class A1,A2 ai
    class LLM llm
    class OUT out
    class HU human
```

<sub>🟦 data · 🟩 Python: maths & rules (auditable) · 🟪 AI: reasoning & writing · ⬛ local LLM · 🟨 result</sub>

## 💬 Sample conversation

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** Should we change prices on our earbuds, water bottles and other lines this week?

<details><summary>🐍 Python · Guard-railed price proposals</summary>

```json
[
  {
    "sku": "P-1",
    "name": "Wireless earbuds",
    "current_price": 49.99,
    "competitor_avg": 45.5,
    "proposed_price": 49.99,
    "change_pct": 0.0,
    "margin_pct": 58.0,
    "expected_weekly_units": 320,
    "weekly_gross_profit_now": 9277,
    "weekly_gross_profit_new": 9277,
    "weeks_of_stock": 3.0,
    "pricing_reason": "Low stock (3.0 weeks): hold price even though it is +9.9% vs competitors, to avoid selling out"
  },
  {
    "sku": "P-2",
    "name": "Stainless water bottle 750ml",
    "current_price": 14.99,
    "competitor_avg": 17.83,
    "proposed_price": 16.49,
    "change_pct": 10.0,
    "margin_pct": 62.4,
    "expected_weekly_units": 481,
    "weekly_gross_profit_now": 4747,
    "weekly_gross_profit_new": 4945,
    "weeks_of_stock": 6.0,
    "pricing_reason": "Move toward competitor average (-15.9% vs competitors); capped at the 10% max move"
  },
  {
    "sku": "P-3",
    "name": "Fleece throw blanket",
    "current_price": 29.99,
    "competitor_avg": 29.5,
    "proposed_price": 28.02,
    "change_pct": -6.6,
    "margin_pct": 66.1,
    "expected_weekly_units": 97,
    "weekly_gross_profit_now": 1742,
    "weekly_gross_profit_new": 1802,
    "weeks_of_stock": 22.0,
    "pricing_reason": "Overstock (22.0 weeks of stock): cut to clear"
  }
]
```

</details>

**🦙 Ollama:**

### Pricing Memo

| SKU | Current Price | Proposed Price | Decision | Reason | Expected Profit Impact | Notes for Marketing and Store Teams |
|-----|---------------|----------------|----------|--------|-----------------------|-------------------------------------|
| P-1 | $49.99        | $49.99         | APPROVE  | Low stock (3.0 weeks): hold price even though it is +9.9% vs competitors, to avoid selling out. | No change in weekly gross profit. | Ensure clear communication to the store teams about the low stock situation and the importance of maintaining current stock levels. |
| P-2 | $14.99        | $16.49         | ADJUST   | Move toward competitor average (-15.9% vs competitors); capped at the 10% max move. | Increase weekly gross profit by $198. | Communicate the rationale to customers and emphasize the quality and value of the product. Monitor competitor pricing closely and be prepared to adjust further if necessary. |
| P-3 | $29.99        | $28.02         | REJECT   | Overstock (22.0 weeks of stock): cut to clear. | Increase weekly gross profit by $60. | Focus on promoting the sale through marketing campaigns and special offers to clear the stock quickly. Consider offering additional value-added services or discounts to attract customers. |

### Summary of Risks:
- **Stock Management:** Holding or cutting prices could lead to either stockouts or overstocking.
- **Customer Perception:** Price changes can affect customer perception and brand image.
- **Competitor Response:** Competitors might react to price changes, leading to competitive pressures.
- **Sales Volume:** Price changes can impact sales volume, both positively and negatively.

By carefully considering these risks, the proposed price changes can be implemented more effectively to balance volume, margin, and price perception.


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
