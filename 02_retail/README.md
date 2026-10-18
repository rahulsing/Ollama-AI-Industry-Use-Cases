# 🛒 Retail: 10 AI Use Cases

**Stores, e-commerce and consumer brands.** AI agents for forecasting, pricing, ranging, customer service and store operations in stores and e-commerce.

[⬅ All industries](../README.md) · [New to retail?](#-new-to-retail) · [Use cases](#-use-cases) · [Primer & glossary](PRIMER.md)

![Use cases](https://img.shields.io/badge/use%20cases-10-success)
![CrewAI](https://img.shields.io/badge/CrewAI-3-FF5A50)
![LangChain](https://img.shields.io/badge/LangChain-7-1C3C3C)

```bash
# from the repo root, with Ollama running
python 02_retail/01_demand_forecasting_agent/app.py
```

---

## 🎓 New to retail?

**How a retailer makes money:** it buys products from suppliers (*cost*) and sells them for more (*price*). The
difference is the *gross margin*. Profit comes from selling enough volume at a healthy margin, while keeping stores,
warehouses and delivery costs under control.

**What makes it hard:**
1. **Inventory** is cash sitting on shelves. Too little means empty shelves and lost sales; too much means markdowns and waste.
2. **Pricing** must beat competitors without destroying margin, and customers notice price swings.
3. **Customers** compare everything online; reviews and service quality directly drive sales.
4. **Margins are thin.** A supermarket may keep only 2-4p of profit from every 1 of sales, so promotions that lose money,
   products that don't earn their shelf space, or 1-2% of stock lost to theft and waste (*shrink*) make a real difference.

Every use case README starts with **"The business problem"**: what happens today, who does the work, why it's hard,
and the key terms explained. For more, see the **[Retail Primer & glossary](PRIMER.md)** (38 terms).

| Department | What it does | Use cases |
|---|---|---|
| 📦 **Supply Chain & Inventory** | Forecasts demand, orders from suppliers and keeps the right stock in the right place. | [01](01_demand_forecasting_agent/), [09](09_supplier_notice_extractor/) |
| 🙋 **Customer Insight** | Listens to customers (reviews, complaints, behaviour) to improve products and service. | [02](02_product_review_analyzer/), [10](10_customer_segmentation/) |
| 🏷️ **Merchandising & Pricing** | Decides what to sell, at what price and with which promotions. | [03](03_dynamic_pricing_advisor/), [04](04_promotion_performance_analyzer/), [05](05_range_review_assistant/) |
| 💬 **E-commerce & Customer Service** | Helps customers find, buy and return products online, in the app and in store. | [06](06_online_shopping_assistant/), [07](07_returns_policy_assistant/) |
| 🏬 **Store Operations & Loss Prevention** | Runs the stores day to day and protects stock from theft, damage and waste. | [08](08_shrink_loss_analyzer/) |

---

## 📚 Use Cases

### 📦 Supply Chain & Inventory

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 01 | **Demand Forecasting & Replenishment Agent** | Forecasts weekly demand per product and recommends what to reorder, flagging stock-out risks. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](01_demand_forecasting_agent/) |
| 09 | **Supplier Notice Extractor** | Turns supplier emails about delays, price rises, short shipments and pack changes into a buyer's action list. | LangChain | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](09_supplier_notice_extractor/) |

### 🙋 Customer Insight

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 02 | **Product Review Analyzer** | Turns customer reviews into sentiment, complaint themes, defects and safety issues. | LangChain | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](02_product_review_analyzer/) |
| 10 | **Customer Segmentation & Campaign Planner** | Groups loyalty customers into segments and plans a marketing campaign for each. | LangChain | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](10_customer_segmentation/) |

### 🏷️ Merchandising & Pricing

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 03 | **Dynamic Pricing Advisor** | Recommends price changes from competitor prices, stock levels and elasticity, within margin guardrails. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](03_dynamic_pricing_advisor/) |
| 04 | **Promotion Performance Analyzer** | Measures whether last month's promotions really made money and which to repeat, rework or drop. | LangChain | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](04_promotion_performance_analyzer/) |
| 05 | **Range Review & Assortment Planner** | Decides which products to delist, keep or give more shelf space in a category range review. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](05_range_review_assistant/) |

### 💬 E-commerce & Customer Service

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 06 | **Online Shopping Assistant** | Helps shoppers find the right product, then checks store stock for click-and-collect and delivery options. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](06_online_shopping_assistant/) |
| 07 | **Returns & Refund Policy Assistant (RAG)** | Answers "can I return this?" questions with a decision based on the store's returns policy. | LangChain | RAG | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](07_returns_policy_assistant/) |

### 🏬 Store Operations & Loss Prevention

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 08 | **Store Shrink & Loss Prevention Analyzer** | Finds why stores lose more stock than they should and writes a 30-day action plan. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](08_shrink_loss_analyzer/) |

## 🧩 By Framework

### ![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) CrewAI (3)

| # | Use Case | Pattern | Code |
|---|---|---|---|
| 03 | Dynamic Pricing Advisor | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](03_dynamic_pricing_advisor/) |
| 05 | Range Review & Assortment Planner | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](05_range_review_assistant/) |
| 08 | Store Shrink & Loss Prevention Analyzer | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](08_shrink_loss_analyzer/) |

### ![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) LangChain (7)

| # | Use Case | Pattern | Code |
|---|---|---|---|
| 01 | Demand Forecasting & Replenishment Agent | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](01_demand_forecasting_agent/) |
| 02 | Product Review Analyzer | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](02_product_review_analyzer/) |
| 04 | Promotion Performance Analyzer | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](04_promotion_performance_analyzer/) |
| 06 | Online Shopping Assistant | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](06_online_shopping_assistant/) |
| 07 | Returns & Refund Policy Assistant (RAG) | RAG | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](07_returns_policy_assistant/) |
| 09 | Supplier Notice Extractor | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](09_supplier_notice_extractor/) |
| 10 | Customer Segmentation & Campaign Planner | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](10_customer_segmentation/) |

---

[⬅ Back to all industries](../README.md)
