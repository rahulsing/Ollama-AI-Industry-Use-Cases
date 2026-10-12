"""SAR Narrative Generator — CrewAI + Ollama.

Run:  python 01_banking/12_sar_narrative_generator/app.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

CASE_FACTS = """
Case ID: INV-2026-0912     Subject: Daniel Okafor (DOB 1985-02-14), personal current account opened 2026-05-03
Stated occupation: Freelance graphic designer, expected monthly income ~4,000.
Activity reviewed: 2026-07-01 to 2026-09-30.
- 46 incoming P2P transfers from 31 unrelated individuals, values 300-1,900, total 41,250.
  Payment references include 'loan', 'gift', 'crypto', 'invest'.
- Within 24 hours of receipt, 92% of funds sent to two crypto exchanges (CoinPeak, BitHarbor), total 37,950.
- 4 incoming payments recalled by sending banks as authorised push payment (APP) fraud victims.
- Login IP addresses from 3 countries in the same week; device changed 5 times.
- Customer did not respond to two requests for information (sent 2026-09-10 and 2026-09-20).
Actions taken: account restricted 2026-09-25.
"""


def main():
    banner("12 - SAR Narrative Generator (CrewAI)")
    analyst = make_agent("Financial Crime Case Analyst", "Turn raw case facts into a clear chronology and typology assessment",
                         "You prepare cases for SAR filing and are meticulous about dates, amounts and sources.")
    writer = make_agent("SAR Narrative Writer", "Write a regulator-ready SAR narrative",
                        "You write SAR narratives that are factual, objective, chronological and answer who/what/when/where/why/how.")
    t1 = make_task("Case facts:\n{facts}\n\nBuild a chronology and identify typologies and red flags.",
                   "Chronology table, typology (e.g. money mule, APP fraud proceeds) and red-flag list.", analyst)
    t2 = make_task(
        "Write the SAR narrative using the analysis. Do not speculate beyond the facts; avoid accusatory language.",
        "SAR narrative with paragraphs: Introduction (summary & amount), Subject information, Suspicious activity "
        "(chronological), Red flags & typology, Actions taken, Conclusion.", writer, context=[t1])
    section("SAR narrative", run_crew([analyst, writer], [t1, t2], {"facts": CASE_FACTS}))


if __name__ == "__main__":
    main()
