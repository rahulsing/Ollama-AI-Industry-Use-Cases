# 🛒 Retail: 3 AI Use Cases

**Stores, e-commerce and consumer brands.** AI agents for forecasting, pricing and customer insight in stores and e-commerce.

[⬅ All industries](../README.md) · [New to retail?](#-new-to-retail) · [Use cases](#-use-cases) · [Primer & glossary](PRIMER.md)

![Use cases](https://img.shields.io/badge/use%20cases-3-success)
![CrewAI](https://img.shields.io/badge/CrewAI-1-FF5A50)
![LangChain](https://img.shields.io/badge/LangChain-2-1C3C3C)

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

Every use case README starts with **"The business problem"**: what happens today, who does the work, why it's hard,
and the key terms explained. For more, see the **[Retail Primer & glossary](PRIMER.md)** (16 terms).

| Department | What it does | Use cases |
|---|---|---|
| 📦 **Supply Chain & Inventory** | Forecasts demand, orders from suppliers and keeps the right stock in the right place. | [01](01_demand_forecasting_agent/) |
| 🙋 **Customer Insight** | Listens to customers (reviews, complaints, behaviour) to improve products and service. | [02](02_product_review_analyzer/) |
| 🏷️ **Merchandising & Pricing** | Decides what to sell, at what price and with which promotions. | [03](03_dynamic_pricing_advisor/) |

---

## 📚 Use Cases

### 📦 Supply Chain & Inventory

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 01 | **Demand Forecasting & Replenishment Agent** | Forecasts weekly demand per product and recommends what to reorder, flagging stock-out risks. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](01_demand_forecasting_agent/) |

### 🙋 Customer Insight

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 02 | **Product Review Analyzer** | Turns customer reviews into sentiment, complaint themes, defects and safety issues. | LangChain | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](02_product_review_analyzer/) |

### 🏷️ Merchandising & Pricing

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 03 | **Dynamic Pricing Advisor** | Recommends price changes from competitor prices, stock levels and elasticity, within margin guardrails. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](03_dynamic_pricing_advisor/) |

## 🧩 By Framework

### ![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) CrewAI (1)

| # | Use Case | Pattern | Code |
|---|---|---|---|
| 03 | Dynamic Pricing Advisor | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](03_dynamic_pricing_advisor/) |

### ![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) LangChain (2)

| # | Use Case | Pattern | Code |
|---|---|---|---|
| 01 | Demand Forecasting & Replenishment Agent | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](01_demand_forecasting_agent/) |
| 02 | Product Review Analyzer | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](02_product_review_analyzer/) |

---

[⬅ Back to all industries](../README.md)
