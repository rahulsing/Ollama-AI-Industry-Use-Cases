"""Plain-English business context for people new to insurance (used by build_docs.py and ui.py)."""

INDUSTRY_101 = """\
**How an insurer makes money:** customers pay a *premium* to transfer a risk (a car crash, a burglary) to the
insurer. The insurer pools many customers' premiums and pays the *claims* of the few who suffer a loss. Profit comes
from pricing risk correctly (premiums > claims + costs) and from investing premiums before claims are paid.

**What makes it hard:**
1. **Pricing (underwriting):** charge each customer the right premium for their risk. Too low loses money; too high loses customers.
2. **Claims:** pay genuine claims quickly and fairly, while catching fraud, which adds costs for every honest customer.
3. **Clarity:** policies are long legal documents. Customers need clear answers about what they are covered for.
"""

AREAS = [
    ("claims", "Claims & Fraud", "Handles losses reported by customers, pays valid claims and investigates suspicious ones."),
    ("policy", "Policy & Customer Service", "Answers customers' questions about their cover and handles policy changes."),
    ("underwriting", "Underwriting & Pricing", "Decides which risks to accept and at what premium."),
]

GLOSSARY = {
    "Premium": ("Basics", "The price a customer pays for an insurance policy, usually yearly or monthly."),
    "Policy wording / schedule": ("Basics", "The wording is the full contract (what is and isn't covered); the schedule lists this customer's chosen covers and limits."),
    "Excess (deductible)": ("Basics", "The amount the customer pays towards each claim before the insurer pays the rest."),
    "Sum insured": ("Basics", "The maximum the insurer will pay for a policy or item."),
    "Exclusion": ("Basics", "Something the policy specifically does not cover, e.g. wear and tear."),
    "Add-on cover": ("Basics", "Optional extra cover bought on top of the core policy, e.g. accidental damage."),
    "Claim": ("Claims", "A customer's request for payment after a loss covered by the policy."),
    "FNOL": ("Claims", "First Notice of Loss: the first report of a claim to the insurer."),
    "Claims triage": ("Claims", "Sorting new claims by complexity and risk: fast-track simple ones, send complex ones to experts."),
    "Adjuster": ("Claims", "The claims professional who assesses a claim and decides what the insurer pays."),
    "Insurance fraud": ("Claims", "Exaggerating or inventing a claim. Fraud costs insurers billions, raising premiums for everyone."),
    "Red flag": ("Claims", "A warning sign of possible fraud, e.g. a claim soon after the policy started or no proof of ownership."),
    "SIU": ("Claims", "Special Investigations Unit: the team that investigates suspected fraud."),
    "Subrogation": ("Claims", "Recovering what the insurer paid from a third party who caused the loss, e.g. the at-fault driver's insurer."),
    "Underwriting": ("Pricing", "Assessing a risk and deciding whether to insure it and on what terms."),
    "Rating factor": ("Pricing", "A characteristic that changes the premium, e.g. driver age, car group or postcode."),
    "Rating engine": ("Pricing", "The system that calculates a premium from a base rate and rating factors."),
    "Vehicle (insurance) group": ("Pricing", "A 1-50 scale ranking cars by repair cost, performance and security. Higher groups cost more to insure."),
    "Voluntary excess": ("Pricing", "An extra excess the customer chooses to pay on claims in exchange for a lower premium."),
}

# (in the business today, who does it, why it's hard, [glossary terms])
BUSINESS = {
    "01_claims_triage_fraud": (
        "When a customer reports a loss, claims handlers decide how to handle it: pay simple claims fast, send complex ones to an adjuster, and refer suspicious ones to the fraud team.",
        "Claims handlers, adjusters and the Special Investigations Unit (SIU).",
        "Honest customers expect quick payment, but fraud is expensive. Handlers must spot red flags without treating genuine customers as suspects, and must not miss chances to recover costs from at-fault third parties.",
        ["FNOL", "Claims triage", "Adjuster", "Insurance fraud", "Red flag", "SIU", "Subrogation", "Sum insured"]),
    "02_policy_coverage_qa": (
        "Customers call the helpline asking 'am I covered for this?'. Staff check the policy wording and the customer's schedule, then explain the answer and the excess.",
        "Contact centre and claims helpline teams.",
        "Policy wordings are long and full of exclusions and conditions. Answers depend on which add-ons the customer bought, and wrong answers lead to complaints.",
        ["Policy wording / schedule", "Exclusion", "Add-on cover", "Excess (deductible)"]),
    "03_motor_quote_agent": (
        "Underwriters and pricing teams set premiums using a rating engine: a base price adjusted by rating factors such as driver age, experience, car and area.",
        "Pricing / underwriting teams; customers see the result as a quote.",
        "Customers often don't understand why their quote is high. Clear explanations and 'what if' options (higher excess, lower mileage) help them choose and build trust.",
        ["Premium", "Underwriting", "Rating factor", "Rating engine", "Vehicle (insurance) group", "Voluntary excess", "Excess (deductible)"]),
}
