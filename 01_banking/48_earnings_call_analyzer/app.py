"""Earnings Call Analyzer — CrewAI + Ollama.

Run:  python 01_banking/48_earnings_call_analyzer/app.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

TRANSCRIPT = """(Fictional Q3 FY26 earnings call - Meridian Bank)
CEO: We delivered a solid quarter. Loan growth was 14% year on year, led by retail mortgages and SME. Net interest
margin compressed by 12 basis points to 3.42% as deposit costs caught up, but we expect margins to stabilise next
quarter as rate cuts flow through to our deposit book.
CFO: Operating expenses grew 11%, mainly technology and branch expansion. Cost-to-income is 46.8%. Credit costs rose to
68 bps from 52 bps, driven by unsecured personal loans and credit cards where we've seen early delinquency tick up.
We've tightened underwriting in that segment. Gross NPA is 2.1%, up 15 bps. Provision coverage is 72%. CET1 is 13.4%.
We maintain FY guidance of 13-15% loan growth and a return on assets of 1.3-1.4%, though we now see the lower end as more likely.
Analyst 1: Can you quantify the unsecured stress? Is it spreading to other segments?
CFO: Unsecured is 9% of the book. We're not seeing spillover to mortgages or SME; those remain very clean.
Analyst 2: Deposit growth was 9% versus loans at 14%. How will you fund growth?
CEO: The LDR is at 88%. We'll lean on granular retail deposits, and may moderate loan growth if deposits lag. We won't chase
expensive bulk deposits.
"""


def main():
    banner("48 - Earnings Call Analyzer (CrewAI)")
    analyst = make_agent("Transcript Analyst", "Extract key financial metrics, guidance changes and management commitments",
                         "Bank equity research analyst who catches subtle guidance changes.")
    sentiment = make_agent("Sentiment & Risk Analyst", "Assess management tone and highlight risks and evasive answers",
                           "You read between the lines of management commentary and analyst Q&A.")
    t1 = make_task("Transcript:\n{transcript}\n\nExtract: KPIs table, guidance (maintained/raised/lowered/softened), key themes.",
                   "KPI table, guidance status, themes.", analyst)
    t2 = make_task("Assess tone (score -5 to +5 with reasons), hedging language, risks, and what to watch next quarter.",
                   "Investor note: Tone score, Top 3 positives, Top 3 risks, Watch-list, One-line takeaway.", sentiment, context=[t1])
    section("Earnings call note", run_crew([analyst, sentiment], [t1, t2], {"transcript": TRANSCRIPT}))


if __name__ == "__main__":
    main()
