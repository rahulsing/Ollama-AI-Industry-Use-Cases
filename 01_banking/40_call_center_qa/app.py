"""Call Center QA Analyzer — CrewAI + Ollama.

Run:  python 01_banking/40_call_center_qa/app.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

TRANSCRIPT = """
Agent: Thanks for calling City Bank, this is Sam. How can I help?
Customer: Hi, there's a charge of 250 on my credit card I don't recognise. It says 'XYZ Digital'.
Agent: Okay. Can you give me your full card number and the CVV so I can check?
Customer: Um, sure, it's 4111... wait, do you need the CVV?
Agent: Yeah it's fine, it's just for verification.
Customer: I'd rather not.
Agent: Fine. I'll verify you another way. Date of birth and postcode please.
Customer: 12 March 1984, LS1 4AB.
Agent: Thanks. Yes I see it. It's probably a subscription you forgot. Not much I can do really.
Customer: I never signed up for anything! I'm really worried.
Agent: Well, you can raise a dispute but it takes ages. Anything else?
Customer: Can you at least block the card?
Agent: Okay, blocked. New card in 5 days. Bye.
"""

CHECKLIST = """
1. Greeting & identification of agent (5)
2. Secure verification - must NEVER ask for full card number, CVV, PIN or OTP (25, critical)
3. Listening & empathy (15)
4. Correct handling of suspected fraud: offer block, raise dispute/fraud claim, explain next steps & timelines (25)
5. Accurate information, no assumptions (10)
6. Ownership & resolution (10)
7. Closing: summary, reference number, anything else (10)
"""


def main():
    banner("40 - Call Center QA Analyzer (CrewAI)")
    auditor = make_agent("QA Auditor", "Score the call objectively against the QA checklist",
                         "Contact-centre quality lead in a regulated bank. A critical fail on security means the call fails overall.")
    coach = make_agent("Team Coach", "Turn QA results into constructive, specific coaching",
                       "Supportive coach who gives specific 'say this instead' examples.")
    t1 = make_task("Transcript:\n{transcript}\n\nChecklist (max points):\n{checklist}\n\nScore each item with evidence quotes.",
                   "Score table with evidence, total /100, critical fails, overall PASS/FAIL.", auditor)
    t2 = make_task("Write coaching feedback for the agent.",
                   "Strengths, top 3 improvements with better phrasing examples, and any compliance escalation needed.",
                   coach, context=[t1])
    section("QA report", run_crew([auditor, coach], [t1, t2], {"transcript": TRANSCRIPT, "checklist": CHECKLIST}))


if __name__ == "__main__":
    main()
