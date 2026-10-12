# 34 · Complaint Classifier & Router

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Structured%20extraction-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🙋 Retail Banking & Customer Experience

## 🏦 The business problem (new to banking? start here)

**In the business today:** Complaints arrive by email, phone and social media. Each must be categorised, prioritised and routed to the right team within regulatory deadlines.

**Who does this work:** Complaints handling teams, with conduct/compliance oversight.

**Why it's hard:** Misrouted or late complaints breach rules; complaints from vulnerable customers need urgent attention.

### Key terms
- **Customer complaint handling**: Regulators set deadlines (e.g. resolve within 30 days) and require reporting of complaint trends.
- **Vulnerable customer**: Someone more likely to suffer harm (e.g. due to age, illness, bereavement). Banks must take extra care with them.
- **Mis-selling**: Selling a product that is unsuitable or not properly explained. Leads to compensation and regulatory fines.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Classifies complaints by product, issue, severity and regulatory reportability and routes them.

### How it works
Structured output schema plus routing table; SLA computed from severity.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/34_complaint_classifier/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
