# 04 · Promotion Performance Analyzer

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Chain-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🛒 Retail · **Category:** 🏷️ Merchandising & Pricing

## 🛒 The business problem (new to retail? start here)

**In the business today:** After each promotion, the promotions team checks whether it was worth it before deciding to run it again. Often they only look at how many extra units sold.

**Who does this work:** Promotions analysts, category managers and supplier account teams.

**Why it's hard:** Volume is easy to see but profit is not: customers stock up and buy less later, shoppers switch from our other products, and the discount and marketing cost money. A promotion can double sales and still lose money.

### Key terms
- **Incremental profit**: The extra profit a promotion earns on top of what normal sales would have made, after all its side effects.
- **Promotion uplift**: The extra sales a promotion generates over normal demand.
- **Post-promotion dip**: Customers stock up during a promotion (pantry loading), so sales fall below normal for a few weeks afterwards.
- **Cannibalisation**: When a promotion takes sales from our own similar products instead of winning new ones.
- **Supplier funding**: Money a supplier pays per unit sold on promotion, to share the cost of the discount.
- **Gross margin**: (Price - cost) / price. A 30% margin means 30p of every 1 of sales is left after paying for the product.

More terms: [Retail Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Measures whether last month's promotions really made money and which to repeat, rework or drop.

### How it works
Python computes each promotion's incremental profit after the post-promotion dip, cannibalisation of sister products and marketing spend, and the extra supplier funding needed to break even; an LLM chain writes the review.

```mermaid
flowchart LR
    IN["📄 Promotion sales & costs"] --> PY["🐍 Python<br/>Incremental profit after dip, cannibalisation & spend"]
    PY -->|"✅ decision & numbers"| CH["🔗 LangChain prompt<br/>explain, don't decide"]
    CH <-.->|"💬"| LLM(["🦙 Ollama"])
    CH --> OUT["📝 Post-promotion review"]
    OUT --> HU["🧑‍⚖️ Human review"]
    classDef data fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    classDef rules fill:#d1fae5,stroke:#059669,color:#064e3b
    classDef ai fill:#ede9fe,stroke:#7c3aed,color:#3b0764
    classDef llm fill:#1f2937,stroke:#111827,color:#ffffff
    classDef out fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef human fill:#f3f4f6,stroke:#6b7280,color:#111827
    class IN data
    class PY rules
    class CH ai
    class LLM llm
    class OUT out
    class HU human
```

<sub>🟦 data · 🟩 Python: maths & rules (auditable) · 🟪 AI: reasoning & writing · ⬛ local LLM · 🟨 result</sub>

## 💬 Sample conversation

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 8 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** How did last month's promotions perform? Which should we run again?

<details><summary>🐍 Python · Incremental profit by promotion</summary>

```json
[
  {
    "id": "PR-01",
    "product": "Coffee beans 1kg",
    "mechanic": "25% off",
    "volume_uplift_pct": 242,
    "promo_week_profit": 2050,
    "normal_week_profit": 960,
    "post_promo_dip_units": 90,
    "post_promo_dip_loss": 720,
    "cannibalisation_loss": 192,
    "cannibalised_product": "Coffee beans 500g",
    "marketing_spend": 800,
    "incremental_profit": -622,
    "biggest_drag_on_profit": "marketing spend (800)",
    "verdict": "REWORK",
    "extra_supplier_funding_per_unit_to_break_even": 1.52
  },
  {
    "id": "PR-02",
    "product": "Pasta sauce 500g",
    "mechanic": "2 for 5.00",
    "volume_uplift_pct": 200,
    "promo_week_profit": 1170,
    "normal_week_profit": 480,
    "post_promo_dip_units": 40,
    "post_promo_dip_loss": 64,
    "cannibalisation_loss": 81,
    "cannibalised_product": "Own-brand pasta sauce",
    "marketing_spend": 300,
    "incremental_profit": 245,
    "biggest_drag_on_profit": "marketing spend (300)",
    "verdict": "REPEAT",
    "extra_supplier_funding_per_unit_to_break_even": null
  },
  {
    "id": "PR-03",
    "product": "Kitchen towels 4-pack",
    "mechanic": "10% off",
    "volume_uplift_pct": 15,
    "promo_week_profit": 437,
    "normal_week_profit": 500,
    "post_promo_dip_units": 0,
    "post_promo_dip_loss": 0,
    "cannibalisation_loss": 0,
    "cannibalised_product": null,
    "marketing_spend": 250,
    "incremental_profit": -313,
    "biggest_drag_on_profit": "marketing spend (250)",
    "verdict": "DROP",
    "extra_supplier_funding_per_unit_to_break_even": null
  }
]
```

</details>

**🦙 Ollama:**

### Promotion Review Summary

1. **PR-01 (Coffee beans 1kg)**
   - **Verdict:** REWORK
   - **Incremental Profit:** -622
   - **Biggest Drag on Profit:** marketing spend (800)
   - **Fix Suggestion:** Increase supplier funding by 1.52 per unit to break even.

2. **PR-02 (Pasta sauce 500g)**
   - **Verdict:** REPEAT
   - **Incremental Profit:** 245
   - **Biggest Drag on Profit:** marketing spend (300)
   - **Fix Suggestion:** None needed, as the promotion is already profitable.

3. **PR-03 (Kitchen towels 4-pack)**
   - **Verdict:** DROP
   - **Incremental Profit:** -313
   - **Biggest Drag on Profit:** marketing spend (250)
   - **Fix Suggestion:** None needed, as the promotion is not profitable.

### Lessons for Next Quarter

1. **Optimize Marketing Spend:** High marketing spend can significantly impact profitability. Consider more targeted marketing strategies to reduce costs without compromising sales.
2. **Balance Discounts with Profitability:** Shallow discounts can be more effective in maintaining profit margins while still driving sales. Evaluate the impact of deeper discounts on overall profitability.
3. **Monitor Cannibalization:** Ensure that promotions do not negatively impact sales of other products. Target promotions to specific product lines to avoid cannibalization and maintain overall category health.


## Run
```bash
# from the repo root, with Ollama running
python 02_retail/04_promotion_performance_analyzer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Retail use cases](../README.md#-use-cases) · [All industries](../../README.md)
