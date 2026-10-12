# 25 · Model Risk Validation Assistant

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📜 Regulatory & Risk Reporting

## 🏦 The business problem (new to banking? start here)

**In the business today:** Banks use statistical models (e.g. credit scores) to make decisions. An independent team must test each model regularly and report whether it still works.

**Who does this work:** Model validation / Model Risk Management team.

**Why it's hard:** Validation reports are long and technical; findings must be rated and explained to non-specialists.

### Key terms
- **Model risk**: The risk of losses from a model that is wrong or misused. Regulators (e.g. SR 11-7) require independent model validation.
- **Gini / KS / PSI**: Model metrics: Gini and KS measure how well a score separates good and bad customers; PSI measures how much the population has shifted.
- **PD / LGD / EAD**: Probability of Default, Loss Given Default (% lost if default happens) and Exposure at Default (amount owed).

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Reviews a credit model's performance metrics and drafts an SR 11-7 style validation report.

### How it works
Python computes Gini, KS, PSI and calibration; Model Validator and MRM Reviewer agents write findings and ratings.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/25_model_risk_validator/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
