"""Demand Forecasting & Replenishment Agent — LangChain tool-calling agent + Ollama.

Run:  python 02_retail/01_demand_forecasting_agent/app.py
      python 02_retail/01_demand_forecasting_agent/app.py "Will SKU-102 run out before the next delivery?"
"""

import math
import statistics
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from langchain_core.tools import tool

from common import banner, run_agent, section

# Last 8 weeks of unit sales, current stock, supplier lead time and planned promotions
PRODUCTS = {
    "SKU-101": {"name": "Organic oat milk 1L", "sales": [410, 395, 430, 420, 445, 460, 452, 470], "stock": 900,
                "on_order": 0, "lead_time_weeks": 1, "case_size": 12, "promo_next_week": False},
    "SKU-102": {"name": "Sunscreen SPF50 200ml", "sales": [80, 95, 120, 150, 175, 210, 240, 260], "stock": 380,
                "on_order": 0, "lead_time_weeks": 2, "case_size": 24, "promo_next_week": True},
    "SKU-103": {"name": "Wool scarf (grey)", "sales": [60, 52, 41, 35, 30, 22, 18, 15], "stock": 640,
                "on_order": 200, "lead_time_weeks": 4, "case_size": 10, "promo_next_week": False},
}
PROMO_UPLIFT = 0.35   # promotions lift demand ~35%
SERVICE_Z = 1.65      # ~95% service level


@tool
def list_products() -> dict:
    """List SKUs with product names."""
    return {sku: p["name"] for sku, p in PRODUCTS.items()}


@tool
def forecast_demand(sku: str, weeks: int = 4) -> dict:
    """Forecast weekly unit demand for a SKU using the recent trend, plus promotion uplift."""
    p = PRODUCTS[sku]
    recent = p["sales"][-4:]
    trend = (recent[-1] - recent[0]) / 3  # units per week
    base = statistics.mean(recent)
    forecast = []
    for w in range(1, weeks + 1):
        f = max(base + trend * (w + 1.5), 0)
        if w == 1 and p["promo_next_week"]:
            f *= 1 + PROMO_UPLIFT
        forecast.append(round(f))
    return {"sku": sku, "trend_units_per_week": round(trend, 1), "weekly_forecast": forecast,
            "promo_next_week": p["promo_next_week"]}


@tool
def reorder_plan(sku: str) -> dict:
    """Weeks of stock cover, reorder point and recommended order quantity (rounded to full cases)."""
    p = PRODUCTS[sku]
    fc_info = forecast_demand.invoke({"sku": sku, "weeks": 12})
    fc = fc_info["weekly_forecast"]
    lead, horizon = p["lead_time_weeks"], p["lead_time_weeks"] + 2   # order covers lead time + 2 weeks
    lead_demand = sum(fc[:lead])
    safety = SERVICE_Z * statistics.stdev(p["sales"]) * math.sqrt(lead)
    reorder_point = lead_demand + safety
    available = p["stock"] + p["on_order"]
    cover_weeks, left = 0.0, available
    for f in fc:
        if left >= f:
            cover_weeks, left = cover_weeks + 1, left - f
        else:
            cover_weeks += left / f if f else 0
            break
    order_now = available < reorder_point
    need = reorder_point + sum(fc[lead:horizon]) - available if order_now else 0
    qty = math.ceil(need / p["case_size"]) * p["case_size"] if need > 0 else 0
    trend = fc_info["trend_units_per_week"]
    if trend < 0 and cover_weeks >= 6:
        status = "SLOW SELLER / OVERSTOCK (consider markdown or cancelling open orders)"
    elif trend > 0.05 * statistics.mean(p["sales"][-4:]):
        status = "GROWING DEMAND (do not discount)"
    else:
        status = "STEADY"
    return {"sku": sku, "available_units": available,
            "weeks_of_cover": f"{cover_weeks:.1f}" if cover_weeks < 12 else "12+",
            "lead_time_weeks": lead, "reorder_point": round(reorder_point),
            "order_now": order_now, "recommended_order_units": qty,
            "stockout_risk_before_delivery": available < lead_demand, "demand_status": status}


SYSTEM = (
    "You are a retail replenishment analyst. Use list_products, then forecast_demand and reorder_plan for each SKU. "
    "Copy numbers exactly from the tools. Give a table (SKU, product, weeks of cover, order now?, order units), flag "
    "stock-out risks first, mention trends and promotions, and suggest actions for slow sellers (e.g. markdown, "
    "cancel open orders)."
)


def main():
    banner("Retail 01 - Demand Forecasting & Replenishment Agent (LangChain agent)")
    q = sys.argv[1] if len(sys.argv) > 1 else "Review all products: what should we reorder this week and why?"
    section("Question", q)
    section("Answer", run_agent(SYSTEM, [list_products, forecast_demand, reorder_plan], q))


if __name__ == "__main__":
    main()
