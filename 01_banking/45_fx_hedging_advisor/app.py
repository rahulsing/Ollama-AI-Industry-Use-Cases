"""FX Hedging Advisor — LangChain tool-calling agent + Ollama.

Run:  python 01_banking/45_fx_hedging_advisor/app.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from langchain_core.tools import tool

from common import banner, run_agent, section

# Corporate client (home currency INR): foreign currency cash flows over next 6 months
EXPOSURES = [
    {"currency": "USD", "type": "receivable", "amount": 2_000_000, "months": 3},
    {"currency": "USD", "type": "payable", "amount": 800_000, "months": 3},
    {"currency": "EUR", "type": "payable", "amount": 1_200_000, "months": 6},
]
SPOT = {"USD": 84.20, "EUR": 91.50}
RATES = {"INR": 6.5, "USD": 4.25, "EUR": 2.5}  # annual interest rates %
VOL = {"USD": 4.5, "EUR": 6.5}  # annualised volatility %


@tool
def net_exposure() -> dict:
    """Net foreign-currency exposure per currency and tenor (positive = net long / receivable)."""
    out = {}
    for e in EXPOSURES:
        key = f"{e['currency']}_{e['months']}m"
        out[key] = out.get(key, 0) + (e["amount"] if e["type"] == "receivable" else -e["amount"])
    return out


@tool
def forward_rate(currency: str, months: int) -> str:
    """Forward rate (INR per unit) via covered interest parity, plus a 1-sigma move range for the unhedged spot."""
    s, t = SPOT[currency], months / 12
    fwd = s * (1 + RATES["INR"] / 100 * t) / (1 + RATES[currency] / 100 * t)
    sigma = s * VOL[currency] / 100 * t ** 0.5
    return f"{currency} {months}m forward: {fwd:.2f} (spot {s}); 1-sigma spot range at maturity {s - sigma:.2f} - {s + sigma:.2f}"


SYSTEM = (
    "You are an FX sales advisor at a bank for a corporate client whose home currency is INR. The client's exposures "
    "are already in the system: never ask the user for data. Always start by calling net_exposure, then call "
    "forward_rate for each net exposure. Explain the risk of being unhedged in INR terms (use the 1-sigma range), and "
    "recommend a hedge ratio and instrument (forward vs option) for each exposure, noting natural hedges. "
    "Remind that hedging is for risk management, not speculation."
)


def main():
    banner("45 - FX Hedging Advisor (LangChain agent)")
    section("Advice", run_agent(SYSTEM, [net_exposure, forward_rate], "Analyse our FX exposures and recommend a hedging plan."))


if __name__ == "__main__":
    main()
