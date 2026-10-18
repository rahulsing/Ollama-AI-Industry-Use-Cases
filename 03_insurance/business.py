"""Plain-English business context for people new to insurance (used by build_docs.py and ui.py)."""

INDUSTRY_101 = """\
**How an insurer makes money:** customers pay a *premium* to transfer a risk (a car crash, a burglary) to the
insurer. The insurer pools many customers' premiums and pays the *claims* of the few who suffer a loss. Profit comes
from pricing risk correctly (premiums > claims + costs) and from investing premiums before claims are paid.

**What makes it hard:**
1. **Pricing (underwriting):** charge each customer the right premium for their risk. Too low loses money; too high loses customers.
2. **Claims:** pay genuine claims quickly and fairly, while catching fraud, which adds costs for every honest customer.
3. **Clarity:** policies are long legal documents. Customers need clear answers about what they are covered for.
4. **Reserves and catastrophes:** claims are paid over years, so insurers must set aside enough money for claims not yet
   paid (or even reported), and make sure one big storm or flood can't sink the company, using *reinsurance*.
"""

AREAS = [
    ("claims", "Claims & Fraud", "Handles losses reported by customers, pays valid claims and investigates suspicious ones."),
    ("policy", "Policy & Customer Service", "Answers customers' questions about their cover and handles policy changes."),
    ("underwriting", "Underwriting & Pricing", "Decides which risks to accept and at what premium."),
    ("actuarial", "Actuarial & Risk", "Sets aside money for future claims and limits how much one catastrophe could cost."),
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
    "Risk appetite": ("Underwriting", "The types and amount of risk the insurer is willing to accept, set by the board."),
    "Referral": ("Underwriting", "Passing a risk the rules can't approve on their own to a more senior underwriter."),
    "Rebuild cost": ("Underwriting", "What it would cost to rebuild the home from scratch. This, not the market price, sets the buildings sum insured."),
    "Underinsurance": ("Underwriting", "Insuring something for less than it is worth. The insurer may then pay only part of each claim."),
    "Policy terms (endorsement)": ("Underwriting", "Special conditions added to one customer's policy, e.g. a higher flood excess."),
    "Subsidence": ("Underwriting", "Ground under a building sinking, which cracks walls. Expensive to fix, so insurers check its history."),
    "Vulnerable customer": ("Claims", "A customer whose circumstances (age, health, a crisis) mean they need extra care and support."),
    "Bodily injury claim": ("Claims", "A claim for someone's injury, handled by a specialist team because it is costly and slow to settle."),
    "Total loss (write-off)": ("Claims", "When repairing the car would cost too much compared with its value, so the insurer pays out its value instead."),
    "Market value": ("Claims", "What it would cost to buy the same car (make, model, age, mileage) just before the loss."),
    "Salvage": ("Claims", "The damaged car's remaining value, e.g. for parts. The insurer sells it unless the customer keeps it."),
    "Write-off category": ("Claims", "How badly a written-off car is damaged: Category S (structural) and N (non-structural) can be repaired; A and B must be scrapped."),
    "Claims leakage": ("Claims", "Money paid on claims that should not have been, through mistakes or missed recoveries rather than fraud."),
    "Wear and tear (betterment)": ("Claims", "A deduction for an old item's age when the policy pays its value, so the customer isn't better off than before."),
    "Renewal": ("Pricing", "Offering an existing customer a new policy year, usually at a new price."),
    "Technical price": ("Pricing", "The price that covers the expected claims and costs for a risk. Below it, the policy is expected to lose money."),
    "Fair-pricing rule": ("Pricing", "A rule (e.g. in the UK since 2022) that renewing customers can't be charged more than a new customer for the same cover."),
    "Price walking": ("Pricing", "Raising prices for loyal customers each year because they rarely shop around. Banned by fair-pricing rules."),
    "Claims reserve": ("Actuarial", "Money set aside today for claims that will be paid in the future."),
    "IBNR": ("Actuarial", "Incurred But Not Reported: claims that have happened but the insurer hasn't heard about yet."),
    "Accident year": ("Actuarial", "The year in which the losses happened, however many years the claims take to pay."),
    "Claims triangle": ("Actuarial", "A table of claims paid by accident year (rows) and years since (columns), used to see how claims build up over time."),
    "Chain-ladder": ("Actuarial", "The standard reserving method: assumes claims will keep building up the way they did in past years."),
    "Development factor": ("Actuarial", "How much claims paid for an accident year grow from one year to the next, e.g. 1.25 = +25%."),
    "Ultimate claims": ("Actuarial", "The total an accident year's claims will cost once every claim is paid."),
    "Loss ratio": ("Actuarial", "Claims divided by earned premium. Above about 75%, there is usually little left after costs."),
    "Earned premium": ("Actuarial", "The part of premiums that covers time already passed, matched against that period's claims."),
    "Catastrophe (cat) event": ("Actuarial", "One event, such as a storm or flood, that causes many claims at once."),
    "Total insured value (TIV)": ("Actuarial", "The sum of all the sums insured in an area: the most the insurer could lose there."),
    "1-in-200 event": ("Actuarial", "An event so severe it is expected once in 200 years (0.5% a year). Capital rules require surviving one."),
    "Reinsurance": ("Actuarial", "Insurance for insurers: another company pays part of very large losses in exchange for a premium."),
    "Excess of loss (XL)": ("Actuarial", "Reinsurance that pays the part of an event's loss above a retention, up to a limit, e.g. 100m excess of 25m."),
    "Accumulation": ("Actuarial", "Too much insured value concentrated in one area, so a single event hits many policies at once."),
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
    "04_home_underwriting_assessor": (
        "Brokers send home insurance applications. Underwriters check each home against the underwriting guide, then accept it, add terms, refer it to a senior colleague or decline it.",
        "Home underwriters, with senior underwriters for referrals; brokers pass the decisions to customers.",
        "Every home is different: flood risk, subsidence, old or unusual construction. Customers often underestimate the rebuild cost, which leaves them underinsured when they claim.",
        ["Underwriting", "Risk appetite", "Referral", "Rebuild cost", "Underinsurance", "Policy terms (endorsement)", "Subsidence", "Sum insured"]),
    "05_fnol_claim_intake": (
        "Customers report losses by email, web form or phone. Claims staff read each one, find the policy, check it was in force and covers the loss, and pass it to the right team.",
        "Claims intake and first-notice-of-loss (FNOL) teams.",
        "Reports arrive as free text with key facts scattered or missing. Emergencies, injuries and customers who need extra support must be spotted at once, not when the email reaches the top of the pile.",
        ["FNOL", "Claims triage", "Vulnerable customer", "Bodily injury claim", "Excess (deductible)", "Subrogation"]),
    "06_renewal_pricing_advisor": (
        "Each month, the pricing team sets the renewal price for policies coming up for renewal and the customer gets a renewal letter.",
        "Pricing analysts and retention teams.",
        "Prices must cover rising claims costs, but a renewing customer can't be charged more than a new one. Loyal customers deserve a clear reason when their price changes.",
        ["Renewal", "Technical price", "Fair-pricing rule", "Price walking", "Premium"]),
    "07_total_loss_settlement": (
        "When a car is too damaged to repair economically, the claims handler values it, agrees the settlement with the customer and pays any finance company first.",
        "Motor claims handlers and total loss teams.",
        "Customers are upset and often think the valuation is too low. The settlement must be clearly explained: how the value was set, the excess, the finance, and the option to keep the car.",
        ["Total loss (write-off)", "Market value", "Salvage", "Write-off category", "Excess (deductible)"]),
    "08_claims_reserving_analyst": (
        "Every quarter, actuaries estimate how much the insurer will still pay on claims that have already happened, and check the reserves on the balance sheet are enough.",
        "Reserving actuaries, the finance team and the reserving committee.",
        "Claims take years to settle and some haven't been reported yet. Too little in reserve overstates profit; too much ties up capital. The newest years are the most uncertain.",
        ["Claims reserve", "IBNR", "Accident year", "Claims triangle", "Chain-ladder", "Development factor", "Ultimate claims", "Loss ratio", "Earned premium"]),
    "09_cat_exposure_monitor": (
        "Before each storm season, the exposure team checks how much the insurer could lose from a severe storm or flood, after reinsurance, against the board's risk appetite.",
        "Catastrophe risk analysts, the chief underwriting officer and the board risk committee.",
        "Growth in cheap, high-hazard areas quietly piles up exposure. One event hits thousands of homes at once, and a loss bigger than the reinsurance falls straight on the insurer's capital.",
        ["Catastrophe (cat) event", "Total insured value (TIV)", "1-in-200 event", "Reinsurance", "Excess of loss (XL)", "Accumulation", "Risk appetite"]),
    "10_claims_leakage_auditor": (
        "Claims quality teams re-check a sample of closed claims to find money paid that shouldn't have been, and fix the cause.",
        "Claims auditors, claims managers and team leaders.",
        "Small mistakes repeat across thousands of claims: an excess not taken, an invoice paid twice, a third party nobody claimed from. Fixing the process matters more than blaming people.",
        ["Claims leakage", "Wear and tear (betterment)", "Subrogation", "Excess (deductible)"]),
}

# Flow diagram labels: (input data, what Python computes or decides, output). "" if Python does no maths.
FLOWS = {
    "01_claims_triage_fraud": ("New claims", "Red-flag rules → pay / adjuster / SIU", "Claim decisions + customer messages"),
    "02_policy_coverage_qa": ("Policy wording + schedule", "COVERED / NOT COVERED decision", "Answer with clause citations"),
    "03_motor_quote_agent": ("Driver & car details", "", "Premium + breakdown"),
    "04_home_underwriting_assessor": ("Home insurance applications", "Appetite, referral & rebuild-cost rules + premium", "Decisions + broker notes"),
    "05_fnol_claim_intake": ("Claim emails", "Check policy, cover, excess, missing info & urgency", "Claims work queue"),
    "06_renewal_pricing_advisor": ("Renewing policies", "Inflation & claim loadings, fair-pricing cap, match floor", "Renewal review + customer notes"),
    "07_total_loss_settlement": ("Claim, car & comparable adverts", "", "Settlement explained"),
    "08_claims_reserving_analyst": ("Paid claims triangle", "Chain-ladder: factors, ultimates, reserve gap", "Reserving memo"),
    "09_cat_exposure_monitor": ("Insured values by zone", "1-in-200 scenarios through reinsurance vs appetite", "Actions memo"),
    "10_claims_leakage_auditor": ("Closed claims", "Re-calculate payments + find missed recoveries", "Audit report + recovery plan"),
}

# What the user asks in the sample conversation (for use cases without a typed question)
ASK = {
    "01_claims_triage_fraud": "Triage this morning's new claims. Which can we pay, and which need an adjuster or a fraud check?",
    "04_home_underwriting_assessor": "Four home insurance applications came in from brokers this morning. Which can we accept, and on what terms?",
    "05_fnol_claim_intake": "Four new claims came in by email overnight. What are they, and what does the claims team need to do first?",
    "06_renewal_pricing_advisor": "Price next month's motor renewals. Who gets an increase, and are we treating loyal customers fairly?",
    "08_claims_reserving_analyst": "Are our motor claims reserves enough at year-end? Which accident years need more?",
    "09_cat_exposure_monitor": "Is our home insurance catastrophe exposure within appetite? What should we change before the winter storm season?",
    "10_claims_leakage_auditor": "Audit last month's closed claims. Where did we overpay, and what can we recover?",
}
