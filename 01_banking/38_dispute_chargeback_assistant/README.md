# 38 · Dispute & Chargeback Assistant

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🙋 Retail Banking & Customer Experience

## 🏦 The business problem (new to banking? start here)

**In the business today:** When a customer disputes a card payment (item never arrived, cancelled subscription still charged), the bank raises a chargeback through Visa/Mastercard.

**Who does this work:** Card disputes / chargeback operations.

**Why it's hard:** Each network has strict reason codes, deadlines and evidence rules; mistakes mean the bank loses the dispute.

### Key terms
- **Chargeback**: Reversing a card payment through the card network (Visa/Mastercard) when a customer has a valid dispute.
- **Reason code**: The card network's code for why a chargeback is raised (fraud, goods not received...), each with its own evidence rules.
- **MCC**: Merchant Category Code: a 4-digit code describing what kind of business a card merchant is, e.g. 5411 grocery, 7995 gambling.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Guides a card dispute, determines the reason code and drafts the chargeback case.

### How it works
Agent uses `lookup_transaction` and `reason_code_rules` tools and drafts the dispute summary.

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/38_dispute_chargeback_assistant/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
