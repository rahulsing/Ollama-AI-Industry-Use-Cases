"""Online Shopping Assistant — LangChain tool-calling agent + Ollama.

The agent searches the catalog, then checks store stock for click-and-collect and the delivery options.
It can only recommend what the tools return, so it never invents products, prices or stock.

Run:  python 02_retail/06_online_shopping_assistant/app.py
      python 02_retail/06_online_shopping_assistant/app.py "Do you have trail shoes in size 9 under 130?"
"""

import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from langchain_core.tools import tool

from common import banner, run_agent, section

CATALOG = {
    "RS-01": {"name": "Stridewell Stability 5", "price": 94.99, "rating": 4.6, "sizes": [8, 8.5, 9, 9.5, 10, 10.5, 11, 12],
              "tags": "running shoe road stability support flat feet overpronation"},
    "RS-02": {"name": "CloudLite Neutral Runner", "price": 79.99, "rating": 4.4, "sizes": [7, 8, 9, 10, 11],
              "tags": "running shoe road neutral cushioned lightweight high arches"},
    "RS-03": {"name": "TrailGrip Pro", "price": 119.99, "rating": 4.5, "sizes": [8, 9, 10, 11],
              "tags": "running shoe trail grip waterproof"},
    "RS-04": {"name": "Stridewell Stability 5 Wide", "price": 99.99, "rating": 4.5, "sizes": [9, 10, 11],
              "tags": "running shoe road stability support flat feet overpronation wide fit"},
    "RS-05": {"name": "ArchGuard Motion Control", "price": 109.99, "rating": 4.3, "sizes": [9, 10, 11, 12],
              "tags": "running shoe road motion control flat feet severe overpronation"},
    "AC-01": {"name": "ArchFit support insoles", "price": 24.99, "rating": 4.2, "sizes": [8, 9, 10, 11, 12],
              "tags": "insoles arch support flat feet running"},
}
# units on hand by store and size (normally a live inventory API)
STORE_STOCK = {
    "RS-01": {"Austin - South Congress": {10: 1, 11: 2}, "Austin - Domain": {9: 3}, "Dallas - Uptown": {10: 4}},
    "RS-04": {"Dallas - Uptown": {10: 2}},
    "AC-01": {"Austin - Domain": {10: 6}, "Austin - South Congress": {10: 3}},
}
WAREHOUSE = {"RS-01": {10: 25}, "RS-02": {10: 40}, "RS-04": {10: 8}, "RS-05": {10: 12}, "AC-01": {10: 60}}


@tool
def search_products(query: str, max_price: float = 0, size: float = 0) -> list:
    """Search the catalog by keywords (e.g. 'running shoes flat feet'). Optional max_price and shoe size filters."""
    words = set(re.findall(r"[a-z]+", query.lower())) - {"for", "and", "the", "with", "shoe", "shoes"}
    hits = []
    for sku, p in CATALOG.items():
        score = len(words & set((p["name"] + " " + p["tags"]).lower().split()))
        if score and (not max_price or p["price"] <= max_price) and (not size or size in p["sizes"]):
            hits.append((score, p["rating"], {"sku": sku, "name": p["name"], "price": p["price"],
                                              "rating": p["rating"], "suits": p["tags"]}))
    return [h[2] for h in sorted(hits, key=lambda h: (h[0], h[1]), reverse=True)] or ["no matching products"]


def delivery(sku: str, size: float) -> dict:
    """Home delivery options for a SKU and size from the online warehouse."""
    if not WAREHOUSE.get(sku, {}).get(size, 0):
        return {"home_delivery": "out of stock online"}
    return {"standard_delivery": "3-5 days, " + ("free" if CATALOG[sku]["price"] >= 50 else "4.99"),
            "express_delivery": "next day if ordered before 8pm, 7.99"}


@tool
def check_availability(sku: str, size: float, city: str) -> dict:
    """Click-and-collect stock at each store in a city today, plus home delivery options, for a SKU and size."""
    if sku not in CATALOG:  # small models sometimes invent codes: send them back to the search results
        return {"error": f"Unknown SKU {sku!r}. Use a sku exactly as returned by search_products, e.g. 'RS-01'."}
    stores = {store: sizes.get(size, 0) for store, sizes in STORE_STOCK.get(sku, {}).items()
              if store.lower().startswith(city.lower())}
    ready = [s for s, units in stores.items() if units > 0]
    return {"sku": sku, "size": size, "units_by_store": stores or f"no stores in {city} stock it",
            "collect_today": f"ready in 1 hour at {', '.join(ready)}" if ready else "not available to collect today",
            **delivery(sku, size)}


SYSTEM = (
    "You are a friendly online shopping assistant for a sports retailer. Work in two steps. Step 1: call "
    "search_products on its own and wait for the results. Step 2: call check_availability for each of the top 3 "
    "results, using the sku values exactly as search_products returned them. Then answer. Only mention products you "
    "checked in step 2, with the prices, stock and delivery options the tools returned. For each give the price, why "
    "it suits the customer, and whether they can collect today or get delivery. If something is over budget, say so. Don't "
    "give medical advice: for foot pain suggest the free in-store gait analysis."
)


def main():
    banner("Retail 06 - Online Shopping Assistant (LangChain agent)")
    q = sys.argv[1] if len(sys.argv) > 1 else (
        "I need running shoes for flat feet, size 10, under 100. Can I pick them up in Austin today?")
    section("Question", q)
    section("Answer", run_agent(SYSTEM, [search_products, check_availability], q))


if __name__ == "__main__":
    main()
