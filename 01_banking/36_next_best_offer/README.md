# 36 · Next Best Offer / Cross-sell

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🙋 Retail Banking & Customer Experience

## 🏦 The business problem (new to banking? start here)

**In the business today:** Banks try to offer each customer the product they most likely need next (e.g. a credit card for a new salaried customer) at the right time and channel.

**Who does this work:** Marketing / CRM analytics teams.

**Why it's hard:** Irrelevant offers annoy customers and can be seen as pushy or unfair.

### Key terms
- **Cross-sell / Next Best Offer**: Offering an existing customer the product they most likely need next.
- **Retail banking**: Banking for individuals: accounts, cards, loans, mortgages and savings.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Recommends the next best product for each customer with a personalised message.

### How it works
Python scores product propensity; a Marketing Analyst agent picks offers and a Copywriter agent drafts compliant messages.

```mermaid
flowchart LR
    IN["📄 Customers + product catalogue"] --> PY["🐍 Python<br/>Product propensity scores"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🧑‍💼 Marketing Analyst"]
        A2["✍️ Compliance-aware Copywriter"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Compliant offer messages"]
    OUT --> HU["🧑‍⚖️ Human review"]
    classDef data fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    classDef rules fill:#d1fae5,stroke:#059669,color:#064e3b
    classDef ai fill:#ede9fe,stroke:#7c3aed,color:#3b0764
    classDef llm fill:#1f2937,stroke:#111827,color:#ffffff
    classDef out fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef human fill:#f3f4f6,stroke:#6b7280,color:#111827
    class IN data
    class PY rules
    class A1,A2 ai
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
--- Propensity (top 3) ---
{
  "R-1": {
    "credit_card": 0.6,
    "mutual_fund_sip": 0.4,
    "term_insurance": 0.4
  },
  "R-2": {
    "home_loan": 0.8,
    "mutual_fund_sip": 0.6,
    "travel_card": 0.5
  },
  "R-3": {
    "mutual_fund_sip": 0.6,
    "credit_card": 0.1,
    "travel_card": 0.1
  }
}


--- Campaign ---
**Customer R-1:**
"Hey R-1, with your salary increase, a credit card could be perfect! Enjoy flexible spending and rewards. Download now in-app. Opt-out anytime."

**Customer R-2:**
"Hi R-2, we noticed your interest in home loans. Let’s discuss your options. Call us soon for a detailed conversation. Opt-out anytime."

**Customer R-3:**
"Hi R-3, your fixed deposit is maturing. Consider a mutual fund SIP for growth. Learn more in your inbox. Opt-out anytime."
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/36_next_best_offer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
