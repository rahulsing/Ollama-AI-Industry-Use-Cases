"""Motor Insurance Quote Agent — LangChain tool-calling agent + Ollama.

A simplified rating engine (base rate x factors) that the agent explains and uses for what-ifs.

Run:  python 03_insurance/03_motor_quote_agent/app.py
      python 03_insurance/03_motor_quote_agent/app.py "I'm 24, licensed 3 years, group 18 car, no claims. Quote?"
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from langchain_core.tools import tool

from common import banner, run_agent, section

BASE_PREMIUM = 420.0
EXCESS_FACTORS = {0: 1.0, 250: 0.95, 500: 0.9, 1000: 0.85}  # higher voluntary excess = lower premium


def age_factor(age: int) -> float:
    return 2.2 if age < 21 else 1.6 if age < 25 else 1.0 if age < 70 else 1.3


@tool
def rate_quote(driver_age: int, years_licensed: int, vehicle_group: int, area_risk: str = "medium",
               claims_last_5y: int = 0, annual_mileage: int = 8000, voluntary_excess: int = 0) -> dict:
    """Price a motor insurance policy and return the premium with a factor-by-factor breakdown.
    vehicle_group: 1 (cheap, low power) to 50 (high performance). area_risk: low, medium or high.
    voluntary_excess: optional extra excess the customer chooses (0, 250, 500 or 1000); leave at 0 unless asked."""
    factors = {
        "driver_age": age_factor(driver_age),
        "experience": 1.4 if years_licensed < 2 else 1.15 if years_licensed < 5 else 1.0,
        "vehicle_group": round(0.7 + vehicle_group / 50 * 1.3, 2),
        "area": {"low": 0.85, "medium": 1.0, "high": 1.35}[area_risk],
        "claims_history": round(1 + 0.25 * claims_last_5y, 2),
        "mileage": 0.9 if annual_mileage < 5000 else 1.0 if annual_mileage <= 12000 else 1.2,
        "voluntary_excess": EXCESS_FACTORS.get(voluntary_excess, 1.0),
    }
    premium = BASE_PREMIUM
    for f in factors.values():
        premium *= f
    without_excess = premium / factors["voluntary_excess"]
    excess_options = {f"voluntary_excess_{x}": {"annual_premium": round(without_excess * f, 2),
                                                "annual_saving_vs_0": round(without_excess * (1 - f), 2)}
                      for x, f in EXCESS_FACTORS.items()}
    return {"annual_premium": round(premium, 2), "monthly_premium": round(premium * 1.05 / 12, 2),
            "base_premium": BASE_PREMIUM, "factors": factors,
            "biggest_driver": max(factors, key=lambda k: factors[k]), "excess_options": excess_options}


SYSTEM = (
    "You are a friendly motor insurance quote assistant. Use rate_quote for every price; copy the numbers exactly. "
    "Explain the premium in plain language using the factor breakdown (what pushes it up or down). For voluntary "
    "excess questions, quote excess_options exactly. For other what-ifs call rate_quote again with the changed "
    "inputs and state the difference. Monthly price includes a "
    "5% instalment charge. This is an indicative quote, subject to underwriting."
)


def main():
    banner("Insurance 03 - Motor Insurance Quote Agent (LangChain agent)")
    q = sys.argv[1] if len(sys.argv) > 1 else (
        "I'm 23, licensed 2 years, driving a group 22 car in a high-risk area, 1 claim in 5 years, 9,000 miles a year. "
        "What's my quote, and how much would I save with a 500 voluntary excess?")
    section("Customer", q)
    section("Quote", run_agent(SYSTEM, [rate_quote], q))


if __name__ == "__main__":
    main()
