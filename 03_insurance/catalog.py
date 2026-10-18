"""Insurance industry catalog. Regenerate docs after editing:  python scripts/build_docs.py"""

DOMAIN = {
    "name": "Insurance",
    "icon": "🛡️",
    "tagline": "Property & casualty, motor and home insurers",
    "description": "AI agents for claims handling, fraud detection, coverage questions, underwriting, pricing, reserving and catastrophe risk.",
}

CATEGORIES = {
    "claims": "🧾 Claims & Fraud",
    "policy": "🙋 Policy & Customer Service",
    "underwriting": "📝 Underwriting & Pricing",
    "actuarial": "📊 Actuarial & Risk",
}

# (slug, title, category, framework, pattern, description, how_it_works)
USE_CASES = [
    ("01_claims_triage_fraud", "Claims Triage & Fraud Detection", "claims", "CrewAI", "Multi-agent",
     "Triages new claims into fast-track, adjuster review or fraud investigation, and spots recovery opportunities.",
     "Python applies red-flag rules (new policy, late reporting, near sum insured, prior claims) and decides the "
     "handling (pay, adjuster review, SIU referral), so no honest customer is flagged by the AI; a Claims Adjuster "
     "agent assesses each claim and an SIU Investigator agent writes evidence requests, customer messages and recovery actions."),
    ("02_policy_coverage_qa", "Policy Coverage Q&A (RAG)", "policy", "LangChain", "RAG",
     "Answers 'am I covered?' questions from the policy wording and the customer's schedule, with clause citations.",
     "Relevant clauses are retrieved (the schedule and excess are always included); the LLM fills a coverage "
     "checklist (matching section, conditions met) and checks each exclusion sentence; Python decides COVERED / NOT "
     "COVERED from the customer's schedule; the LLM explains the decision with citations."),
    ("03_motor_quote_agent", "Motor Insurance Quote Agent", "underwriting", "LangChain", "Tool-calling agent",
     "Prices a car insurance policy, explains what drives the premium and answers what-if questions.",
     "A rating-engine tool multiplies a base premium by rating factors (age, experience, car group, area, claims, "
     "mileage, excess); the agent explains the breakdown and re-prices what-ifs."),
    ("04_home_underwriting_assessor", "Home Insurance Underwriting Assessor", "underwriting", "CrewAI", "Multi-agent",
     "Decides whether to accept, refer or decline new home insurance applications, with terms and a premium.",
     "Python applies the underwriting guide: appetite (non-standard construction, too many claims), referral rules "
     "(subsidence, listed buildings), a rebuild-cost check that catches underinsurance, and extra excesses, then "
     "prices the home; a Risk Analyst agent explains the risks and a Lead Underwriter agent writes the broker notes."),
    ("05_fnol_claim_intake", "FNOL Claim Intake", "claims", "LangChain", "Structured extraction",
     "Turns first-notice-of-loss emails into checked claims, routed to the right team with urgent cases first.",
     "Each email is first classified (motor accident, home damage, theft), then the details for that type are "
     "extracted into a small Pydantic schema; Python checks the policy was in force on the loss date and covers the "
     "cause, sets the excess, lists missing information and flags emergencies, injuries and customers who need extra "
     "support; an LLM chain writes the claims team's work queue."),
    ("06_renewal_pricing_advisor", "Renewal Pricing & Retention Advisor", "underwriting", "LangChain", "Chain",
     "Prices motor renewals fairly and explains to each customer why their price went up or down.",
     "Python applies claims inflation and claim loadings, raises prices to the cost of the risk, caps every renewal "
     "at the price a new customer would pay (fair-pricing rule) and matches a competitor quote only down to a margin "
     "floor; an LLM chain writes the pricing review and a plain-English note per customer."),
    ("07_total_loss_settlement", "Motor Total Loss Settlement Agent", "claims", "LangChain", "Tool-calling agent",
     "Explains a write-off settlement: what the car is worth, why it's a write-off and who gets paid what.",
     "Tools value the car from mileage-adjusted comparable adverts, apply the 60% repair-cost write-off rule and "
     "category, and split the settlement between the finance company and the customer, with or without keeping the "
     "car; the agent explains it and copies every number from the tools."),
    ("08_claims_reserving_analyst", "Claims Reserving Analyst (Chain-Ladder)", "actuarial", "LangChain", "Chain",
     "Estimates how much money to hold for future claim payments and whether today's reserves are enough.",
     "Python runs the chain-ladder method on a paid claims triangle (age-to-age factors, ultimate claims, reserve "
     "needed per accident year) and compares it with booked reserves and the target loss ratio; an LLM chain writes "
     "the reserving memo with its caveats."),
    ("09_cat_exposure_monitor", "Catastrophe Exposure Monitor", "actuarial", "CrewAI", "Multi-agent",
     "Checks whether a 1-in-200 storm or flood would cost more than the board's risk appetite, and what to change.",
     "Python totals insured values by zone against appetite limits, runs 1-in-200 windstorm and flood scenarios "
     "through the reinsurance programme and works out the net loss and any extra cover needed; an Exposure Analyst "
     "agent explains the drivers and a Chief Underwriting Officer agent writes the actions memo."),
    ("10_claims_leakage_auditor", "Claims Leakage Auditor", "claims", "CrewAI", "Multi-agent",
     "Re-checks closed claims for overpayments and missed recoveries, and plans how to recover money and fix the process.",
     "Python re-calculates what each claim should have paid (excess, approved repair cost, wear and tear, duplicate "
     "invoices) and finds at-fault third parties nobody recovered from; a Claims Auditor agent explains the root "
     "causes and a Claims Manager agent writes the recovery list and process fixes."),
]
