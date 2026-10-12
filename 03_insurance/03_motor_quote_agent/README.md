# 03 · Motor Insurance Quote Agent

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🛡️ Insurance · **Category:** 📝 Underwriting & Pricing

## 🛡️ The business problem (new to insurance? start here)

**In the business today:** Underwriters and pricing teams set premiums using a rating engine: a base price adjusted by rating factors such as driver age, experience, car and area.

**Who does this work:** Pricing / underwriting teams; customers see the result as a quote.

**Why it's hard:** Customers often don't understand why their quote is high. Clear explanations and 'what if' options (higher excess, lower mileage) help them choose and build trust.

### Key terms
- **Premium**: The price a customer pays for an insurance policy, usually yearly or monthly.
- **Underwriting**: Assessing a risk and deciding whether to insure it and on what terms.
- **Rating factor**: A characteristic that changes the premium, e.g. driver age, car group or postcode.
- **Rating engine**: The system that calculates a premium from a base rate and rating factors.
- **Vehicle (insurance) group**: A 1-50 scale ranking cars by repair cost, performance and security. Higher groups cost more to insure.
- **Voluntary excess**: An extra excess the customer chooses to pay on claims in exchange for a lower premium.
- **Excess (deductible)**: The amount the customer pays towards each claim before the insurer pays the rest.

More terms: [Insurance Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Prices a car insurance policy, explains what drives the premium and answers what-if questions.

### How it works
A rating-engine tool multiplies a base premium by rating factors (age, experience, car group, area, claims, mileage, excess); the agent explains the breakdown and re-prices what-ifs.

## Run
```bash
# from the repo root, with Ollama running
python 03_insurance/03_motor_quote_agent/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Insurance use cases](../README.md#-use-cases) · [All industries](../../README.md)
