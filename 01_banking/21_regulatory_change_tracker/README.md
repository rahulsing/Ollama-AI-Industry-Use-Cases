# 21 · Regulatory Change Impact Analyzer

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📜 Regulatory & Risk Reporting

## 🏦 The business problem (new to banking? start here)

**In the business today:** Regulators publish new rules constantly. Compliance must work out what each new rule requires, which teams and systems are affected, and what must change by the deadline.

**Who does this work:** Compliance and regulatory change management teams.

**Why it's hard:** Legal text is dense, and missing one obligation can lead to enforcement action.

### Key terms
- **Regulatory circular**: A notice from a regulator introducing new rules that banks must implement by a deadline.
- **Regulatory reporting**: Regular returns banks must send to their regulator (capital, liquidity, large exposures...). Errors can mean fines.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Reads a new regulatory circular and maps obligations to impacted business units and controls.

### How it works
Regulatory Analyst agent extracts obligations; Compliance Impact agent maps them to the bank's process inventory and gaps.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/21_regulatory_change_tracker/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
