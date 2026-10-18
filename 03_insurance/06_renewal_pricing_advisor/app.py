"""Renewal Pricing & Retention Advisor — LangChain chain + Ollama.

Python prices each motor renewal: claims inflation and claims loadings, a fair-pricing cap (never more than a new
customer would pay for the same cover), a floor at the technical price, and a guarded competitor price match;
the LLM writes the renewal review and a plain-English note for each customer.

Run:  python 03_insurance/06_renewal_pricing_advisor/app.py
"""

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import banner, run_chain, section

# Motor policies renewing next month.
# technical_price = expected claims cost + expenses for this risk next year (from the pricing model)
# new_business_price = what we would charge a new customer for exactly the same risk and cover today
RENEWALS = [
    {"id": "RN-01", "years_with_us": 8, "last_premium": 540, "at_fault_claims_last_year": 0,
     "technical_price": 430, "new_business_price": 505, "competitor_quote": None},
    {"id": "RN-02", "years_with_us": 2, "last_premium": 610, "at_fault_claims_last_year": 1,
     "technical_price": 690, "new_business_price": 840, "competitor_quote": None},
    {"id": "RN-03", "years_with_us": 4, "last_premium": 480, "at_fault_claims_last_year": 0,
     "technical_price": 400, "new_business_price": 530, "competitor_quote": 470},
    {"id": "RN-04", "years_with_us": 3, "last_premium": 395, "at_fault_claims_last_year": 0,
     "technical_price": 455, "new_business_price": 445, "competitor_quote": None},
]
CLAIMS_INFLATION = 0.07     # repair and parts costs up 7% this year
CLAIM_LOADING = 0.25        # +25% per at-fault claim last year
MIN_MARGIN = 0.05           # a price match never goes below technical price + 5%
BIG_INCREASE = 0.20         # increases above 20% need a call and cheaper options


def price(r: dict) -> dict:
    steps = [f"last premium {r['last_premium']}"]
    reasons = [f"repair and parts costs rose about {CLAIMS_INFLATION:.0%} this year"]   # for the customer note
    p = r["last_premium"] * (1 + CLAIMS_INFLATION)
    steps.append(f"+{CLAIMS_INFLATION:.0%} claims inflation -> {p:.2f}")
    if r["at_fault_claims_last_year"]:
        p *= 1 + CLAIM_LOADING * r["at_fault_claims_last_year"]
        steps.append(f"+{CLAIM_LOADING:.0%} for {r['at_fault_claims_last_year']} at-fault claim -> {p:.2f}")
        reasons.append("the at-fault claim on the policy last year")
    flags = []
    if p < r["technical_price"]:
        p = r["technical_price"]
        steps.append(f"raised to the technical price -> {p}")
        reasons.append("the cost of insuring cars like yours in your area has gone up")
    if p > r["new_business_price"]:  # the fair-pricing rule wins over the technical price
        p = r["new_business_price"]
        steps.append(f"capped at the new-customer price {p} (fair-pricing rule)")
        reasons.append("we never charge a renewing customer more than a new customer for the same cover")
    floor = round(r["technical_price"] * (1 + MIN_MARGIN), 2)
    if r["competitor_quote"] and r["competitor_quote"] < p:
        p = max(r["competitor_quote"], floor)
        steps.append(f"price match to {p:g} (competitor quote {r['competitor_quote']}; our floor would be {floor:g})")
        reasons.append(f"we matched the {r['competitor_quote']} quote you told us about" if p == r["competitor_quote"]
                       else "we reduced the price as far as we can towards the quote you told us about")
    if p < r["technical_price"]:
        flags.append(f"Below technical price ({r['technical_price']}) but capped by the fair-pricing rule: refer to "
                     "the pricing team to review new-customer rates, which are too low for this risk")
    change = p / r["last_premium"] - 1
    if change > BIG_INCREASE:
        flags.append("Large increase: call the customer and offer options (higher voluntary excess, fewer add-ons)")
    return {"id": r["id"], "years_with_us": r["years_with_us"], "last_premium": r["last_premium"],
            "renewal_premium": round(p, 2), "change": f"{change:+.1%}", "change_amount": round(p - r["last_premium"], 2),
            "internal_price_steps": steps, "margin_over_technical_price": round(p - r["technical_price"], 2),
            "flags": flags or None, "reasons_for_customer": reasons}


SYSTEM = (
    "You are a motor insurance pricing analyst. Use ONLY the figures given; never recalculate. Write amounts as "
    "plain numbers (505, never $505). Write: (1) a renewal review for the pricing manager: a table with columns ID | "
    "Last premium | Renewal premium | Change | Why (summarise internal_price_steps), then a 'Flags' list quoting "
    "every flag with its ID; (2) 'Customer notes': 2-3 friendly sentences per customer explaining their new price "
    "and the change, using ONLY reasons_for_customer, with no greeting, sign-off or placeholders like [Your Name]. "
    "Customer notes never mention internal price steps, technical price, margin, floors or flags. Under 350 words."
)


def main():
    banner("Insurance 06 - Renewal Pricing & Retention Advisor (LangChain chain)")
    results = [price(r) for r in RENEWALS]
    section("Renewal prices", json.dumps(results, indent=2))
    section("Renewal review", run_chain(SYSTEM, "Renewal prices:\n{r}", r=json.dumps(results, indent=2)))


if __name__ == "__main__":
    main()
