# 23 · IFRS 9 ECL Calculator & Explainer

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📜 Regulatory & Risk Reporting

## 🏦 The business problem (new to banking? start here)

**In the business today:** Under IFRS 9, banks set aside provisions for loans they expect to go bad, based on each loan's stage and probability of default.

**Who does this work:** Credit risk / impairment team and Finance.

**Why it's hard:** Provisions directly hit profit; auditors challenge every staging decision and number.

### Key terms
- **IFRS 9**: The accounting standard that makes banks set aside provisions for expected (not just actual) loan losses.
- **ECL (Expected Credit Loss)**: The loss a bank expects on a loan: PD x LGD x EAD. Booked as a provision in the accounts.
- **PD / LGD / EAD**: Probability of Default, Loss Given Default (% lost if default happens) and Exposure at Default (amount owed).
- **IFRS 9 stages**: Stage 1 performing (12-month ECL), Stage 2 significant increase in credit risk (lifetime ECL), Stage 3 credit-impaired.
- **SICR**: Significant Increase in Credit Risk since the loan was made. Moves a loan from Stage 1 to Stage 2.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Stages loans (1/2/3) and calculates expected credit loss, then explains drivers.

### How it works
Agent calls `stage_loan` and `calculate_ecl` tools; explains SICR triggers and 12-month vs. lifetime ECL.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/23_ifrs9_ecl_calculator/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
