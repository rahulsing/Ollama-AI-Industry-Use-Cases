# 37 · Customer Churn Retention Agent

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🙋 Retail Banking & Customer Experience

## 🏦 The business problem (new to banking? start here)

**In the business today:** Banks watch for customers about to leave (salary stops arriving, balances drop, complaints rise) and try to keep the valuable ones.

**Who does this work:** Customer analytics and retention / customer success teams.

**Why it's hard:** Winning back a customer after they leave is much harder than keeping them.

### Key terms
- **Churn / attrition**: Customers leaving the bank or moving their main banking elsewhere.
- **Retail banking**: Banking for individuals: accounts, cards, loans, mortgages and savings.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Identifies customers likely to leave and designs retention actions.

### How it works
Churn signals scored in Python; Retention Analyst and Customer Success agents propose save offers.

```mermaid
flowchart LR
    IN["📄 Customer activity signals"] --> PY["🐍 Python<br/>Churn risk score"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🧑‍💼 Retention Analyst"]
        A2["👔 Customer Success Manager"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Retention plan + save offers"]
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

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 27 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** Which customers are at risk of leaving, and how do we keep them?

<details><summary>🐍 Python · Churn risk</summary>

```json
[
  {
    "id": "C-11",
    "churn_score": 92,
    "risk": "HIGH"
  },
  {
    "id": "C-12",
    "churn_score": 0,
    "risk": "LOW"
  },
  {
    "id": "C-13",
    "churn_score": 44,
    "risk": "MEDIUM"
  }
]
```

</details>

<details><summary>🧑‍💼 Retention Analyst (agent)</summary>

### Per-Customer Diagnosis for MEDIUM/HIGH Risk Customers

#### Customer C-11 (High Risk)
- **Tenure Years:** 8 years
- **Balance Trend (3M %):** -62%
- **Salary/Credit Stopped:** Yes
- **Logins Trend (3M %):** -70%
- **Complaints (90d):** 2
- **Products:** 3
- **Value Segment:** Affluent
- **Note:** Complained about FX fees twice

**Likely Churn Drivers:**
1. **High Churn Score (92):** This indicates a very high likelihood of churn.
2. **Long Tenure with Declining Balance:** A long tenure with a significant decline in balance suggests dissatisfaction or financial changes impacting the customer.
3. **Stopped Salary/Credit:** This could indicate a financial hardship or change in the customer's financial situation.
4. **High Frequency of Complaints (2 complaints in 90 days):** The customer has expressed dissatisfaction multiple times, which is a strong indicator of potential churn.
5. **Low Engagement (Logins Trend -70%):** Reduced login activity could suggest disengagement or dissatisfaction with the service.

#### Customer C-13 (Medium Risk)
- **Tenure Years:** 4 years
- **Balance Trend (3M %):** -35%
- **Salary/Credit Stopped:** No
- **Logins Trend (3M %):** -40%
- **Complaints (90d):** 1
- **Products:** 1
- **Value Segment:** Mass Affluent
- **Note:** Asked about mortgage rates, then went quiet

**Likely Churn Drivers:**
1. **Medium Churn Score (44):** This indicates a moderate likelihood of churn.
2. **Long Tenure with Declining Balance:** A 4-year tenure with a 35% decline in balance suggests dissatisfaction or financial changes impacting the customer.
3. **Low Engagement (Logins Trend -40%):** Reduced login activity could suggest disengagement or dissatisfaction with the service.
4. **Single Complaint (1 complaint in 90 days):** The customer has expressed dissatisfaction once, which is a warning sign.
5. **Low Product Ownership (1 product):** Limited product ownership could indicate a lack of value or satisfaction with the current offerings.
6. **Silent Period:** The customer asked about mortgage rates and then went quiet, which could suggest they are exploring alternatives or are dissatisfied with the current service.

### Summary
- **Customer C-11:** High risk due to long tenure, significant balance decline, stopped salary/credit, high frequency of complaints, and low engagement.
- **Customer C-13:** Medium risk due to long tenure, significant balance decline, low engagement, single complaint, and low product ownership.

</details>

**🦙 Ollama:**

### Retention Plan for Customer C-11

**Action:** Personalized Rate Match Offer
**Offer:** Match the customer's current rate with a competitor's rate, up to a 1% reduction.
**Owner:** Account Manager (AM) - Jane Doe
**Channel:** Email
**Script Opener:** "Dear [Customer Name], I noticed you've been experiencing some financial changes, and I wanted to ensure you're getting the best possible rate with us."
**Success Metric:** Customer retention rate post-offer acceptance.

---

### Retention Plan for Customer C-11

**Action:** Personalized Rate Match Offer
**Offer:** Match the customer's current rate with a competitor's rate, up to a 1% reduction.
**Owner:** Account Manager (AM) - Jane Doe
**Channel:** Email
**Script Opener:** "Dear [Customer Name], I noticed you've been experiencing some financial changes, and I wanted to ensure you're getting the best possible rate with us."
**Success Metric:** Customer retention rate post-offer acceptance.

---

### Retention Plan for Customer C-13

**Action:** Personalized Product Upsell
**Offer:** Offer a free consultation for a mortgage product to explore potential savings and benefits.
**Owner:** Relationship Manager (RM) - John Smith
**Channel:** Phone Call
**Script Opener:** "Hello [Customer Name], I noticed you've been exploring mortgage rates recently. I wanted to offer you a free consultation to see how we can help you save and improve your financial situation."
**Success Metric:** Number of upsold products post-consultation.

---

### Retention Plan for Customer C-13

**Action:** Personalized Product Upsell
**Offer:** Offer a free consultation for a mortgage product to explore potential savings and benefits.
**Owner:** Relationship Manager (RM) - John Smith
**Channel:** Phone Call
**Script Opener:** "Hello [Customer Name], I noticed you've been exploring mortgage rates recently. I wanted to offer you a free consultation to see how we can help you save and improve your financial situation."
**Success Metric:** Number of upsold products post-consultation.


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/37_churn_retention_agent/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
