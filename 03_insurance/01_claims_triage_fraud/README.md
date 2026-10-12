# 01 · Claims Triage & Fraud Detection

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🛡️ Insurance · **Category:** 🧾 Claims & Fraud

## 🛡️ The business problem (new to insurance? start here)

**In the business today:** When a customer reports a loss, claims handlers decide how to handle it: pay simple claims fast, send complex ones to an adjuster, and refer suspicious ones to the fraud team.

**Who does this work:** Claims handlers, adjusters and the Special Investigations Unit (SIU).

**Why it's hard:** Honest customers expect quick payment, but fraud is expensive. Handlers must spot red flags without treating genuine customers as suspects, and must not miss chances to recover costs from at-fault third parties.

### Key terms
- **FNOL**: First Notice of Loss: the first report of a claim to the insurer.
- **Claims triage**: Sorting new claims by complexity and risk: fast-track simple ones, send complex ones to experts.
- **Adjuster**: The claims professional who assesses a claim and decides what the insurer pays.
- **Insurance fraud**: Exaggerating or inventing a claim. Fraud costs insurers billions, raising premiums for everyone.
- **Red flag**: A warning sign of possible fraud, e.g. a claim soon after the policy started or no proof of ownership.
- **SIU**: Special Investigations Unit: the team that investigates suspected fraud.
- **Subrogation**: Recovering what the insurer paid from a third party who caused the loss, e.g. the at-fault driver's insurer.
- **Sum insured**: The maximum the insurer will pay for a policy or item.

More terms: [Insurance Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Triages new claims into fast-track, adjuster review or fraud investigation, and spots recovery opportunities.

### How it works
Python applies red-flag rules (new policy, late reporting, near sum insured, prior claims) and decides the handling (pay, adjuster review, SIU referral), so no honest customer is flagged by the AI; a Claims Adjuster agent assesses each claim and an SIU Investigator agent writes evidence requests, customer messages and recovery actions.

## Run
```bash
# from the repo root, with Ollama running
python 03_insurance/01_claims_triage_fraud/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Insurance use cases](../README.md#-use-cases) · [All industries](../../README.md)
