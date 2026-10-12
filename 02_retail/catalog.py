"""Retail industry catalog. Regenerate docs after editing:  python scripts/build_docs.py"""

DOMAIN = {
    "name": "Retail",
    "icon": "🛒",
    "tagline": "Stores, e-commerce and consumer brands",
    "description": "AI agents for forecasting, pricing and customer insight in stores and e-commerce.",
}

CATEGORIES = {
    "supply": "📦 Supply Chain & Inventory",
    "customer": "🙋 Customer Insight",
    "merch": "🏷️ Merchandising & Pricing",
}

# (slug, title, category, framework, pattern, description, how_it_works)
USE_CASES = [
    ("01_demand_forecasting_agent", "Demand Forecasting & Replenishment Agent", "supply", "LangChain", "Tool-calling agent",
     "Forecasts weekly demand per product and recommends what to reorder, flagging stock-out risks.",
     "Tools compute trend-based forecasts with promotion uplift, weeks of cover, safety stock and order quantities "
     "in full cases; the agent explains priorities and actions for slow sellers."),
    ("02_product_review_analyzer", "Product Review Analyzer", "customer", "LangChain", "Structured extraction",
     "Turns customer reviews into sentiment, complaint themes, defects and safety issues.",
     "Each review is classified into a Pydantic schema, Python aggregates the counts, and an LLM chain writes the "
     "quality report with escalation of safety concerns."),
    ("03_dynamic_pricing_advisor", "Dynamic Pricing Advisor", "merch", "CrewAI", "Multi-agent",
     "Recommends price changes from competitor prices, stock levels and elasticity, within margin guardrails.",
     "Python proposes prices (30% margin floor, max 10% move) and estimates profit impact; a Pricing Analyst agent "
     "explains them and a Category Manager agent approves or adjusts and writes the pricing memo."),
]
