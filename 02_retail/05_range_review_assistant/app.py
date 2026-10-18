"""Range Review & Assortment Planner — CrewAI + Ollama.

Python scores every product on profit per shelf facing and how much of its demand would transfer to other
products if it were delisted; agents explain the evidence and write the range review decisions.

Run:  python 02_retail/05_range_review_assistant/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

# Breakfast cereal aisle, last 12 weeks. transferable = share of buyers who would switch to another product
# on the shelf if this one were removed (from loyalty-card switching data). unique_need = only option for a need.
CATEGORY = "Breakfast cereals"
PRODUCTS = [
    {"sku": "C-01", "name": "Honey oat clusters 500g", "weekly_sales": 1450, "margin_pct": 32, "facings": 4, "transferable": 0.55, "oos_rate": 0.07, "unique_need": None},
    {"sku": "C-02", "name": "Corn flakes 750g", "weekly_sales": 1680, "margin_pct": 24, "facings": 5, "transferable": 0.60, "oos_rate": 0.02, "unique_need": None},
    {"sku": "C-03", "name": "Choco puffs 375g", "weekly_sales": 920, "margin_pct": 30, "facings": 3, "transferable": 0.70, "oos_rate": 0.01, "unique_need": None},
    {"sku": "C-04", "name": "Gluten-free granola 400g", "weekly_sales": 200, "margin_pct": 38, "facings": 3, "transferable": 0.15, "oos_rate": 0.03, "unique_need": "gluten-free"},
    {"sku": "C-05", "name": "Bran flakes 500g", "weekly_sales": 310, "margin_pct": 26, "facings": 3, "transferable": 0.85, "oos_rate": 0.00, "unique_need": None},
    {"sku": "C-06", "name": "Fruit muesli 1kg", "weekly_sales": 640, "margin_pct": 35, "facings": 2, "transferable": 0.40, "oos_rate": 0.09, "unique_need": None},
    {"sku": "C-07", "name": "Frosted rings 300g", "weekly_sales": 240, "margin_pct": 28, "facings": 3, "transferable": 0.80, "oos_rate": 0.00, "unique_need": None},
    {"sku": "C-08", "name": "Protein crunch 350g", "weekly_sales": 380, "margin_pct": 40, "facings": 2, "transferable": 0.35, "oos_rate": 0.04, "unique_need": None},
]
BOTTOM_N = 3                    # delist candidates come from the 3 weakest products on profit per facing
MIN_TRANSFER_TO_DELIST = 0.70   # most buyers must have an alternative they already accept
OOS_TO_EXPAND = 0.05            # out of stock more than 5% of the time -> needs more space


def score(products: list[dict]) -> list[dict]:
    rows = []
    for p in products:
        profit = p["weekly_sales"] * p["margin_pct"] / 100
        rows.append({**p, "weekly_profit": round(profit), "profit_per_facing": round(profit / p["facings"])})
    ranked = sorted(rows, key=lambda r: r["profit_per_facing"])
    bottom = {r["sku"] for r in ranked[:BOTTOM_N]}
    for r in rows:
        if r["sku"] in bottom and r["transferable"] >= MIN_TRANSFER_TO_DELIST and not r["unique_need"]:
            r["proposal"] = "DELIST"
            r["profit_kept_by_switching"] = round(r["weekly_profit"] * r["transferable"])
            r["profit_at_risk"] = r["weekly_profit"] - r["profit_kept_by_switching"]
        elif r["oos_rate"] > OOS_TO_EXPAND:
            r["proposal"] = "ADD A FACING"
        elif r["sku"] in bottom and r["unique_need"]:
            r["proposal"] = f"KEEP (only {r['unique_need']} option)"
        else:
            r["proposal"] = "KEEP"
    return rows


def main():
    banner("Retail 05 - Range Review & Assortment Planner (CrewAI)")
    rows = score(PRODUCTS)
    freed = sum(r["facings"] for r in rows if r["proposal"] == "DELIST")
    wanted = sum(1 for r in rows if r["proposal"] == "ADD A FACING")
    facts = {"category": CATEGORY, "products": rows, "facings_freed_by_delists": freed,
             "facings_requested_by_expansions": wanted, "facings_left_over": freed - wanted,
             "weekly_profit_at_risk_from_delists": sum(r.get("profit_at_risk", 0) for r in rows),
             "rules": f"DELIST = bottom {BOTTOM_N} on profit per facing AND at least {MIN_TRANSFER_TO_DELIST:.0%} of demand "
                      f"transfers AND no unique need; ADD A FACING = out of stock more than {OOS_TO_EXPAND:.0%} of the time"}
    section("Range scorecard", json.dumps(facts, indent=2))

    analyst = make_agent("Category Analyst", "Explain the evidence behind each range proposal",
                         "Retail category analyst who uses loyalty-card switching data, not gut feel.")
    buyer = make_agent("Senior Buyer", "Make the final range decisions and write the range review memo",
                       "You own the cereal aisle: you protect shoppers' choice and the category's profit.")
    t1 = make_task("Range scorecard (exact figures):\n{facts}\n\nFor each product explain its proposal in one line, "
                   "using profit per facing, transferable demand, out-of-stock rate and any unique need.",
                   "One line of evidence per SKU.", analyst)
    t2 = make_task("Range scorecard (exact figures; quote these, never recalculate):\n{facts}\n\n"
                   "Confirm or change each proposal and write the range review memo.",
                   "Memo from the Senior Buyer to the Category Director, with no date, signature or placeholder lines "
                   "like [Insert Name]: decision table (SKU, product, decision, reason), "
                   "how to use the facings_left_over (e.g. trial a new product or give best sellers more space), "
                   "the weekly profit at risk from delists, and talking points for the suppliers of delisted products.",
                   buyer, context=[t1])
    section("Range review memo", run_crew([analyst, buyer], [t1, t2], {"facts": json.dumps(facts, indent=2)}))


if __name__ == "__main__":
    main()
