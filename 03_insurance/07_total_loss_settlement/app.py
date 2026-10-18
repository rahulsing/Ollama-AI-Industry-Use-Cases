"""Motor Total Loss Settlement Agent — LangChain tool-calling agent + Ollama.

Tools value the car from comparable adverts, decide whether it is a write-off, and work out the settlement:
who gets paid what (the finance company first), and how much less the customer gets if they keep the car.

Run:  python 03_insurance/07_total_loss_settlement/app.py
      python 03_insurance/07_total_loss_settlement/app.py "Claim CL-7731: why is my car worth so little?"
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from langchain_core.tools import tool

from common import banner, run_agent, section

CLAIMS = {
    "CL-7731": {"vehicle": "2021 Volkswagen Golf 1.5 TSI Life", "mileage": 38_000, "repair_estimate": 11_800,
                "damage": "structural: chassis leg and floor pan bent", "excess": 350,
                "finance": {"lender": "Northgate Finance", "outstanding": 6_200}, "gap_insurance": False},
}
# Adverts for the same model and trim from the last 30 days (normally a trade valuation guide or listings feed)
COMPARABLES = {
    "CL-7731": [("dealer advert", 31_000, 16_450), ("dealer advert", 36_500, 15_990), ("private sale", 42_000, 15_200)],
}
MILEAGE_ADJUSTMENT = 40       # value change per 1,000 miles of difference
WRITE_OFF_THRESHOLD = 0.60    # repairs costing more than 60% of the car's value are uneconomical
SALVAGE_SHARE = 0.20          # salvage is worth about 20% of the market value
DOCUMENTS = ["vehicle registration document (logbook)", "both keys", "finance settlement letter", "service history"]


def _value(claim_id: str) -> tuple[dict, list, int]:
    c = CLAIMS[claim_id]
    adjusted = [(src, miles, ad, ad + round((miles - c["mileage"]) / 1000 * MILEAGE_ADJUSTMENT))
                for src, miles, ad in COMPARABLES[claim_id]]
    return c, adjusted, round(sum(a[3] for a in adjusted) / len(adjusted))


@tool
def vehicle_valuation(claim_id: str) -> dict:
    """Market value of the claim's car from comparable adverts, and whether it is a write-off (total loss)."""
    if claim_id.strip().upper() not in CLAIMS:
        return {"error": f"Unknown claim {claim_id!r}. Use the claim ID the customer gave, e.g. 'CL-7731'."}
    c, adjusted, value = _value(claim_id.strip().upper())
    ratio = c["repair_estimate"] / value
    structural = c["damage"].startswith("structural")
    return {"vehicle": c["vehicle"], "mileage": c["mileage"], "market_value": value,
            "comparables": [f"{src}, {miles:,} miles: {ad:,}, adjusted for mileage to {adj:,}"
                            for src, miles, ad, adj in adjusted],
            "repair_estimate": c["repair_estimate"], "repair_cost_share_of_value": f"{ratio:.0%}",
            "decision": "TOTAL LOSS (uneconomical to repair)" if ratio > WRITE_OFF_THRESHOLD else "REPAIR",
            "write_off_category": ("Category S: structural damage, can be professionally repaired and put back on "
                                   "the road") if structural else "Category N: non-structural damage, can be repaired"}


@tool
def settlement_options(claim_id: str) -> dict:
    """Total loss settlement for a claim: what the insurer pays, how much goes to the finance company and the
    customer, for both options: the insurer keeps the car, or the customer keeps it."""
    if claim_id.strip().upper() not in CLAIMS:
        return {"error": f"Unknown claim {claim_id!r}. Use the claim ID the customer gave, e.g. 'CL-7731'."}
    c, _, value = _value(claim_id.strip().upper())
    salvage = round(value * SALVAGE_SHARE)
    lender, owed = c["finance"]["lender"], c["finance"]["outstanding"]

    def split(total: int) -> dict:
        to_lender = min(owed, total)
        return {"excess_deducted": c["excess"], "total_settlement": total, "paid_to_finance_company": to_lender,
                "paid_to_customer": total - to_lender,
                "still_owed_to_lender": owed - to_lender if owed > total else 0}

    return {"market_value": value, "excess": c["excess"], "salvage_value": salvage, "finance_company": lender,
            "option_1_insurer_keeps_car": {"calculation": f"{value:,} - {c['excess']} excess", **split(value - c["excess"])},
            "option_2_customer_keeps_car": {"calculation": f"{value:,} - {c['excess']} excess - {salvage:,} salvage value",
                                            **split(value - c["excess"] - salvage),
                                            "conditions": "the car must be professionally repaired and inspected "
                                                          "before it is driven again; it stays recorded as a write-off"},
            "finance_rule": f"the outstanding finance ({owed:,}) is paid to {lender} first, because they own the car "
                            "until it is paid off",
            "gap_insurance": c["gap_insurance"], "documents_needed": DOCUMENTS,
            "payment": "within 5 working days of receiving the documents",
            "if_you_disagree_with_the_value": "send adverts for the same model, year and mileage and we will review it"}


SYSTEM = (
    "You are a motor claims assistant explaining a total loss settlement to a customer. Work in two steps. Step 1: "
    "call vehicle_valuation with the customer's claim ID. Step 2: call settlement_options with the same claim ID. "
    "Then answer. Copy every number exactly as the tools returned it; never add, subtract or round, and add no "
    "currency symbols. Explain: the market value and how it was set (list the comparables), why the car is a "
    "write-off and its write-off category, both settlement options with their calculation line, the excess "
    "deducted and what goes to the finance company and to the customer, the documents needed, and what to do if they "
    "disagree with the value. Be warm and clear; the customer has just lost their car."
)


def main():
    banner("Insurance 07 - Motor Total Loss Settlement Agent (LangChain agent)")
    q = sys.argv[1] if len(sys.argv) > 1 else (
        "My car was written off in the crash last week (claim CL-7731). How much will I get, and could I keep the car "
        "and get it repaired myself instead?")
    section("Customer", q)
    section("Answer", run_agent(SYSTEM, [vehicle_valuation, settlement_options], q))


if __name__ == "__main__":
    main()
