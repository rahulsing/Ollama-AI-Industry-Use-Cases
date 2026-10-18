"""Home Insurance Underwriting Assessor — CrewAI + Ollama.

Python applies the underwriting guide (appetite, referral rules, rebuild-cost check, policy terms) and prices
each home; agents explain the risks and write the decisions and notes for the broker.

Run:  python 03_insurance/04_home_underwriting_assessor/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, make_agent, make_task, run_crew, section

# New home insurance applications from brokers. declared_rebuild = buildings sum insured the customer asked for
APPLICATIONS = [
    {"id": "HU-01", "property": "3-bed semi-detached, 1998", "construction": "brick, tiled roof", "floor_area_m2": 95,
     "flood_risk": "low", "subsidence_last_10y": False, "engineer_certificate": False, "claims_5y": [],
     "listed_building": False, "declared_rebuild": 180_000},
    {"id": "HU-02", "property": "4-bed detached by the river, 1975", "construction": "brick, tiled roof",
     "floor_area_m2": 160, "flood_risk": "high", "subsidence_last_10y": False, "engineer_certificate": False,
     "claims_5y": ["escape of water"], "listed_building": False, "declared_rebuild": 220_000},
    {"id": "HU-03", "property": "2-bed Victorian terrace, 1890", "construction": "brick, slate roof",
     "floor_area_m2": 80, "flood_risk": "low", "subsidence_last_10y": True, "engineer_certificate": True,
     "claims_5y": ["subsidence"], "listed_building": False, "declared_rebuild": 175_000},
    {"id": "HU-04", "property": "3-bed cottage, 1760", "construction": "stone, thatched roof", "floor_area_m2": 110,
     "flood_risk": "medium", "subsidence_last_10y": False, "engineer_certificate": False, "claims_5y": [],
     "listed_building": True, "declared_rebuild": 420_000},
]
REBUILD_RATE_PER_M2 = 1_850      # average rebuild cost for standard construction
UNDERINSURED_BELOW = 0.85        # declared rebuild under 85% of our estimate -> increase the sum insured
MAX_CLAIMS_5Y = 3
RATE_PER_1000 = 1.20             # base buildings premium per 1,000 of sum insured
FLOOD_LOADING = {"low": 1.0, "medium": 1.25, "high": 1.6}
CLAIM_LOADING = 0.15             # +15% per claim in the last 5 years


def key_risks(a: dict) -> list[str]:
    """The application's risk facts in plain English, so the agents explain these rather than reread raw fields."""
    sub = ("subsidence in the last 10 years" + (", structural engineer's certificate supplied" if a["engineer_certificate"]
                                                 else ", no structural engineer's certificate")
           if a["subsidence_last_10y"] else "no subsidence in the last 10 years")
    claims = f"claims in the last 5 years: {', '.join(a['claims_5y'])}" if a["claims_5y"] else "no claims in the last 5 years"
    return [f"{a['flood_risk']} flood risk", a["construction"], sub, claims] + (["listed building"] if a["listed_building"] else [])


def assess(a: dict) -> dict:
    declines, referrals, terms = [], [], []
    if "thatch" in a["construction"]:
        declines.append("Thatched roof: outside our appetite (non-standard construction)")
    if len(a["claims_5y"]) > MAX_CLAIMS_5Y:
        declines.append(f"{len(a['claims_5y'])} claims in 5 years (maximum {MAX_CLAIMS_5Y})")
    if a["subsidence_last_10y"]:
        (referrals if a["engineer_certificate"] else declines).append(
            "Subsidence in the last 10 years" + (" (structural engineer's certificate supplied)" if a["engineer_certificate"]
                                                 else " with no structural engineer's certificate"))
    if a["listed_building"]:
        referrals.append("Listed building: specialist rebuild costs")

    estimate = a["floor_area_m2"] * REBUILD_RATE_PER_M2
    sum_insured = a["declared_rebuild"]
    if a["declared_rebuild"] < UNDERINSURED_BELOW * estimate:
        sum_insured = estimate
        terms.append(f"Increase the buildings sum insured from {a['declared_rebuild']:,} to {estimate:,} "
                     f"(declared is {a['declared_rebuild'] / estimate:.0%} of our rebuild estimate)")
    if a["flood_risk"] == "high":
        terms.append("Flood excess of 1,000")
    if "escape of water" in a["claims_5y"]:
        terms.append("Escape of water excess of 750")
    if a["subsidence_last_10y"]:
        terms.append("Subsidence excess of 2,500")

    decision = ("DECLINE" if declines else "REFER TO SENIOR UNDERWRITER" if referrals
                else "ACCEPT WITH TERMS" if terms else "ACCEPT")
    if declines:
        return {"id": a["id"], "summary_line": f"{a['id']}: DECLINE", "property": a["property"],
                "key_risks": key_risks(a), "decision": decision, "decline_reasons": declines}
    premium = round(sum_insured / 1000 * RATE_PER_1000 * FLOOD_LOADING[a["flood_risk"]]
                    * (1 + CLAIM_LOADING * len(a["claims_5y"])))
    price = (f"indicative premium {premium} a year, subject to referral" if referrals
             else f"premium {premium} a year, buildings sum insured {sum_insured:,}")
    return {"id": a["id"], "summary_line": f"{a['id']}: {decision}, {price}", "property": a["property"],
            "key_risks": key_risks(a), "decision": decision, "referral_reasons": referrals or None, "terms": terms or None,
            "rebuild_estimate": estimate, "declared_rebuild": a["declared_rebuild"], "sum_insured_quoted": sum_insured,
            "indicative_annual_premium": premium if not referrals else f"{premium} (subject to referral)"}


def main():
    banner("Insurance 04 - Home Insurance Underwriting Assessor (CrewAI)")
    results = [assess(a) for a in APPLICATIONS]
    section("Underwriting rules", json.dumps(results, indent=2))

    analyst = make_agent("Risk Analyst", "Explain the main risks of each home and why the rules reached their decision",
                         "Home insurance risk analyst who knows flood, subsidence and construction risks.")
    underwriter = make_agent("Lead Underwriter", "Write the final decision and clear notes for the broker",
                             "You approve home insurance risks: you are firm on appetite but always helpful to brokers.")
    t1 = make_task("Rule results (final, do not change):\n{results}\n\nFor each application explain in 2-3 sentences "
                   "its main risks, using only its key_risks, and why the rules reached this decision.",
                   "Risk summary per application.", analyst)
    t2 = make_task("Rule results (exact; copy each decision, term, sum insured and premium unchanged):\n{results}\n\n"
                   "Write a note to the broker for each application.",
                   "Per application: its summary_line copied exactly as the heading, then a short note in sentences, "
                   "not a list of fields: each term in plain English and why it is there, and the next step: for "
                   "ACCEPT what happens next; for ACCEPT WITH TERMS what the customer must agree to; "
                   "for REFER the documents the senior underwriter needs; for DECLINE a courteous reason and a "
                   "suggestion to try a specialist insurer. No date, signature or placeholder lines.",
                   underwriter, context=[t1])
    section("Broker notes", run_crew([analyst, underwriter], [t1, t2], {"results": json.dumps(results, indent=2)}))


if __name__ == "__main__":
    main()
