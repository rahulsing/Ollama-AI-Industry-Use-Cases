# 19 · Basel III Capital Calculator Assistant

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📜 Regulatory & Risk Reporting

## 🏦 The business problem (new to banking? start here)

**In the business today:** Banks must hold enough capital against risky assets. Treasury and risk teams constantly ask: what are our ratios, and what happens if we lend more?

**Who does this work:** Capital management (Treasury / Finance / Risk).

**Why it's hard:** Capital is expensive and limited; every lending decision consumes some, so quick what-if answers matter.

### Key terms
- **Basel III**: The global rulebook for how much capital and liquidity banks must hold, set by the Basel Committee.
- **Capital (CET1, Tier 1, Tier 2)**: The bank's own money that absorbs losses. CET1 (mostly shareholders' equity) is the highest-quality layer.
- **RWA (Risk-Weighted Assets)**: Assets adjusted for risk: a government bond might count 0%, an unrated corporate loan 100%. Capital requirements are a % of RWA.
- **Capital ratio**: Capital / RWA. E.g. a CET1 ratio of 12% vs a 7% minimum means 5 percentage points of headroom.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Answers capital-adequacy questions by computing RWA, CET1, Tier 1 and total capital ratios.

### How it works
Agent uses `compute_rwa` and `capital_ratios` tools on the sample balance sheet and explains headroom vs. minimums.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/19_basel_capital_calculator/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
