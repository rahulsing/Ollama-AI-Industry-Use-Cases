"""Promotion Performance Analyzer — LangChain chain + Ollama.

Python measures each promotion's true incremental profit (after the post-promo dip, cannibalisation and
marketing spend); the LLM writes the post-promotion review.

Run:  python 02_retail/04_promotion_performance_analyzer/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, run_chain, section

# One-week promotions from last month. baseline = normal weekly units (4-week average before the promo)
PROMOS = [
    {"id": "PR-01", "product": "Coffee beans 1kg", "mechanic": "25% off", "price": 18.00, "promo_price": 13.50,
     "unit_cost": 10.00, "supplier_funding_per_unit": 1.50, "baseline_units": 120, "promo_units": 410,
     "post_weeks": 2, "post_units": 150, "cannibalised": {"product": "Coffee beans 500g", "units": 60, "unit_margin": 3.20},
     "marketing_spend": 800},
    {"id": "PR-02", "product": "Pasta sauce 500g", "mechanic": "2 for 5.00", "price": 3.20, "promo_price": 2.50,
     "unit_cost": 1.60, "supplier_funding_per_unit": 0.40, "baseline_units": 300, "promo_units": 900,
     "post_weeks": 2, "post_units": 560, "cannibalised": {"product": "Own-brand pasta sauce", "units": 90, "unit_margin": 0.90},
     "marketing_spend": 300},
    {"id": "PR-03", "product": "Kitchen towels 4-pack", "mechanic": "10% off", "price": 6.00, "promo_price": 5.40,
     "unit_cost": 3.50, "supplier_funding_per_unit": 0.00, "baseline_units": 200, "promo_units": 230,
     "post_weeks": 2, "post_units": 400, "cannibalised": None, "marketing_spend": 250},
]


def evaluate(p: dict) -> dict:
    """Incremental profit = promo-week profit - normal profit - post-promo dip - cannibalisation - marketing."""
    normal_margin = p["price"] - p["unit_cost"]
    promo_margin = p["promo_price"] - p["unit_cost"] + p["supplier_funding_per_unit"]
    uplift = p["promo_units"] / p["baseline_units"] - 1
    baseline_profit = p["baseline_units"] * normal_margin
    promo_profit = p["promo_units"] * promo_margin
    dip_units = max(p["baseline_units"] * p["post_weeks"] - p["post_units"], 0)  # customers stocked up
    dip_loss = dip_units * normal_margin
    c = p["cannibalised"]
    cannibal_loss = c["units"] * c["unit_margin"] if c else 0
    net = promo_profit - baseline_profit - dip_loss - cannibal_loss - p["marketing_spend"]
    drags = {"post-promotion dip": dip_loss, "cannibalisation": cannibal_loss, "marketing spend": p["marketing_spend"]}
    biggest = max(drags, key=drags.get)
    if net > 0:
        verdict = "REPEAT"
    elif uplift >= 1.0:
        verdict = "REWORK"   # strong traffic driver, but the economics don't work yet
    else:
        verdict = "DROP"     # too shallow to move volume
    return {"id": p["id"], "product": p["product"], "mechanic": p["mechanic"],
            "volume_uplift_pct": round(uplift * 100), "promo_week_profit": round(promo_profit),
            "normal_week_profit": round(baseline_profit), "post_promo_dip_units": dip_units,
            "post_promo_dip_loss": round(dip_loss), "cannibalisation_loss": round(cannibal_loss),
            "cannibalised_product": c["product"] if c else None, "marketing_spend": p["marketing_spend"],
            "incremental_profit": round(net), "biggest_drag_on_profit": f"{biggest} ({round(drags[biggest])})",
            "verdict": verdict,
            "extra_supplier_funding_per_unit_to_break_even": round(-net / p["promo_units"], 2) if verdict == "REWORK" else None}


SYSTEM = (
    "You are a retail promotions analyst writing a post-promotion review for the category manager. Use ONLY the "
    "figures given; never recalculate. Every figure is money (profit or cost) except volume_uplift_pct and the "
    "fields ending in _units. For each promotion state the verdict (REPEAT / REWORK / DROP), the incremental "
    "profit and biggest_drag_on_profit. For REWORK, suggest fixes: shallower discount, more supplier funding "
    "(quote extra_supplier_funding_per_unit_to_break_even), or a different mechanic. End with 3 lessons drawn from "
    "these results for next quarter's promotion calendar. Keep it under 300 words."
)


def main():
    banner("Retail 04 - Promotion Performance Analyzer (LangChain chain)")
    results = [evaluate(p) for p in PROMOS]
    section("Incremental profit by promotion", json.dumps(results, indent=2))
    section("Post-promotion review", run_chain(SYSTEM, "Promotion results:\n{r}", r=json.dumps(results, indent=2)))


if __name__ == "__main__":
    main()
