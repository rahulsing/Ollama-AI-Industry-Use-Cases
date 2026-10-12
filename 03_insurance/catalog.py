"""Insurance industry catalog. Regenerate docs after editing:  python scripts/build_docs.py"""

DOMAIN = {
    "name": "Insurance",
    "icon": "🛡️",
    "tagline": "Property & casualty, motor and home insurers",
    "description": "AI agents for claims handling, fraud detection, coverage questions and pricing.",
}

CATEGORIES = {
    "claims": "🧾 Claims & Fraud",
    "policy": "🙋 Policy & Customer Service",
    "underwriting": "📝 Underwriting & Pricing",
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
]
