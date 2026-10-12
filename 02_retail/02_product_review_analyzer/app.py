"""Product Review Analyzer — LangChain structured output + Ollama.

Run:  python 02_retail/02_product_review_analyzer/app.py
"""

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Literal

sys.path.append(str(Path(__file__).resolve().parents[2]))
from pydantic import BaseModel, Field

from common import banner, run_chain, run_structured, section

PRODUCT = "AeroBlend 600W Personal Blender"
REVIEWS = [
    (5, "Makes smoothies in 30 seconds and is easy to clean. Love it!"),
    (2, "Lid started leaking after two weeks. Juice everywhere on my counter."),
    (4, "Powerful for the size, but quite loud early in the morning."),
    (1, "Motor burned out after a month. Smelled of burning plastic. Very disappointed."),
    (3, "Does the job but the cup is smaller than the photos suggest."),
    (2, "Leaks from the bottom seal every time I blend ice."),
    (5, "Great value, delivery was fast and it crushes ice well."),
    (1, "Blade assembly cracked; I'm worried about plastic bits in my drink."),
]


class Review(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]
    themes: list[Literal["performance", "leaking", "durability", "noise", "size", "cleaning", "value",
                         "delivery"]] = Field(description="Only the themes the review actually talks about")
    product_defect: bool = Field(description="True if the review describes a product fault, not just a preference")
    safety_concern: bool = Field(description="True for burning smells, cracked blades, overheating, injury risk")


SYSTEM = (
    "You are a retail product quality analyst. Write a short report for the product and quality teams: overall "
    "sentiment, top complaint themes with counts, any SAFETY issues that need urgent escalation (possible recall "
    "review), and 3 concrete actions (supplier quality check, listing description fix, customer replies). "
    "Use only the counts provided."
)


def main():
    banner("Retail 02 - Product Review Analyzer (LangChain structured output)")
    rows = []
    for stars, text in REVIEWS:
        r = run_structured("Classify this product review accurately.", text, Review)
        rows.append({"stars": stars, "text": text, **r.model_dump()})
        section(f"{stars}★ {text[:60]}", r.model_dump())

    summary = {
        "product": PRODUCT,
        "reviews": len(rows),
        "avg_stars": round(sum(r["stars"] for r in rows) / len(rows), 2),
        "sentiment": dict(Counter(r["sentiment"] for r in rows)),
        "theme_counts": dict(Counter(t for r in rows for t in r["themes"]).most_common()),
        "defect_reviews": sum(r["product_defect"] for r in rows),
        "safety_reviews": [r["text"] for r in rows if r["safety_concern"]],
    }
    section("Summary", json.dumps(summary, indent=2, ensure_ascii=False))
    section("Quality report", run_chain(SYSTEM, "Summary:\n{s}", s=json.dumps(summary, indent=2, ensure_ascii=False)))


if __name__ == "__main__":
    main()
