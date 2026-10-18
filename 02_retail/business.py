"""Plain-English business context for people new to retail (used by build_docs.py and ui.py)."""

INDUSTRY_101 = """\
**How a retailer makes money:** it buys products from suppliers (*cost*) and sells them for more (*price*). The
difference is the *gross margin*. Profit comes from selling enough volume at a healthy margin, while keeping stores,
warehouses and delivery costs under control.

**What makes it hard:**
1. **Inventory** is cash sitting on shelves. Too little means empty shelves and lost sales; too much means markdowns and waste.
2. **Pricing** must beat competitors without destroying margin, and customers notice price swings.
3. **Customers** compare everything online; reviews and service quality directly drive sales.
4. **Margins are thin.** A supermarket may keep only 2-4p of profit from every 1 of sales, so promotions that lose money,
   products that don't earn their shelf space, or 1-2% of stock lost to theft and waste (*shrink*) make a real difference.
"""

AREAS = [
    ("supply", "Supply Chain & Inventory", "Forecasts demand, orders from suppliers and keeps the right stock in the right place."),
    ("customer", "Customer Insight", "Listens to customers (reviews, complaints, behaviour) to improve products and service."),
    ("merch", "Merchandising & Pricing", "Decides what to sell, at what price and with which promotions."),
    ("service", "E-commerce & Customer Service", "Helps customers find, buy and return products online, in the app and in store."),
    ("store", "Store Operations & Loss Prevention", "Runs the stores day to day and protects stock from theft, damage and waste."),
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
    "Purchase order (PO)": ("Supply chain", "A formal order to a supplier: which products, how many, at what price and when to deliver."),
    "Short shipment": ("Supply chain", "A delivery with fewer units than were ordered."),
    "Shrinkflation": ("Supply chain", "A smaller pack sold at the same price: a hidden price increase."),
    "Incremental profit": ("Promotions & range", "The extra profit a promotion earns on top of what normal sales would have made, after all its side effects."),
    "Post-promotion dip": ("Promotions & range", "Customers stock up during a promotion (pantry loading), so sales fall below normal for a few weeks afterwards."),
    "Cannibalisation": ("Promotions & range", "When a promotion takes sales from our own similar products instead of winning new ones."),
    "Supplier funding": ("Promotions & range", "Money a supplier pays per unit sold on promotion, to share the cost of the discount."),
    "Range review": ("Promotions & range", "A regular review of which products a category should stock, drop or add."),
    "Facing": ("Promotions & range", "One product's width at the front of the shelf. More facings means more space, visibility and stock on display."),
    "Transferable demand": ("Promotions & range", "The share of a product's buyers who would buy something else in the range if it were removed."),
    "Delist": ("Promotions & range", "To stop stocking a product."),
    "Click-and-collect": ("Service", "Order online, then pick the item up in a store."),
    "Restocking fee": ("Service", "A share of the price kept back on some opened returns, to cover checking, repackaging and reselling the item."),
    "Final sale": ("Service", "Items, usually on clearance, sold on the condition that they can't be returned unless faulty."),
    "Proof of purchase": ("Service", "A receipt, order confirmation or the payment card used, showing when and where an item was bought."),
    "Shrink": ("Stores", "Stock that is lost instead of sold (theft, damage, waste, admin errors), usually shown as a % of sales."),
    "Known vs unknown loss": ("Stores", "Known loss is recorded when it happens (waste, damage); unknown loss only shows up as a gap at the stock count (theft, errors)."),
    "Till exceptions": ("Stores", "Unusual till activity, like refunds without a receipt or cancelled items, that loss prevention teams review."),
    "RFM": ("Customer", "Recency, Frequency, Monetary value: scoring customers on how recently, how often and how much they buy."),
    "Customer segment": ("Customer", "A group of customers who behave alike and get the same marketing approach."),
    "Win-back campaign": ("Customer", "An offer aimed at valuable customers who have stopped buying."),
    "Control group": ("Customer", "Customers deliberately left out of a campaign so its real effect can be measured."),
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
    "04_promotion_performance_analyzer": (
        "After each promotion, the promotions team checks whether it was worth it before deciding to run it again. Often they only look at how many extra units sold.",
        "Promotions analysts, category managers and supplier account teams.",
        "Volume is easy to see but profit is not: customers stock up and buy less later, shoppers switch from our other products, and the discount and marketing cost money. A promotion can double sales and still lose money.",
        ["Incremental profit", "Promotion uplift", "Post-promotion dip", "Cannibalisation", "Supplier funding", "Gross margin"]),
    "05_range_review_assistant": (
        "Once or twice a year each category has a range review: buyers decide which products to drop, keep or give more shelf space, and tell the suppliers.",
        "Buyers and category managers, supported by category analysts.",
        "Shelf space is limited and every product wants more of it. Dropping a product on sales alone can upset loyal shoppers who have no alternative, while weak products quietly waste space.",
        ["Range review", "Facing", "Transferable demand", "Delist", "Stock-out", "Category manager"]),
    "06_online_shopping_assistant": (
        "Shoppers on the website or app ask what to buy and whether they can get it today. Store and contact-centre staff answer by checking the catalog and the stock system.",
        "E-commerce and customer service teams, and store colleagues.",
        "Customers want a fast, personal answer. A wrong answer about price or stock, like promising an item is in store when it isn't, loses the sale and the customer's trust.",
        ["Click-and-collect", "Stock-out"]),
    "07_returns_policy_assistant": (
        "Customers ask whether they can return an item and how they'll be refunded. Service staff look up the returns policy, check the dates and proof of purchase, and explain the decision.",
        "Customer service agents and store customer-desk staff.",
        "Returns policies have many rules (time windows, electronics, final sale, hygiene, faulty items) and staff apply them inconsistently. Customers must get the same correct answer everywhere.",
        ["Restocking fee", "Final sale", "Proof of purchase"]),
    "08_shrink_loss_analyzer": (
        "Every quarter, stock counts show how much stock was lost. The loss prevention team works out where and why, and agrees actions with store managers.",
        "Loss prevention analysts, regional and store managers.",
        "Losses mix theft, damage, waste and paperwork errors, and each needs a different fix. Unusual till activity must be reviewed fairly, without accusing staff on numbers alone.",
        ["Shrink", "Known vs unknown loss", "Till exceptions"]),
    "09_supplier_notice_extractor": (
        "Buyers receive a steady stream of supplier emails: late deliveries, price rises, short shipments and pack changes. Each one has to be read, checked and acted on.",
        "Buyers and supply chain planners.",
        "The important details are buried in free text, and the impact depends on our own stock and contract terms. Missing one email can mean empty shelves or paying more than the contract allows.",
        ["Purchase order (PO)", "Short shipment", "Shrinkflation", "Lead time", "Weeks of cover", "Stock-out"]),
    "10_customer_segmentation": (
        "The CRM team groups loyalty-card customers by how they shop and sends each group a different campaign.",
        "CRM and loyalty marketing teams.",
        "Sending the same discount to everyone wastes money on customers who would buy anyway and does too little for those about to leave.",
        ["RFM", "Customer segment", "Win-back campaign", "Control group"]),
}

# Flow diagram labels: (input data, what Python computes or decides, output). "" if Python does no maths.
FLOWS = {
    "01_demand_forecasting_agent": ("Sales history + stock levels", "", "Reorder plan + stock-out risks"),
    "02_product_review_analyzer": ("Customer reviews", "Count themes, defects & safety issues", "Quality report + escalations"),
    "03_dynamic_pricing_advisor": ("Prices, competitors & stock", "Guard-railed prices: 30% margin floor, max 10% move", "Pricing memo"),
    "04_promotion_performance_analyzer": ("Promotion sales & costs", "Incremental profit after dip, cannibalisation & spend", "Post-promotion review"),
    "05_range_review_assistant": ("Range sales, space & switching", "Profit per facing + transferable demand rules", "Range review memo"),
    "06_online_shopping_assistant": ("Catalog, store & warehouse stock", "", "Product picks + collect / delivery"),
    "07_returns_policy_assistant": ("Returns policy", "Return windows, fees & proof-of-purchase rules", "Returns decision + explanation"),
    "08_shrink_loss_analyzer": ("Stock losses & till logs", "Shrink vs 1.5% benchmark + till flags", "30-day action plan"),
    "09_supplier_notice_extractor": ("Supplier emails", "Check stock cover, orders & contract terms", "Buyer's action list"),
    "10_customer_segmentation": ("Loyalty customer history", "RFM segments + discount limits", "Campaign plan per segment"),
}

# What the user asks in the sample conversation (for use cases without a typed question)
ASK = {
    "02_product_review_analyzer": "What are customers saying about the AeroBlend 600W blender? Are there any safety issues?",
    "03_dynamic_pricing_advisor": "Should we change prices on our earbuds, water bottles and other lines this week?",
    "04_promotion_performance_analyzer": "How did last month's promotions perform? Which should we run again?",
    "05_range_review_assistant": "Which cereals should we delist, keep or give more space in the spring range review?",
    "08_shrink_loss_analyzer": "Why is shrink above target at some stores this quarter, and what should we do about it?",
    "09_supplier_notice_extractor": "We've had four supplier emails this morning. What do they mean for our stock and costs?",
    "10_customer_segmentation": "Who are our customer segments, and what campaign should each one get?",
}
