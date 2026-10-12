"""Market News Briefing for RMs — CrewAI + Ollama.

Run:  python 01_banking/29_market_news_summarizer/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

NEWS = """(Sample headlines - replace with your news feed)
1. Central bank holds policy rate at 6.25%, signals one more cut this year as inflation eases to 3.9%.
2. Crude oil jumps 6% on supply disruption fears; airline and paint stocks fall.
3. IT services majors guide flat revenue growth; US clients delay discretionary spend.
4. Government announces 15% capital subsidy for semiconductor manufacturing.
5. 10-year government bond yield falls 12 bps to 6.48% after rate guidance.
6. Gold hits record high on safe-haven demand.
"""

CLIENTS = {
    "Mr. Kapoor (Retired, conservative)": {"Long-duration gilt fund": 40, "Bank FDs": 30, "Large-cap fund": 20, "Gold ETF": 10},
    "Ms. Rao (Tech founder, aggressive)": {"IT services stocks": 45, "Small-cap fund": 25, "Semiconductor theme fund": 20, "Cash": 10},
    "Sharma Family Office (balanced)": {"Aviation stocks": 15, "Nifty index fund": 40, "Corporate bond fund": 30, "Paint & chemicals stocks": 15},
}


def main():
    banner("29 - Market News Briefing for RMs (CrewAI)")
    analyst = make_agent("Market Analyst", "Distil market news into themes and asset-class impacts",
                         "Sell-side strategist who explains what news means for equities, bonds, commodities.")
    briefer = make_agent("RM Briefing Specialist", "Turn market themes into client-specific talking points",
                         "Former private banker; you make RMs sound informed and compliant (no guarantees, no tips).")
    t1 = make_task("News:\n{news}\n\nSummarise into 3-5 themes with likely impact (positive/negative/neutral) on asset classes and sectors.",
                   "Theme list with asset-class/sector impacts.", analyst)
    t2 = make_task("Client holdings (% weights):\n{clients}\n\nFor each client: impact on their holdings, 2-3 talking points, and "
                   "whether a proactive call is warranted today.", "Per-client briefing.", briefer, context=[t1])
    section("RM morning briefing", run_crew([analyst, briefer], [t1, t2], {"news": NEWS, "clients": json.dumps(CLIENTS, indent=2)}))


if __name__ == "__main__":
    main()
