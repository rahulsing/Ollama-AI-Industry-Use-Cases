# 20 · Liquidity LCR / NSFR Monitor

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Chain-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📜 Regulatory & Risk Reporting

## 🏦 The business problem (new to banking? start here)

**In the business today:** Treasury tracks whether the bank has enough liquid assets to survive a 30-day stress (LCR) and stable funding for the next year (NSFR), and reports to ALCO.

**Who does this work:** Treasury / liquidity risk team, reporting to ALCO.

**Why it's hard:** Liquidity can disappear fast (as in bank runs); positions must be monitored and explained frequently.

### Key terms
- **Liquidity**: Having enough cash to pay what is due, even under stress. Banks can be solvent but still fail from lack of liquidity.
- **LCR (Liquidity Coverage Ratio)**: High-quality liquid assets / expected net cash outflows over 30 days of stress. Must be at least 100%.
- **NSFR (Net Stable Funding Ratio)**: Stable funding available / stable funding required over one year. Must be at least 100%.
- **HQLA**: High-Quality Liquid Assets: cash and assets (like government bonds) that can be sold quickly without big losses.
- **ALCO**: Asset-Liability Committee: senior managers who oversee the bank's liquidity, funding and interest-rate risk.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Calculates LCR and NSFR and produces an ALCO liquidity commentary.

### How it works
HQLA haircuts and outflow run-off rates are applied in Python; an LLM writes the ALCO note and actions.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/20_liquidity_lcr_nsfr_monitor/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
