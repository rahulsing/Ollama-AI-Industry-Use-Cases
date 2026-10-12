# 02 · Policy Coverage Q&A (RAG)

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-RAG-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🛡️ Insurance · **Category:** 🙋 Policy & Customer Service

## 🛡️ The business problem (new to insurance? start here)

**In the business today:** Customers call the helpline asking 'am I covered for this?'. Staff check the policy wording and the customer's schedule, then explain the answer and the excess.

**Who does this work:** Contact centre and claims helpline teams.

**Why it's hard:** Policy wordings are long and full of exclusions and conditions. Answers depend on which add-ons the customer bought, and wrong answers lead to complaints.

### Key terms
- **Policy wording / schedule**: The wording is the full contract (what is and isn't covered); the schedule lists this customer's chosen covers and limits.
- **Exclusion**: Something the policy specifically does not cover, e.g. wear and tear.
- **Add-on cover**: Optional extra cover bought on top of the core policy, e.g. accidental damage.
- **Excess (deductible)**: The amount the customer pays towards each claim before the insurer pays the rest.

More terms: [Insurance Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Answers 'am I covered?' questions from the policy wording and the customer's schedule, with clause citations.

### How it works
Relevant clauses are retrieved (the schedule and excess are always included); the LLM fills a coverage checklist (matching section, conditions met) and checks each exclusion sentence; Python decides COVERED / NOT COVERED from the customer's schedule; the LLM explains the decision with citations.

## Run
```bash
# from the repo root, with Ollama running
python 03_insurance/02_policy_coverage_qa/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Insurance use cases](../README.md#-use-cases) · [All industries](../../README.md)
