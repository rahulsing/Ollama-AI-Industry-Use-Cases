# 36 · Next Best Offer / Cross-sell

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🙋 Retail Banking & Customer Experience

## 🏦 The business problem (new to banking? start here)

**In the business today:** Banks try to offer each customer the product they most likely need next (e.g. a credit card for a new salaried customer) at the right time and channel.

**Who does this work:** Marketing / CRM analytics teams.

**Why it's hard:** Irrelevant offers annoy customers and can be seen as pushy or unfair.

### Key terms
- **Cross-sell / Next Best Offer**: Offering an existing customer the product they most likely need next.
- **Retail banking**: Banking for individuals: accounts, cards, loans, mortgages and savings.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Recommends the next best product for each customer with a personalised message.

### How it works
Python scores product propensity; a Marketing Analyst agent picks offers and a Copywriter agent drafts compliant messages.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/36_next_best_offer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
