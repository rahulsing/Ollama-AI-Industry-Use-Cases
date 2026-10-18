"""Retail industry catalog. Regenerate docs after editing:  python scripts/build_docs.py"""

DOMAIN = {
    "name": "Retail",
    "icon": "🛒",
    "tagline": "Stores, e-commerce and consumer brands",
    "description": "AI agents for forecasting, pricing, ranging, customer service and store operations in stores and e-commerce.",
}

CATEGORIES = {
    "supply": "📦 Supply Chain & Inventory",
    "customer": "🙋 Customer Insight",
    "merch": "🏷️ Merchandising & Pricing",
    "service": "💬 E-commerce & Customer Service",
    "store": "🏬 Store Operations & Loss Prevention",
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
    ("04_promotion_performance_analyzer", "Promotion Performance Analyzer", "merch", "LangChain", "Chain",
     "Measures whether last month's promotions really made money and which to repeat, rework or drop.",
     "Python computes each promotion's incremental profit after the post-promotion dip, cannibalisation of sister "
     "products and marketing spend, and the extra supplier funding needed to break even; an LLM chain writes the review."),
    ("05_range_review_assistant", "Range Review & Assortment Planner", "merch", "CrewAI", "Multi-agent",
     "Decides which products to delist, keep or give more shelf space in a category range review.",
     "Python ranks products on profit per shelf facing and checks how much demand would switch to other products "
     "(delist only if 70%+ transfers and no unique need is left unserved); a Category Analyst agent explains the "
     "evidence and a Senior Buyer agent writes the range review memo."),
    ("06_online_shopping_assistant", "Online Shopping Assistant", "service", "LangChain", "Tool-calling agent",
     "Helps shoppers find the right product, then checks store stock for click-and-collect and delivery options.",
     "Tools search the catalog with price and size filters, check live stock by store and city, and quote delivery; "
     "the agent recommends only what the tools return, so it never invents products, prices or stock."),
    ("07_returns_policy_assistant", "Returns & Refund Policy Assistant (RAG)", "service", "LangChain", "RAG",
     "Answers \"can I return this?\" questions with a decision based on the store's returns policy.",
     "Retrieval finds the relevant policy sections, the LLM turns the customer's message into a returns checklist, "
     "Python applies the rules (return windows, restocking fee, final sale, proof of purchase) and the LLM explains."),
    ("08_shrink_loss_analyzer", "Store Shrink & Loss Prevention Analyzer", "store", "CrewAI", "Multi-agent",
     "Finds why stores lose more stock than they should and writes a 30-day action plan.",
     "Python splits shrink into known loss (waste, damage) and unknown loss (theft, errors), compares stores to the "
     "1.5% benchmark and flags unusual till refunds and voids for review; a Loss Prevention Analyst agent finds the "
     "causes and a Regional Operations Manager agent writes the plan."),
    ("09_supplier_notice_extractor", "Supplier Notice Extractor", "supply", "LangChain", "Structured extraction",
     "Turns supplier emails about delays, price rises, short shipments and pack changes into a buyer's action list.",
     "Each email is first classified (delay, price change, short shipment, substitution), then the details for that "
     "type are extracted into a small Pydantic schema; Python checks them against stock cover and the supplier "
     "contract (stock-out risk, notice period, price cap, hidden pack-size increases); an LLM chain writes the actions."),
    ("10_customer_segmentation", "Customer Segmentation & Campaign Planner", "customer", "LangChain", "Chain",
     "Groups loyalty customers into segments and plans a marketing campaign for each.",
     "Python scores customers on recency, frequency and spend (RFM), sizes each segment's share of revenue and sets "
     "its discount limit; an LLM chain writes the offer, channel and message for every segment within those limits."),
]
