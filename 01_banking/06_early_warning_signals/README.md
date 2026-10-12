# 06 · Early Warning Signals (EWS) Monitor

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Chain-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏦 Credit & Lending

## 🏦 The business problem (new to banking? start here)

**In the business today:** For business loans, banks watch for warning signs (overdraft breaches, bounced cheques, falling sales, rating downgrades) so they can act before the borrower defaults.

**Who does this work:** Credit monitoring teams and relationship managers.

**Why it's hard:** Signals are spread across many systems; spotting them early is what makes a recovery possible.

### Key terms
- **Early Warning Signals (EWS)**: Signs that a healthy borrower may get into trouble, spotted before they miss payments.
- **SMA / watch-list**: Special Mention Account / watch-list: loans showing stress that get closer monitoring.
- **Credit risk**: The risk that a borrower does not pay back what they owe. Managing it is the core skill of any lender.
- **Covenant**: A promise in a loan agreement, e.g. 'keep debt below 3x EBITDA'. Breaking it lets the bank act early.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Detects early signs of stress in a corporate loan book and drafts watch-list commentary.

### How it works
Python flags triggers (overdraft breaches, cheque returns, rating downgrades, late financials); an LLM chain writes a watch-list note per borrower.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/06_early_warning_signals/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
