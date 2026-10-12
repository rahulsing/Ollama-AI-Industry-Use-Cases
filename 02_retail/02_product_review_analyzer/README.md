# 02 · Product Review Analyzer

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Structured%20extraction-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🛒 Retail · **Category:** 🙋 Customer Insight

## 🛒 The business problem (new to retail? start here)

**In the business today:** Product and quality teams read customer reviews to spot recurring problems, fix product listings and catch safety issues early.

**Who does this work:** Product managers, quality assurance and customer care teams.

**Why it's hard:** Popular products get thousands of reviews. Important signals, like a burning smell or a cracked blade, can be buried among comments about delivery or colour.

### Key terms
- **Customer reviews / sentiment**: Star ratings and comments; sentiment is whether they are positive, neutral or negative.
- **Product defect**: A fault in the product itself (leaks, breakage), as opposed to a matter of taste.
- **Product recall**: Withdrawing an unsafe product from sale and from customers. Safety complaints must be escalated fast.

More terms: [Retail Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Turns customer reviews into sentiment, complaint themes, defects and safety issues.

### How it works
Each review is classified into a Pydantic schema, Python aggregates the counts, and an LLM chain writes the quality report with escalation of safety concerns.

## Run
```bash
# from the repo root, with Ollama running
python 02_retail/02_product_review_analyzer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Retail use cases](../README.md#-use-cases) · [All industries](../../README.md)
