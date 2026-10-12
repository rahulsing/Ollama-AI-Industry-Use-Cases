"""Early Warning Signals (EWS) Monitor — LangChain chain + Ollama.

Run:  python 01_banking/06_early_warning_signals/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, run_chain, section

BORROWERS = [
    {"name": "Apex Textiles", "exposure": 45_000_000, "od_limit_breach_days_90d": 18, "cheque_returns_90d": 3,
     "rating_change": "BBB -> BB", "financials_overdue_days": 60, "gst_turnover_change_pct": -28, "promoter_pledge_pct": 45},
    {"name": "Nova Logistics", "exposure": 30_000_000, "od_limit_breach_days_90d": 0, "cheque_returns_90d": 0,
     "rating_change": "A (stable)", "financials_overdue_days": 0, "gst_turnover_change_pct": 12, "promoter_pledge_pct": 0},
    {"name": "Sunrise Builders", "exposure": 80_000_000, "od_limit_breach_days_90d": 7, "cheque_returns_90d": 1,
     "rating_change": "BBB (negative watch)", "financials_overdue_days": 30, "gst_turnover_change_pct": -9, "promoter_pledge_pct": 20},
]

RULES = [
    ("od_limit_breach_days_90d", lambda v: v > 10, "Persistent overdraft limit breaches"),
    ("cheque_returns_90d", lambda v: v >= 2, "Repeated cheque returns"),
    ("rating_change", lambda v: "->" in v or "negative" in v, "External rating downgrade / negative outlook"),
    ("financials_overdue_days", lambda v: v >= 30, "Delay in submitting financials"),
    ("gst_turnover_change_pct", lambda v: v < -15, "Sharp fall in GST turnover"),
    ("promoter_pledge_pct", lambda v: v > 30, "High promoter share pledge"),
]


def scan(b: dict) -> dict:
    triggers = [msg for key, test, msg in RULES if test(b[key])]
    status = "RED" if len(triggers) >= 3 else "AMBER" if triggers else "GREEN"
    return {"name": b["name"], "exposure": b["exposure"], "status": status, "triggers": triggers}


SYSTEM = (
    "You are a credit monitoring officer. For each AMBER or RED borrower write a watch-list note: "
    "situation, likely cause, recommended actions (e.g. client call, stock audit, tighten limits, SMA classification), "
    "and review date. For GREEN borrowers just say 'No action'."
)


def main():
    banner("06 - Early Warning Signals Monitor (LangChain)")
    results = [scan(b) for b in BORROWERS]
    section("EWS scan", json.dumps(results, indent=2))
    section("Watch-list notes", run_chain(SYSTEM, "EWS results:\n{r}\n\nRaw data:\n{raw}",
                                          r=json.dumps(results, indent=2), raw=json.dumps(BORROWERS, indent=2)))


if __name__ == "__main__":
    main()
