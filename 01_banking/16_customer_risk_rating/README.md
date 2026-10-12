# 16 · Customer Risk Rating (CRR)

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Chain-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🕵️ Financial Crime & Compliance

## 🏦 The business problem (new to banking? start here)

**In the business today:** Each customer gets a money-laundering risk rating based on factors like occupation, countries, products and PEP status. It decides how much checking and how frequent reviews they need.

**Who does this work:** KYC / AML compliance teams.

**Why it's hard:** Ratings must be consistent and justified in writing for auditors and regulators.

### Key terms
- **Customer Risk Rating (CRR)**: A Low / Medium / High money-laundering risk score per customer that decides how much due diligence and monitoring they get.
- **PEP**: Politically Exposed Person: someone with a prominent public role (or their family/associates). Higher bribery and corruption risk, so EDD is required.
- **CDD / EDD**: Customer Due Diligence (standard checks) and Enhanced Due Diligence (deeper checks for high-risk customers, such as source of wealth).
- **KYC (Know Your Customer)**: Verifying who a customer is (ID, address) and understanding what they do, before and during the relationship.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Computes a customer ML/TF risk rating and justifies it for periodic KYC review.

### How it works
Weighted factor model (occupation, geography, product, channel, PEP) gives Low/Medium/High; LLM writes the justification.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/16_customer_risk_rating/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
