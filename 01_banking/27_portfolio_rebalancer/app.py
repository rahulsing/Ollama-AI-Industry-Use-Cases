"""Portfolio Rebalancing Agent — LangChain tool-calling agent + Ollama.

Run:  python 01_banking/27_portfolio_rebalancer/app.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from langchain_core.tools import tool

from common import banner, run_agent, section

HOLDINGS = {  # ticker: (asset_class, units, price, cost_basis_per_unit, held_months)
    "VTI": ("US equity", 420, 285.0, 190.0, 40),
    "VXUS": ("Intl equity", 300, 64.0, 58.0, 30),
    "BND": ("Bonds", 260, 72.5, 78.0, 26),
    "VNQ": ("REITs", 90, 88.0, 92.0, 8),
    "CASH": ("Cash", 9000, 1.0, 1.0, 0),
}
TARGET = {"US equity": 45, "Intl equity": 20, "Bonds": 25, "REITs": 5, "Cash": 5}
BAND = 5  # rebalance if drift > 5pp


@tool
def current_allocation() -> dict:
    """Current market value and weight by asset class, with drift vs target (percentage points)."""
    values = {}
    for asset, units, price, *_ in HOLDINGS.values():
        values[asset] = values.get(asset, 0) + units * price
    total = sum(values.values())
    by_class = {a: {"value": round(v), "weight_pct": round(v / total * 100, 1), "target_pct": TARGET[a],
                    "drift_pp": round(v / total * 100 - TARGET[a], 1)} for a, v in values.items()}
    breach = any(abs(c["drift_pp"]) > BAND for c in by_class.values())
    return {"total_value": round(total), "by_class": by_class, "rebalance_needed": breach,
            "next_step": "Call rebalance_trades to get the exact trades." if breach else "No action needed."}


@tool
def rebalance_trades() -> list:
    """Trades (buy/sell amounts per ticker) to restore target weights, with estimated capital gain/loss on sells."""
    total = sum(u * p for _, u, p, *_ in HOLDINGS.values())
    trades = []
    for t, (asset, units, price, cost, months) in HOLDINGS.items():
        diff = TARGET[asset] / 100 * total - units * price
        if abs(diff) < 100 or t == "CASH":
            continue
        trade = {"ticker": t, "action": "BUY" if diff > 0 else "SELL", "amount": round(abs(diff)), "units": round(abs(diff) / price, 1)}
        if diff < 0:
            gain = (price - cost) * abs(diff) / price
            trade.update(est_gain=round(gain), term="long-term" if months >= 12 else "short-term")
        trades.append(trade)
    return trades


SYSTEM = (
    f"You are a portfolio manager. Rebalancing band is +/-{BAND}pp. Use current_allocation to check drift; if any class "
    "breaches the band, you MUST call rebalance_trades and present exactly those trades - never invent trade amounts "
    "or tax outcomes. Explain each trade, highlight tax impact using est_gain and term (prefer realising losses, avoid "
    "short-term gains), and suggest using cash/new contributions to reduce selling. End with a short client summary."
)


def main():
    banner("27 - Portfolio Rebalancing Agent (LangChain agent)")
    section("Recommendation", run_agent(SYSTEM, [current_allocation, rebalance_trades], "Review my portfolio and rebalance if needed."))


if __name__ == "__main__":
    main()
