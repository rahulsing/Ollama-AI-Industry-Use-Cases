# 33 · Banking Customer Support Agent

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🙋 Retail Banking & Customer Experience

## 🏦 The business problem (new to banking? start here)

**In the business today:** Contact centres handle millions of simple requests: balances, recent transactions, blocking a lost card, branch hours.

**Who does this work:** Contact centre / customer service.

**Why it's hard:** Simple requests clog queues; customers want 24/7 instant help, done securely.

### Key terms
- **Retail banking**: Banking for individuals: accounts, cards, loans, mortgages and savings.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Answers balance, transaction and card questions and can block a lost card.

### How it works
Agent uses `get_balance`, `recent_transactions`, `block_card` and `branch_hours` tools over a mock core-banking API.

```mermaid
flowchart LR
    QU["💬 Your question"] --> AG["🤖 LangChain agent<br/>decides which tool to call"]
    AG <-->|"🔧 calls & results"| T["🐍 Python tools<br/>get_balance()<br/>recent_transactions()<br/>block_card()<br/>branch_hours()"]
    IN["📄 Customer's accounts & cards"] --> T
    AG <-.->|"💬 reasoning"| LLM(["🦙 Ollama"])
    AG --> OUT["📝 Answer + action taken"]
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
--- You: What's my total balance? ---
Bot: Your total balance across all accounts is $5027.5. Here's a breakdown:
- Savings Account: $4215.4
- Current Account: $812.1


--- You: Show my last 3 transactions ---
Bot: Here are your last three transactions:

1. On 2026-10-09, you made a purchase of $64.2 from Amazon.
2. On 2026-10-08, you received a deposit of $2800.0 from Salary ACME Ltd.
3. On 2026-10-07, you had a direct debit of $120.0 for the Electric Co.


--- You: I lost my debit card ending 4821, please block it ---
Bot: Your card ending in 4821 has been blocked due to it being lost. A replacement card will be dispatched to you in 5 working days. Your new card reference is BLK-4821-2026. Please keep this reference for future inquiries.


--- You: What time does the Leeds branch open on Saturday? ---
Bot: The Leeds branch is open on Saturdays from 9:30 AM to 1:00 PM. For any further assistance, you can contact our 24/7 phone support at 0800 123 456.
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/33_customer_support_agent/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
