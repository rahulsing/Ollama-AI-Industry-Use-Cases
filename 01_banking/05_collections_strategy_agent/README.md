# 05 · Collections & Recovery Strategist

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏦 Credit & Lending

## 🏦 The business problem (new to banking? start here)

**In the business today:** When customers miss loan payments, the collections team decides who to contact, how (SMS, call, letter), how often, and what to offer (payment plan, settlement).

**Who does this work:** Collections strategy and operations teams.

**Why it's hard:** Too soft loses money; too aggressive harms customers and breaks conduct rules, especially for customers in hardship.

### Key terms
- **Collections**: The team that contacts customers who have missed payments and agrees ways to pay, e.g. payment plans.
- **DPD (Days Past Due)**: How many days a payment is late. 30, 60 and 90 DPD are the standard warning milestones.
- **Delinquency / NPA / NPL**: A delinquent loan is behind on payments. After about 90 DPD it becomes a Non-Performing Asset / Loan.
- **Propensity to pay**: A prediction of how likely a late customer is to pay, used to choose the right collection approach.
- **Vulnerable customer**: Someone more likely to suffer harm (e.g. due to age, illness, bereavement). Banks must take extra care with them.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Segments delinquent accounts and designs a compliant, empathetic collection strategy per segment.

### How it works
Accounts are bucketed by DPD and propensity-to-pay; a Collections Strategist agent designs treatments and a Conduct Reviewer agent checks for fair-treatment issues.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/05_collections_strategy_agent/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
