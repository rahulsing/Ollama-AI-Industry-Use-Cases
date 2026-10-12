"""Sanctions Screening Assistant — fuzzy matching + LangChain adjudication.

Run:  python 01_banking/11_sanctions_screening_assistant/app.py
"""

import json
import sys
from difflib import SequenceMatcher
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, run_chain, section

# Fictional watchlist for demo purposes only
WATCHLIST = [
    {"name": "Viktor Aleksandrovich Petrov", "dob": "1965-03-12", "nationality": "RU", "program": "SDN-UKRAINE"},
    {"name": "Hassan Al-Rashid", "dob": "1972-11-02", "nationality": "SY", "program": "SDGT"},
    {"name": "Golden Crescent Shipping LLC", "dob": None, "nationality": "IR", "program": "IRAN"},
]

PARTIES = [
    {"name": "Victor A. Petrov", "dob": "1988-07-19", "nationality": "CA", "address": "Toronto, Canada", "role": "Remitter"},
    {"name": "Hasan Al Rashid", "dob": "1972-11-02", "nationality": "SY", "address": "Dubai, UAE", "role": "Beneficiary"},
    {"name": "Golden Crescent Shipping", "dob": None, "nationality": "AE", "address": "Jebel Ali, UAE", "role": "Beneficiary"},
]


def norm(s: str) -> str:
    return " ".join(s.lower().replace("-", " ").replace(".", "").split())


def token_score(a: str, b: str) -> float:
    """Average best match of each token in `a` against `b`; single letters match as initials."""
    ta, tb = norm(a).split(), norm(b).split()
    best = [max(1.0 if len(t) == 1 and u.startswith(t) else SequenceMatcher(None, t, u).ratio() for u in tb) for t in ta]
    return sum(best) / len(best)


def screen(party: dict, threshold: float = 0.75) -> list[dict]:
    hits = []
    for w in WATCHLIST:
        score = max(SequenceMatcher(None, norm(party["name"]), norm(w["name"])).ratio(), token_score(party["name"], w["name"]))
        if score >= threshold:
            hits.append({"party": party, "watchlist_entry": w, "name_score": round(score, 2)})
    return hits


SYSTEM = (
    "You are a sanctions screening analyst. For each potential match, compare secondary identifiers "
    "(DOB, nationality, entity type, location). Decide TRUE MATCH, POSSIBLE MATCH (escalate) or FALSE POSITIVE, "
    "with a one-line reason. Be conservative: if identifiers support the match, do not discount it. "
    "For persons, a clearly different DOB is strong evidence of a false positive. For entities, a different "
    "country of registration does NOT clear a near-identical name (front companies are common) - escalate. "
    "Finish with whether the payment can be released or must be held."
)


def main():
    banner("11 - Sanctions Screening Assistant (LangChain)")
    hits = [h for p in PARTIES for h in screen(p)]
    section("Fuzzy-match hits", json.dumps(hits, indent=2))
    section("Adjudication", run_chain(SYSTEM, "Potential matches:\n{hits}", hits=json.dumps(hits, indent=2)))


if __name__ == "__main__":
    main()
