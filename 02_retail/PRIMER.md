# 🛒 Retail Primer: the business behind the use cases

New to retail? This page explains how the industry works, which department each use case helps, and every
term used in these use cases, in plain English.

[⬅ Back to Retail use cases](README.md)

---

## How it works

**How a retailer makes money:** it buys products from suppliers (*cost*) and sells them for more (*price*). The
difference is the *gross margin*. Profit comes from selling enough volume at a healthy margin, while keeping stores,
warehouses and delivery costs under control.

**What makes it hard:**
1. **Inventory** is cash sitting on shelves. Too little means empty shelves and lost sales; too much means markdowns and waste.
2. **Pricing** must beat competitors without destroying margin, and customers notice price swings.
3. **Customers** compare everything online; reviews and service quality directly drive sales.
4. **Margins are thin.** A supermarket may keep only 2-4p of profit from every 1 of sales, so promotions that lose money,
   products that don't earn their shelf space, or 1-2% of stock lost to theft and waste (*shrink*) make a real difference.

## Departments and use cases

| Department | What it does | Use cases |
|---|---|---|
| 📦 **Supply Chain & Inventory** | Forecasts demand, orders from suppliers and keeps the right stock in the right place. | [01](01_demand_forecasting_agent/), [09](09_supplier_notice_extractor/) |
| 🙋 **Customer Insight** | Listens to customers (reviews, complaints, behaviour) to improve products and service. | [02](02_product_review_analyzer/), [10](10_customer_segmentation/) |
| 🏷️ **Merchandising & Pricing** | Decides what to sell, at what price and with which promotions. | [03](03_dynamic_pricing_advisor/), [04](04_promotion_performance_analyzer/), [05](05_range_review_assistant/) |
| 💬 **E-commerce & Customer Service** | Helps customers find, buy and return products online, in the app and in store. | [06](06_online_shopping_assistant/), [07](07_returns_policy_assistant/) |
| 🏬 **Store Operations & Loss Prevention** | Runs the stores day to day and protects stock from theft, damage and waste. | [08](08_shrink_loss_analyzer/) |

---

## Glossary

### Supply chain

- <a id="demand-forecasting"></a>**Demand forecasting**: Predicting how many units will sell in future weeks, using past sales, trends, seasons and promotions.
- <a id="lead-time"></a>**Lead time**: How long a supplier takes to deliver after an order is placed.
- <a id="promotion-uplift"></a>**Promotion uplift**: The extra sales a promotion generates over normal demand.
- <a id="purchase-order-po"></a>**Purchase order (PO)**: A formal order to a supplier: which products, how many, at what price and when to deliver.
- <a id="reorder-point"></a>**Reorder point**: The stock level at which a new order must be placed to arrive before running out.
- <a id="replenishment"></a>**Replenishment**: Re-ordering stock from suppliers so shelves don't run empty.
- <a id="safety-stock"></a>**Safety stock**: Extra stock held to protect against forecast errors and late deliveries.
- <a id="short-shipment"></a>**Short shipment**: A delivery with fewer units than were ordered.
- <a id="shrinkflation"></a>**Shrinkflation**: A smaller pack sold at the same price: a hidden price increase.
- <a id="stock-out"></a>**Stock-out**: When a product is unavailable: a lost sale and an unhappy customer.
- <a id="weeks-of-cover"></a>**Weeks of cover**: How many weeks current stock will last at forecast sales.

### Customer

- <a id="control-group"></a>**Control group**: Customers deliberately left out of a campaign so its real effect can be measured.
- <a id="customer-reviews--sentiment"></a>**Customer reviews / sentiment**: Star ratings and comments; sentiment is whether they are positive, neutral or negative.
- <a id="customer-segment"></a>**Customer segment**: A group of customers who behave alike and get the same marketing approach.
- <a id="product-defect"></a>**Product defect**: A fault in the product itself (leaks, breakage), as opposed to a matter of taste.
- <a id="product-recall"></a>**Product recall**: Withdrawing an unsafe product from sale and from customers. Safety complaints must be escalated fast.
- <a id="rfm"></a>**RFM**: Recency, Frequency, Monetary value: scoring customers on how recently, how often and how much they buy.
- <a id="win-back-campaign"></a>**Win-back campaign**: An offer aimed at valuable customers who have stopped buying.

### Pricing

- <a id="category-manager"></a>**Category manager**: The person who owns a product category's range, pricing and profit.
- <a id="competitive-price-index"></a>**Competitive price index**: Our price compared to competitors' average for the same product.
- <a id="gross-margin"></a>**Gross margin**: (Price - cost) / price. A 30% margin means 30p of every 1 of sales is left after paying for the product.
- <a id="markdown"></a>**Markdown**: A permanent price cut, usually to clear excess or seasonal stock.
- <a id="price-elasticity"></a>**Price elasticity**: How much volume changes when price changes. Elasticity of -2 means a 1% price cut lifts volume about 2%.

### Promotions & range

- <a id="cannibalisation"></a>**Cannibalisation**: When a promotion takes sales from our own similar products instead of winning new ones.
- <a id="delist"></a>**Delist**: To stop stocking a product.
- <a id="facing"></a>**Facing**: One product's width at the front of the shelf. More facings means more space, visibility and stock on display.
- <a id="incremental-profit"></a>**Incremental profit**: The extra profit a promotion earns on top of what normal sales would have made, after all its side effects.
- <a id="post-promotion-dip"></a>**Post-promotion dip**: Customers stock up during a promotion (pantry loading), so sales fall below normal for a few weeks afterwards.
- <a id="range-review"></a>**Range review**: A regular review of which products a category should stock, drop or add.
- <a id="supplier-funding"></a>**Supplier funding**: Money a supplier pays per unit sold on promotion, to share the cost of the discount.
- <a id="transferable-demand"></a>**Transferable demand**: The share of a product's buyers who would buy something else in the range if it were removed.

### Service

- <a id="click-and-collect"></a>**Click-and-collect**: Order online, then pick the item up in a store.
- <a id="final-sale"></a>**Final sale**: Items, usually on clearance, sold on the condition that they can't be returned unless faulty.
- <a id="proof-of-purchase"></a>**Proof of purchase**: A receipt, order confirmation or the payment card used, showing when and where an item was bought.
- <a id="restocking-fee"></a>**Restocking fee**: A share of the price kept back on some opened returns, to cover checking, repackaging and reselling the item.

### Stores

- <a id="known-vs-unknown-loss"></a>**Known vs unknown loss**: Known loss is recorded when it happens (waste, damage); unknown loss only shows up as a gap at the stock count (theft, errors).
- <a id="shrink"></a>**Shrink**: Stock that is lost instead of sold (theft, damage, waste, admin errors), usually shown as a % of sales.
- <a id="till-exceptions"></a>**Till exceptions**: Unusual till activity, like refunds without a receipt or cancelled items, that loss prevention teams review.

---

*Definitions are simplified for learning. Exact rules vary by country and regulator.*
