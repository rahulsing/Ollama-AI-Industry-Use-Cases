# 17 · Money Mule Account Detector

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🕵️ Financial Crime & Compliance

## 🏦 The business problem (new to banking? start here)

**In the business today:** Fraudsters use 'mule' accounts to receive stolen money and pass it on quickly. Banks look for accounts where money comes in from many people and leaves almost immediately.

**Who does this work:** Fraud and financial crime teams.

**Why it's hard:** Mules are often young people being exploited, so action must stop the fraud and also protect them.

### Key terms
- **Money mule**: A person whose account is used to receive and quickly pass on stolen money, often recruited with 'easy money' offers.
- **APP fraud**: Authorised Push Payment fraud: victims are tricked into sending money themselves, e.g. a fake investment.
- **Typology**: A known pattern of financial crime, e.g. structuring, mule accounts or trade-based laundering.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Identifies likely mule accounts from pass-through behaviour and new-account signals.

### How it works
Python computes pass-through ratio, account age and counterparties; Fraud Analyst and Investigator agents rank and recommend actions.

```mermaid
flowchart LR
    IN["📄 Account activity"] --> PY["🐍 Python<br/>Pass-through ratio · account age · counterparties"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🧑‍💼 Fraud Analyst"]
        A2["🕵️ Fraud Investigator"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Ranked mule suspects + actions"]
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

## 💬 Sample conversation

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 39 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** Which of these accounts look like money mules, and what should we do about them?

<details><summary>🐍 Python · Mule scores</summary>

```json
[
  {
    "acct": "A-100",
    "pass_through_ratio": 0.98,
    "mule_score": 100,
    "tier": "HIGH"
  },
  {
    "acct": "A-102",
    "pass_through_ratio": 0.98,
    "mule_score": 100,
    "tier": "HIGH"
  },
  {
    "acct": "A-101",
    "pass_through_ratio": 0.9,
    "mule_score": 25,
    "tier": "LOW"
  },
  {
    "acct": "A-103",
    "pass_through_ratio": 0.4,
    "mule_score": 0,
    "tier": "LOW"
  }
]
```

</details>

<details><summary>🧑‍💼 Fraud Analyst (agent)</summary>

### Per-account Explanation:

#### Account A-100
- **Age of Account (21 days)**: The account is relatively new, which is a common characteristic of money mules. Mules often open new accounts to avoid detection.
- **Inflow and Outflow ($18,400 and $18,100 respectively)**: The inflow and outflow are nearly identical, indicating a high pass-through ratio (98%). This is a strong indicator of mule activity, as mules typically transfer funds quickly without retaining much value.
- **Unique Senders (27)**: A high number of unique senders suggests that the account is being used to process a large volume of transactions, which is typical for mules.
- **Average Hold Time (3 hours)**: The short average hold time is another red flag, as mules often move funds quickly to avoid scrutiny.
- **Age of Holder (19 years)**: The young age of the holder is suspicious, as older individuals are less likely to be recruited for mule jobs.
- **Devices Shared With (2)**: Sharing devices can indicate a lack of personal investment in the account, which is common among mules.
- **Crypto or Cash Out Percentage (85%)**: A high percentage of crypto or cash out suggests that the account is being used to process digital assets, which is a common method for mules to avoid detection.
- **Mule Score (100)**: The high mule score and "HIGH" tier indicate a strong likelihood that this account is being used as a money mule.

#### Account A-101
- **Age of Account (1400 days)**: The account is quite old, which is unusual for a mule account. Mules typically open new accounts to avoid detection.
- **Inflow and Outflow ($5,200 and $4,700 respectively)**: The pass-through ratio is 90%, which is high but not as extreme as A-100. This suggests some level of mule activity but not as intense.
- **Unique Senders (2)**: A low number of unique senders is less suspicious compared to A-100, but it still indicates some level of mule activity.
- **Average Hold Time (240 hours)**: The long average hold time is less suspicious compared to A-100, but it still indicates some level of mule activity.
- **Age of Holder (41 years)**: The older age of the holder is less suspicious compared to A-100, but it still raises some concerns.
- **Devices Shared With (0)**: No shared devices suggest a higher level of personal investment, which is less common among mules.
- **Crypto or Cash Out Percentage (5%)**: A low percentage of crypto or cash out suggests that the account is being used for more traditional money mule activities.
- **Mule Score (25)**: The lower mule score and "LOW" tier indicate a lower likelihood that this account is being used as a money mule, but it still warrants further investigation.

#### Account A-102
- **Age of Account (60 days)**: The account is relatively new, which is a common characteristic of money mules.
- **Inflow and Outflow ($9,100 and $8,900 respectively)**: The inflow and outflow are nearly identical, indicating a high pass-through ratio (98%). This is a strong indicator of mule activity.
- **Unique Senders (11)**: A high number of unique senders suggests that the account is being used to process a large volume of transactions.
- **Average Hold Time (12 hours)**: The short average hold time is another red flag, as mules often move funds quickly to avoid scrutiny.
- **Age of Holder (22 years)**: The young age of the holder is suspicious, as older individuals are less likely to be recruited for mule jobs.
- **Devices Shared With (1)**: Sharing devices can indicate a lack of personal investment in the account, which is common among mules.
- **Crypto or Cash Out Percentage (60%)**: A high percentage of crypto or cash out suggests that the account is being used to process digital assets, which is a common method for mules to avoid detection.
- **Mule Score (100)**: The high mule score and "HIGH" tier indicate a strong likelihood that this account is being used as a money mule.

#### Account A-103
- **Age of Account (700 days)**: The account is quite old, which is unusual for a mule account. Mules typically open new accounts to avoid detection.
- **Inflow and Outflow ($30,000 and $12,000 respectively)**: The pass-through ratio is 40%, which is significantly lower than the other accounts. This suggests that the account is not being used as a mule account.
- **Unique Senders (4)**: A low number of unique senders is less suspicious compared to the other accounts.
- **Average Hold Time (500 hours)**: The long average hold time is less suspicious compared to the other accounts.
- **Age of Holder (55 years)**: The older age of the holder is less suspicious compared to the other accounts.
- **Devices Shared With (0)**: No shared devices suggest a higher level of personal investment, which is less common among mules.
- **Crypto or Cash Out Percentage (0%)**: A low percentage of crypto or cash out suggests that the account is not being used for mule activities.
- **Mule Score (0)**: The low mule score and "LOW" tier indicate a very low likelihood that this account is being used as a money mule.

</details>

**🦙 Ollama:**

### Prioritised Action List

#### Account A-100
- **Action**: **Close & Report**
- **Reason**: High mule score (100), "HIGH" tier, and strong indicators of mule activity such as high pass-through ratio, short average hold time, and young age of the holder.

#### Account A-101
- **Action**: **Contact Customer for Further Investigation**
- **Reason**: Lower mule score (25), "LOW" tier, and less extreme indicators of mule activity. Further investigation is warranted to confirm the nature of the account.

#### Account A-102
- **Action**: **Close & Report**
- **Reason**: High mule score (100), "HIGH" tier, and strong indicators of mule activity such as high pass-through ratio, short average hold time, and young age of the holder.

#### Account A-103
- **Action**: **Safeguarding Message for Possibly-Exploited Young Holder**
- **Reason**: Low mule score (0), "LOW" tier, and no significant indicators of mule activity. The account holder is older, and the pass-through ratio is low, suggesting the account is not being used for mule activities. However, the young age of the holder warrants a safeguarding message to ensure they are not being exploited.

### Summary of Actions
1. **Account A-100**: Close & Report
2. **Account A-101**: Contact Customer for Further Investigation
3. **Account A-102**: Close & Report
4. **Account A-103**: Safeguarding Message for Possibly-Exploited Young Holder


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/17_mule_account_detector/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
