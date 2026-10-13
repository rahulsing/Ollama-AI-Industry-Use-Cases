# 35 · Personal Finance Coach

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Chain-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🙋 Retail Banking & Customer Experience

## 🏦 The business problem (new to banking? start here)

**In the business today:** Banks increasingly help customers manage money, analysing spending and suggesting budgets and savings inside the banking app.

**Who does this work:** Digital banking / customer engagement teams.

**Why it's hard:** Customers want personal, practical advice, not generic tips.

### Key terms
- **50/30/20 rule**: A budgeting rule: 50% of income on needs, 30% on wants, 20% on savings.
- **Retail banking**: Banking for individuals: accounts, cards, loans, mortgages and savings.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Analyses spending and gives personalised saving tips and a budget.

### How it works
Transactions are categorised and summarised in Python; the LLM coaches against the 50/30/20 rule.

```mermaid
flowchart LR
    IN["📄 Income + transactions"] --> PY["🐍 Python<br/>Spend by category · 50/30/20 check"]
    PY -->|"✅ decision & numbers"| CH["🔗 LangChain prompt<br/>explain, don't decide"]
    CH <-.->|"💬"| LLM(["🦙 Ollama"])
    CH --> OUT["📝 Personal coaching tips"]
    OUT --> HU["🧑‍⚖️ Human review"]
    classDef data fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    classDef rules fill:#d1fae5,stroke:#059669,color:#064e3b
    classDef ai fill:#ede9fe,stroke:#7c3aed,color:#3b0764
    classDef llm fill:#1f2937,stroke:#111827,color:#ffffff
    classDef out fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef human fill:#f3f4f6,stroke:#6b7280,color:#111827
    class IN data
    class PY rules
    class CH ai
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
--- Spending analysis ---
{
  "income": 5200,
  "spent": 4048,
  "pct_of_income": {
    "needs": 54,
    "wants": 20,
    "savings": 4
  },
  "target_50_30_20": {
    "needs": 50,
    "wants": 30,
    "savings": 20
  },
  "top_wants": [
    [
      "Amazon",
      275.0
    ],
    [
      "Restaurants",
      230.0
    ],
    [
      "Zara",
      140.0
    ],
    [
      "Uber Eats",
      116.0
    ],
    [
      "Deliveroo",
      89.0
    ]
  ],
  "subscriptions_total": 90.0,
  "takeaway_total": 205.0
}


--- Coaching ---
**2-line Summary vs 50/30/20 Rule:**
Your current spending is 54% on needs, 20% on wants, and 4% on savings, which deviates from the 50/30/20 rule. To better align, you can adjust your budget to save more and reduce spending on non-essential items.

**4 Specific Saving Tips with Estimated Monthly Savings:**
1. **Cut Back on Takeout Meals:** Reduce takeaway orders by $100/month.
2. **Cancel Unnecessary Subscriptions:** Save $30/month by unsubscribing from unused services.
3. **Reduce Shopping Spree:** Cut down on shopping by $50/month.
4. **Automate Savings:** Set up an automatic transfer of $100/month into a savings account.

**Suggested Monthly Budget Table:**
| Category       | Current Spending | Target Spending | Monthly Savings |
|----------------|-----------------|----------------|----------------|
| Needs          | $2,724          | $2,600         | $124           |
| Wants          | $1,024          | $1,560         | $536           |
| Savings        | $208            | $1,040         | $832           |
| Subscriptions  | $90             | $0             | $90            |
| Takeaway       | $205            | $0             | $205           |
| **Total**      | **$4,048**      | **$4,200**     | **$1,155**     |

**Encouraging Closing Line:**
Keep moving forward with small, consistent changes, and you'll see significant progress in your financial health!
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/35_personal_finance_coach/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
