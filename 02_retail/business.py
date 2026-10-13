"""Plain-English business context for people new to retail (used by build_docs.py and ui.py)."""

INDUSTRY_101 = """\
**How a retailer makes money:** it buys products from suppliers (*cost*) and sells them for more (*price*). The
difference is the *gross margin*. Profit comes from selling enough volume at a healthy margin, while keeping stores,
warehouses and delivery costs under control.

**What makes it hard:**
1. **Inventory** is cash sitting on shelves. Too little means empty shelves and lost sales; too much means markdowns and waste.
2. **Pricing** must beat competitors without destroying margin, and customers notice price swings.
3. **Customers** compare everything online; reviews and service quality directly drive sales.
"""

AREAS = [
    ("supply", "Supply Chain & Inventory", "Forecasts demand, orders from suppliers and keeps the right stock in the right place."),
    ("customer", "Customer Insight", "Listens to customers (reviews, complaints, behaviour) to improve products and service."),
    ("merch", "Merchandising & Pricing", "Decides what to sell, at what price and with which promotions."),
]

GLOSSARY = {
    "Demand forecasting": ("Supply chain", "Predicting how many units will sell in future weeks, using past sales, trends, seasons and promotions."),
    "Replenishment": ("Supply chain", "Re-ordering stock from suppliers so shelves don't run empty."),
    "Lead time": ("Supply chain", "How long a supplier takes to deliver after an order is placed."),
    "Weeks of cover": ("Supply chain", "How many weeks current stock will last at forecast sales."),
    "Safety stock": ("Supply chain", "Extra stock held to protect against forecast errors and late deliveries."),
    "Reorder point": ("Supply chain", "The stock level at which a new order must be placed to arrive before running out."),
    "Stock-out": ("Supply chain", "When a product is unavailable: a lost sale and an unhappy customer."),
    "Promotion uplift": ("Supply chain", "The extra sales a promotion generates over normal demand."),
    "Customer reviews / sentiment": ("Customer", "Star ratings and comments; sentiment is whether they are positive, neutral or negative."),
    "Product defect": ("Customer", "A fault in the product itself (leaks, breakage), as opposed to a matter of taste."),
    "Product recall": ("Customer", "Withdrawing an unsafe product from sale and from customers. Safety complaints must be escalated fast."),
    "Gross margin": ("Pricing", "(Price - cost) / price. A 30% margin means 30p of every 1 of sales is left after paying for the product."),
    "Price elasticity": ("Pricing", "How much volume changes when price changes. Elasticity of -2 means a 1% price cut lifts volume about 2%."),
    "Competitive price index": ("Pricing", "Our price compared to competitors' average for the same product."),
    "Markdown": ("Pricing", "A permanent price cut, usually to clear excess or seasonal stock."),
    "Category manager": ("Pricing", "The person who owns a product category's range, pricing and profit."),
}

# (in the business today, who does it, why it's hard, [glossary terms])
BUSINESS = {
    "01_demand_forecasting_agent": (
        "Every week, replenishment analysts decide how much of each product to order from suppliers, based on recent sales, trends and upcoming promotions.",
        "Replenishment / inventory analysts in the supply chain team.",
        "Large retailers manage tens of thousands of products. Seasonal products (sunscreen in summer, scarves in winter) change fast, and both empty shelves and overstock cost money.",
        ["Demand forecasting", "Replenishment", "Lead time", "Weeks of cover", "Safety stock", "Reorder point", "Stock-out", "Promotion uplift"]),
    "02_product_review_analyzer": (
        "Product and quality teams read customer reviews to spot recurring problems, fix product listings and catch safety issues early.",
        "Product managers, quality assurance and customer care teams.",
        "Popular products get thousands of reviews. Important signals, like a burning smell or a cracked blade, can be buried among comments about delivery or colour.",
        ["Customer reviews / sentiment", "Product defect", "Product recall"]),
    "03_dynamic_pricing_advisor": (
        "Pricing teams regularly review prices against competitors and stock levels: raise prices where there is room, cut to clear overstock, and protect margin.",
        "Pricing analysts and category managers.",
        "Every price change trades volume against margin, and customers notice price swings. Decisions must respect margin rules and be explainable.",
        ["Gross margin", "Price elasticity", "Competitive price index", "Markdown", "Category manager"]),
}

# Flow diagram labels: (input data, what Python computes or decides, output). "" if Python does no maths.
FLOWS = {
    "01_demand_forecasting_agent": ("Sales history + stock levels", "", "Reorder plan + stock-out risks"),
    "02_product_review_analyzer": ("Customer reviews", "Count themes, defects & safety issues", "Quality report + escalations"),
    "03_dynamic_pricing_advisor": ("Prices, competitors & stock", "Guard-railed prices: 30% margin floor, max 10% move", "Pricing memo"),
}

# What the user asks in the sample conversation (for use cases without a typed question)
ASK = {
    "02_product_review_analyzer": "What are customers saying about the AeroBlend 600W blender? Are there any safety issues?",
    "03_dynamic_pricing_advisor": "Should we change prices on our earbuds, water bottles and other lines this week?",
}
