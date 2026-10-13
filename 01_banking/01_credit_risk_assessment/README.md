# 01 · Credit Risk Assessment Agent

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏦 Credit & Lending

## 🏦 The business problem (new to banking? start here)

**In the business today:** When someone applies for a personal loan, the bank must decide: will this person pay us back? Credit analysts look at income, existing debts, credit bureau history and the bank's lending policy, then a more senior approver signs off.

**Who does this work:** Retail credit analysts and credit approvers (Risk department).

**Why it's hard:** Thousands of applications arrive daily. Decisions must be fast, consistent and explainable to the customer and the regulator.

### Key terms
- **Credit risk**: The risk that a borrower does not pay back what they owe. Managing it is the core skill of any lender.
- **DTI (Debt-to-Income)**: Monthly debt payments divided by monthly income. A DTI of 40% means 40% of income already goes to repayments.
- **LTI (Loan-to-Income)**: Loan amount divided by annual income. Caps how big a loan is relative to what the borrower earns.
- **EMI**: Equated Monthly Instalment: the fixed monthly repayment on a loan, covering interest and principal.
- **Credit score / bureau score**: A number (e.g. 300-900) from a credit bureau summarising a person's repayment history. Higher means lower risk.
- **Risk grade**: An internal rating (A, B, C...) that groups borrowers by riskiness and drives approval and pricing.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Scores a retail loan applicant and writes a credit decision memo with risk grade and conditions.

### How it works
Python computes DTI, LTI, PD-style score and policy breaches; a Credit Analyst agent interprets the numbers and a Chief Risk Officer agent issues approve / decline / refer with rationale.

```mermaid
flowchart LR
    IN["📄 Loan application + lending policy"] --> PY["🐍 Python<br/>DTI · LTI · risk score · policy breaches"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🧑‍💼 Retail Credit Analyst"]
        A2["👔 Chief Risk Officer"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Credit decision memo"]
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
--- Computed metrics ---
{
  "policy_assessment": {
    "dti": "29.6% vs max 50% -> WITHIN LIMIT (comfortable)",
    "lti": "0.67x vs max 5x -> WITHIN LIMIT (comfortable)",
    "credit_score": "742 vs min 680 -> PASS"
  },
  "new_emi": 26391,
  "dti_pct": 29.6,
  "lti": 0.67,
  "risk_score": 66.0,
  "risk_grade": "B",
  "policy_breaches": [
    "None"
  ]
}


--- Credit decision memo ---
**Credit Decision Memo**

**Decision:** APPROVE WITH CONDITIONS

**Risk Grade:** B

**Rationale:** The applicant meets the bank's policy criteria with a debt-to-income ratio (DTI) of 29.6%, a loan-to-income (LTI) ratio of 0.67x, and a credit score of 742, all within acceptable limits. However, the proposed monthly EMI of 26,391, combined with an existing EMI of 18,000, poses a risk of financial strain. The salaried employment and the significant loan purpose for home renovation add to the risk profile.

**Conditions/Covenants:**
1. The applicant must maintain a minimum credit score of 700 throughout the loan term.
2. The applicant must not take on any additional debt without prior approval from the bank.
3. The applicant must provide regular updates on the home renovation project and its progress.
4. The applicant must maintain a minimum liquid asset reserve equivalent to 3 months of the proposed EMI.

**Recommended Pricing Adjustment:** 
- Increase the interest rate by 0.5% to reflect the higher risk associated with the high EMI and significant loan purpose.

**Memo End**

This decision balances the applicant's strong credit profile with the need to manage potential financial stress and risk. The conditions and covenants are designed to ensure that the applicant can manage the loan effectively while minimizing risk to the bank.
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/01_credit_risk_assessment/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
