# 05 · Collections & Recovery Strategist

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏦 Credit & Lending

## 🏦 The business problem (new to banking? start here)

**In the business today:** When customers miss loan payments, the collections team decides who to contact, how (SMS, call, letter), how often, and what to offer (payment plan, settlement).

**Who does this work:** Collections strategy and operations teams.

**Why it's hard:** Too soft loses money; too aggressive harms customers and breaks conduct rules, especially for customers in hardship.

### Key terms
- **Collections**: The team that contacts customers who have missed payments and agrees ways to pay, e.g. payment plans.
- **DPD (Days Past Due)**: How many days a payment is late. 30, 60 and 90 DPD are the standard warning milestones.
- **Delinquency / NPA / NPL**: A delinquent loan is behind on payments. After about 90 DPD it becomes a Non-Performing Asset / Loan.
- **Propensity to pay**: A prediction of how likely a late customer is to pay, used to choose the right collection approach.
- **Vulnerable customer**: Someone more likely to suffer harm (e.g. due to age, illness, bereavement). Banks must take extra care with them.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Segments delinquent accounts and designs a compliant, empathetic collection strategy per segment.

### How it works
Accounts are bucketed by DPD and propensity-to-pay; a Collections Strategist agent designs treatments and a Conduct Reviewer agent checks for fair-treatment issues.

```mermaid
flowchart LR
    IN["📄 Overdue accounts"] --> PY["🐍 Python<br/>DPD bucket · propensity to pay · segment"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["♟️ Collections Strategist"]
        A2["🔍 Conduct & Fair Treatment Reviewer"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Fair collections strategy"]
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
--- Segments ---
{
  "1-29 (early) | PTP High": [
    {
      "id": "L-01",
      "outstanding": 2400,
      "hardship": false
    },
    {
      "id": "L-04",
      "outstanding": 900,
      "hardship": false
    }
  ],
  "30-59 | PTP Medium": [
    {
      "id": "L-02",
      "outstanding": 8100,
      "hardship": false
    }
  ],
  "60-89 | PTP Medium": [
    {
      "id": "L-03",
      "outstanding": 15200,
      "hardship": true
    }
  ],
  "90+ (NPA) | PTP Low": [
    {
      "id": "L-05",
      "outstanding": 22000,
      "hardship": false
    }
  ],
  "30-59 | PTP High": [
    {
      "id": "L-06",
      "outstanding": 4300,
      "hardship": true
    }
  ]
}


--- Collections strategy ---
| Segment                  | Channel       | Frequency | Offer                                      | Escalation Trigger                                                                 |
|--------------------------|---------------|-----------|--------------------------------------------|------------------------------------------------------------------------------------|
| 1-29 (early)             | PTP High      | Once       | No immediate action; monitor for changes  | If outstanding amount remains unchanged after 30 days, consider a friendly reminder |
| 30-59                    | PTP Medium    | Twice      | Offer a payment plan (3-6 months)         | If no payment received after second reminder, escalate to a collection officer      |
| 60-89                    | PTP Medium    | Three times| Offer a payment plan (3-6 months)         | If no payment received after third reminder, escalate to a collection officer      |
| 90+ (NPA)                | PTP Low       | Twice      | Offer a settlement (70-80% of outstanding) | If no payment received after second reminder, escalate to a legal advisor           |
| 30-59 hardship=true      | PTP Medium    | Twice      | Offer a payment plan (3-6 months)         | If no payment received after second reminder, escalate to a collection officer      |

### Conduct Notes
1. **Early Stage (1-29 Days):** For accounts flagged as `hardship=true`, the initial approach should be gentle and supportive. The focus should be on understanding the customer's situation and offering flexible payment options. If the account remains unchanged after 30 days, a friendly reminder should be issued, but aggressive actions should be avoided.

2. **30-59 Days:** For accounts flagged as `hardship=true`, the offer of a payment plan should be made twice. If no payment is received after the second reminder, escalation to a collection officer should occur. The collection officer should be trained to handle these cases with empathy and understanding, ensuring that the customer feels supported rather than pressured.

3. **60-89 Days:** For accounts flagged as `hardship=true`, the offer of a payment plan should be made three times. If no payment is received after the third reminder, escalation to a collection officer should occur. The collection officer should follow the same approach as in the 30-59 days segment, focusing on understanding the customer's situation and offering support.

4. **90+ Days (NPA):** For accounts flagged as `hardship=true`, the offer of a settlement should be made twice. If no payment is received after the second reminder, escalation to a legal advisor should occur. The legal advisor should be trained to handle these cases with sensitivity, ensuring that the customer is treated fairly and with respect.

5. **General Guidelines:** All collection officers should be trained to recognize and handle `hardship=true` cases with empathy and understanding. They should avoid aggressive language and tactics, focusing on building a supportive relationship with the customer. Regular training and support should be provided to ensure that all staff are equipped to handle these cases effectively.

By implementing these strategies, we can ensure that vulnerable customers are treated fairly and with respect, while still maintaining a balanced approach to debt collection.
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/05_collections_strategy_agent/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
