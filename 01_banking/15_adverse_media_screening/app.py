"""Adverse Media Screening — LangChain structured output + Ollama.

Run:  python 01_banking/15_adverse_media_screening/app.py
"""

import sys
from pathlib import Path
from typing import Literal

sys.path.append(str(Path(__file__).resolve().parents[2]))
from pydantic import BaseModel, Field

from common import banner, run_structured, section

SUBJECT = "Rajiv Malhotra, MD of Horizon Infra Projects"

ARTICLES = [  # fictional headlines/snippets
    "Horizon Infra Projects wins 2,400 crore highway contract; MD Rajiv Malhotra says execution starts Q1.",
    "Enforcement agency raids Horizon Infra offices in money laundering probe linked to bid-rigging; "
    "MD Rajiv Malhotra questioned for 9 hours, no charges filed yet.",
    "Rajiv Malhotra, a Mumbai-based chef, opens new restaurant in Bandra.",
    "Court grants bail to Horizon Infra MD Rajiv Malhotra after arrest on bribery charges involving state officials.",
]


class MediaAssessment(BaseModel):
    summary: str = Field(description="One-sentence summary of the article")
    about_subject: bool = Field(description="True if the article names the subject person or their company "
                                            "(same name + same company/role). False for a different person with the same name.")
    category: Literal["none", "fraud", "bribery_corruption", "money_laundering", "sanctions", "tax_evasion",
                      "terrorism", "organised_crime", "other_financial_crime"] = Field(
        description="'none' only for positive/neutral news; arrests, raids, probes and charges are never 'none'")
    severity: Literal["none", "low", "medium", "high"] = Field(description="'none' if category is 'none'")
    status: Literal["n/a", "allegation", "investigation", "charged", "convicted", "acquitted"] = Field(
        description="'n/a' if category is 'none'; 'charged' covers arrests and bail")


def main():
    banner("15 - Adverse Media Screening (LangChain structured output)")
    system = (f"You screen news for financial-crime adverse media about: {SUBJECT}. "
              "First summarise the article, then decide whether it is about the subject, then classify. "
              "Positive or neutral business news is category 'none'. A different person with the same name "
              "(e.g. a different job or company) is not about the subject.")
    results = []
    for i, art in enumerate(ARTICLES, 1):
        a = run_structured(system, art, MediaAssessment)
        results.append(a)
        section(f"Article {i}", f"{art}\n-> {a.model_dump()}")

    relevant = [r for r in results if r.about_subject and r.category != "none"]
    worst = max((r.severity for r in relevant), key=["none", "low", "medium", "high"].index, default="none")
    section("Overall", f"{len(relevant)} relevant adverse articles; highest severity: {worst.upper()} "
                       f"-> {'Escalate for EDD' if worst in ('medium', 'high') else 'No action'}")


if __name__ == "__main__":
    main()
