"""Basel III Capital Calculator Assistant — LangChain tool-calling agent + Ollama.

Simplified standardised-approach risk weights for illustration.

Run:  python 01_banking/19_basel_capital_calculator/app.py
      python 01_banking/19_basel_capital_calculator/app.py "What if corporate exposures grow by 2,000?"
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from langchain_core.tools import tool

from common import banner, run_agent, section

EXPOSURES = {  # millions
    "sovereign_AAA": 8_000, "banks_A": 2_500, "corporate_unrated": 14_000, "corporate_BBB": 6_000,
    "retail": 9_000, "residential_mortgage": 12_000, "commercial_real_estate": 3_000, "past_due": 800,
}
RISK_WEIGHTS = {"sovereign_AAA": 0.0, "banks_A": 0.5, "corporate_unrated": 1.0, "corporate_BBB": 1.0,
                "retail": 0.75, "residential_mortgage": 0.35, "commercial_real_estate": 1.0, "past_due": 1.5}
CAPITAL = {"cet1": 3_900, "at1": 500, "tier2": 700}
OTHER_RWA = {"market": 1_800, "operational": 3_400}
MIN = {"cet1": 4.5 + 2.5, "tier1": 6.0 + 2.5, "total": 8.0 + 2.5}  # incl. conservation buffer


@tool
def compute_rwa(extra_exposure_class: str = "", extra_amount: float = 0) -> dict:
    """Compute credit RWA by exposure class and total RWA. Optionally add a hypothetical extra exposure
    (exposure class name and amount in millions) for what-if analysis."""
    exp = dict(EXPOSURES)
    if extra_exposure_class in exp:
        exp[extra_exposure_class] += extra_amount
    credit = {k: v * RISK_WEIGHTS[k] for k, v in exp.items()}
    total = sum(credit.values()) + sum(OTHER_RWA.values())
    return {"credit_rwa_by_class": credit, "market_rwa": OTHER_RWA["market"],
            "operational_rwa": OTHER_RWA["operational"], "total_rwa": total}


@tool
def capital_ratios(total_rwa: float) -> dict:
    """Compute CET1, Tier 1 and Total capital ratios (%) for a given total RWA, with minimums incl. buffers."""
    t1 = CAPITAL["cet1"] + CAPITAL["at1"]
    r = {"cet1": CAPITAL["cet1"] / total_rwa * 100, "tier1": t1 / total_rwa * 100,
         "total": (t1 + CAPITAL["tier2"]) / total_rwa * 100}
    return {k: {"ratio_pct": round(v, 2), "minimum_pct": MIN[k], "headroom_pp": round(v - MIN[k], 2)} for k, v in r.items()}


SYSTEM = (
    "You are a capital management analyst. Always call compute_rwa first, then capital_ratios with its total_rwa. "
    "Exposure classes: " + ", ".join(EXPOSURES) + ". Present ratios in a table, comment on headroom and the "
    "largest RWA drivers, and suggest RWA optimisation ideas if headroom is under 2pp."
)


def main():
    banner("19 - Basel III Capital Calculator (LangChain agent)")
    q = sys.argv[1] if len(sys.argv) > 1 else (
        "What are our current capital ratios? Then: what happens if unrated corporate exposure grows by 3,000 million?")
    section("Question", q)
    section("Answer", run_agent(SYSTEM, [compute_rwa, capital_ratios], q))


if __name__ == "__main__":
    main()
