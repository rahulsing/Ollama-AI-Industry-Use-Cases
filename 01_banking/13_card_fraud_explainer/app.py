"""Card Fraud Detection Explainer — rule score + LangChain explanation.

Run:  python 01_banking/13_card_fraud_explainer/app.py
"""

import json
import statistics
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, run_chain, section

HISTORY_AMOUNTS = [42, 18, 65, 120, 33, 54, 75, 22, 90, 47, 38, 61]  # customer's usual spend
HOME_COUNTRY = "GB"
HIGH_RISK_MCC = {"6051": "Quasi-cash / crypto", "7995": "Gambling", "5967": "Direct marketing"}

TRANSACTIONS = [
    {"id": "T1", "time": "2026-10-10 12:04", "amount": 58, "merchant": "Tesco", "mcc": "5411", "country": "GB", "card_present": True, "txns_last_hour": 1},
    {"id": "T2", "time": "2026-10-10 02:13", "amount": 1450, "merchant": "CoinFast", "mcc": "6051", "country": "LT", "card_present": False, "txns_last_hour": 4},
    {"id": "T3", "time": "2026-10-10 02:19", "amount": 980, "merchant": "LuckySpin", "mcc": "7995", "country": "MT", "card_present": False, "txns_last_hour": 5},
    {"id": "T4", "time": "2026-10-10 18:40", "amount": 240, "merchant": "Ryanair", "mcc": "4511", "country": "IE", "card_present": False, "txns_last_hour": 1},
]


def score(t: dict) -> dict:
    mu, sd = statistics.mean(HISTORY_AMOUNTS), statistics.stdev(HISTORY_AMOUNTS)
    z = (t["amount"] - mu) / sd
    hour = int(t["time"][11:13])
    reasons, s = [], 0
    if z > 3: s += 30; reasons.append(f"amount z-score {z:.1f}")
    if t["mcc"] in HIGH_RISK_MCC: s += 25; reasons.append(f"high-risk MCC ({HIGH_RISK_MCC[t['mcc']]})")
    if t["country"] != HOME_COUNTRY: s += 15; reasons.append(f"foreign country {t['country']}")
    if not t["card_present"]: s += 10; reasons.append("card-not-present")
    if t["txns_last_hour"] >= 3: s += 20; reasons.append(f"velocity {t['txns_last_hour']} txns/hour")
    if hour < 5: s += 10; reasons.append("unusual hour")
    band = "BLOCK" if s >= 70 else "REVIEW" if s >= 40 else "APPROVE"
    return {"id": t["id"], "merchant": t["merchant"], "amount": t["amount"], "score": s, "action": band, "reasons": reasons}


SYSTEM = (
    "You are a card fraud analyst. For each scored transaction write (a) a 1-2 sentence analyst explanation and "
    "(b) for BLOCK/REVIEW, a short SMS to the customer asking them to confirm the transaction (never ask for PIN, "
    "OTP or full card number). Keep the decided actions."
)


def main():
    banner("13 - Card Fraud Detection Explainer (LangChain)")
    scored = [score(t) for t in TRANSACTIONS]
    section("Scores", json.dumps(scored, indent=2))
    section("Explanations", run_chain(SYSTEM, "Scored transactions:\n{s}", s=json.dumps(scored, indent=2)))


if __name__ == "__main__":
    main()
