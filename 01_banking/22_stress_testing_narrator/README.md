# 22 · Stress Testing Scenario Narrator

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📜 Regulatory & Risk Reporting

## 🏦 The business problem (new to banking? start here)

**In the business today:** Banks simulate severe recessions to check they would still have enough capital, then explain the results to the board and regulator.

**Who does this work:** Stress testing / ICAAP teams (Risk), economists, the board risk committee.

**Why it's hard:** Results must be turned into a clear story of what breaks, why, and what management would do.

### Key terms
- **Stress testing**: Simulating a severe recession (GDP down, unemployment up) to check the bank would still have enough capital.
- **ICAAP**: Internal Capital Adequacy Assessment Process: the bank's own assessment of the capital it needs, reviewed by the regulator.
- **PD / LGD / EAD**: Probability of Default, Loss Given Default (% lost if default happens) and Exposure at Default (amount owed).
- **Capital ratio**: Capital / RWA. E.g. a CET1 ratio of 12% vs a 7% minimum means 5 percentage points of headroom.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Applies macro stress scenarios to a portfolio and writes the stress-test narrative for the board.

### How it works
Python shocks PD/LGD by scenario; an Economist agent describes scenarios and a Risk Reporter agent explains capital impact.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/22_stress_testing_narrator/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
