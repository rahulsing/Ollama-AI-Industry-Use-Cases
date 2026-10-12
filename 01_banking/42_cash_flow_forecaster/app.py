"""Corporate Cash Flow Forecaster — LangChain tool-calling agent + Ollama.

Run:  python 01_banking/42_cash_flow_forecaster/app.py
"""

import statistics
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from langchain_core.tools import tool

from common import banner, run_agent, section

OPENING_CASH = 1_200_000
OVERDRAFT_LIMIT = 500_000
# last 12 weeks of history (thousands)
INFLOWS = [820, 760, 910, 700, 880, 790, 640, 610, 590, 650, 600, 580]
OUTFLOWS = [780, 800, 820, 760, 850, 900, 780, 720, 750, 690, 740, 760]
KNOWN_EVENTS = {5: ("Payroll bonus", -450), 9: ("Tax payment", -380), 11: ("Large customer receipt", 300)}  # week: (desc, k)


@tool
def forecast_cash(weeks: int = 13) -> list:
    """13-week cash forecast (thousands) using recent trend plus known events; returns week, net flow, closing cash."""
    trend_in = statistics.mean(INFLOWS[-4:])
    trend_out = statistics.mean(OUTFLOWS[-4:])
    cash, rows = OPENING_CASH / 1000, []
    for w in range(1, weeks + 1):
        event = KNOWN_EVENTS.get(w, ("", 0))
        net = trend_in - trend_out + event[1]
        cash += net
        rows.append({"week": w, "net_flow": round(net), "closing_cash": round(cash), "event": event[0]})
    return rows


@tool
def funding_gap() -> dict:
    """Identify the lowest projected cash point and whether the overdraft limit covers it."""
    rows = forecast_cash.invoke({"weeks": 13})
    low = min(rows, key=lambda r: r["closing_cash"])
    headroom = low["closing_cash"] + OVERDRAFT_LIMIT / 1000
    return {"lowest_week": low["week"], "lowest_cash_k": low["closing_cash"], "overdraft_limit_k": OVERDRAFT_LIMIT / 1000,
            "headroom_k": round(headroom), "breach": headroom < 0}


SYSTEM = (
    "You are a corporate banking treasury advisor. Use forecast_cash and funding_gap. Report: trend of inflows vs "
    "outflows, the week cash turns negative (if any), funding gap vs overdraft, and recommend actions (working capital "
    "line, invoice discounting, payables timing, sweeping surplus). Figures are in thousands."
)


def main():
    banner("42 - Corporate Cash Flow Forecaster (LangChain agent)")
    section("Treasury view", run_agent(SYSTEM, [forecast_cash, funding_gap], "Give me the 13-week cash outlook and any funding needs."))


if __name__ == "__main__":
    main()
