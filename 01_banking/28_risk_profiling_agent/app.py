"""Investor Risk Profiling Agent — LangChain chain + Ollama.

Run:  python 01_banking/28_risk_profiling_agent/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, run_chain, section

QUESTIONS = [  # (question, {answer: points})
    ("Investment horizon", {"<3 years": 1, "3-7 years": 3, ">7 years": 5}),
    ("Reaction to a 20% portfolio fall", {"Sell everything": 1, "Sell some": 2, "Hold": 4, "Buy more": 5}),
    ("Primary objective", {"Capital preservation": 1, "Income": 2, "Balanced growth": 3, "Maximum growth": 5}),
    ("Investment experience", {"None": 1, "Deposits only": 2, "Mutual funds": 4, "Stocks & derivatives": 5}),
    ("Share of savings being invested", {">75%": 1, "50-75%": 2, "25-50%": 4, "<25%": 5}),
    ("Income stability", {"Unstable": 1, "Somewhat stable": 3, "Very stable": 5}),
]

ANSWERS = {
    "Investment horizon": ">7 years",
    "Reaction to a 20% portfolio fall": "Sell everything",
    "Primary objective": "Maximum growth",
    "Investment experience": "Deposits only",
    "Share of savings being invested": ">75%",
    "Income stability": "Very stable",
}


def score(answers: dict) -> dict:
    pts = {q: opts[answers[q]] for q, opts in QUESTIONS}
    total = sum(pts.values())
    pct = round((total - len(QUESTIONS)) / (len(QUESTIONS) * 4) * 100)
    profile = "Conservative" if pct < 30 else "Moderately conservative" if pct < 50 else "Moderate" if pct < 70 else "Aggressive"
    # Inconsistency check: wants growth but cannot tolerate losses
    flags = []
    if pts["Primary objective"] >= 5 and pts["Reaction to a 20% portfolio fall"] <= 1:
        flags.append("Wants maximum growth but would sell everything after a 20% fall")
    if pts["Investment experience"] <= 2 and pts["Primary objective"] >= 5:
        flags.append("Aggressive objective with limited investment experience")
    return {"points": pts, "score_pct": pct, "profile": profile, "inconsistencies": flags}


SYSTEM = (
    "You are a wealth relationship manager. Explain the client's risk profile in plain, friendly language "
    "(max 150 words). If there are inconsistencies, explain them gently, recommend the more cautious profile until "
    "discussed, and list 3 follow-up questions to ask the client."
)


def main():
    banner("28 - Investor Risk Profiling Agent (LangChain)")
    result = score(ANSWERS)
    section("Score", json.dumps(result, indent=2))
    section("Client explanation", run_chain(SYSTEM, "Answers:\n{a}\n\nResult:\n{r}",
                                            a=json.dumps(ANSWERS, indent=2), r=json.dumps(result, indent=2)))


if __name__ == "__main__":
    main()
