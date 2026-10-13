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

```mermaid
flowchart LR
    QU["💬 Your question"] --> AG["🤖 LangChain agent<br/>decides which tool to call"]
    AG <-->|"🔧 calls & results"| T["🐍 Python tools<br/>lookup_transaction()<br/>reason_code_rules()"]
    IN["📄 Card transactions + reason codes"] --> T
    AG <-.->|"💬 reasoning"| LLM(["🦙 Ollama"])
    AG --> OUT["📝 Dispute summary + next steps"]
    OUT --> HU["🧑‍⚖️ Human review"]
    classDef data fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    classDef rules fill:#d1fae5,stroke:#059669,color:#064e3b
    classDef ai fill:#ede9fe,stroke:#7c3aed,color:#3b0764
    classDef llm fill:#1f2937,stroke:#111827,color:#ffffff
    classDef out fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef human fill:#f3f4f6,stroke:#6b7280,color:#111827
    class IN,QU data
    class T rules
    class AG ai
    class LLM llm
    class OUT out
    class HU human
```

<sub>🟦 data · 🟩 Python: maths & rules (auditable) · 🟪 AI: reasoning & writing · ⬛ local LLM · 🟨 result</sub>

## 💬 Sample response

Real output from `qwen2.5:7b-instruct` running locally on a laptop. LLM wording changes from run to run; the numbers from
Python stay the same.

<details>
<summary><b>Show the full output</b></summary>

````text
--- Customer ---
I ordered a laptop from TechMart Online (TX-902) on 22 Sept, it was due 29 Sept and never arrived. The merchant ignores my emails.


--- Assistant ---
Based on the provided information and the transaction details, here is the classification for the dispute:

- **Dispute Type:** Goods Not Received
- **Reason Code:** 4855
- **Evidence Required:** Expected delivery date, merchant contact attempts
- **Temporary Credit:** No (typically not applicable for goods not received disputes)
- **Summary for Back Office:** The customer ordered a laptop from TechMart Online on 22nd September, expecting delivery by 29th September. The laptop has not been received, and the merchant has not responded to the customer's emails. The customer is requesting a resolution. The merchant should be contacted first to verify the delivery status and any attempts made to contact the customer. The customer must provide the expected delivery date and evidence of their attempts to contact the merchant.

If the merchant does not respond or resolve the issue, a chargeback may be initiated. Please contact the merchant first to attempt a resolution.
````

</details>

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
