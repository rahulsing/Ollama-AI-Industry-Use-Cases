# 43 · Reconciliation Exception Agent

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 💱 Treasury, Payments & Operations

## 🏦 The business problem (new to banking? start here)

**In the business today:** Operations teams match every entry in the bank's ledger against bank statements daily. Anything that does not match (a 'break') must be investigated.

**Who does this work:** Reconciliation / operations teams.

**Why it's hard:** Breaks pile up quickly; unresolved ones can hide errors, fraud or losses.

### Key terms
- **Reconciliation**: Matching the bank's internal ledger against external statements to make sure every entry agrees. Mismatches are 'breaks'.
- **Nostro account**: An account a bank holds with another bank in a foreign currency, used to settle payments.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Matches ledger vs. bank statement entries and investigates the breaks.

### How it works
Python matches by amount/reference/date; a Recon Analyst agent classifies breaks and an Ops Lead agent assigns actions.

```mermaid
flowchart LR
    IN["📄 Ledger + bank statement"] --> PY["🐍 Python<br/>Match by amount, reference & date"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🧑‍💼 Reconciliation Analyst"]
        A2["👔 Operations Team Lead"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Break resolution plan"]
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

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 43 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** Reconcile the general ledger against the bank statement and tell me how to clear the breaks.

<details><summary>🐍 Python · Auto-matched</summary>

```json
[
  {
    "gl": "GL-1",
    "bank": "BK-1",
    "date_lag_days": 0
  },
  {
    "gl": "GL-2",
    "bank": "BK-2",
    "date_lag_days": 2
  },
  {
    "gl": "GL-4",
    "bank": "BK-4",
    "date_lag_days": 1
  }
]
```

</details>

<details><summary>🐍 Python · Breaks</summary>

```json
[
  {
    "type": "AMOUNT_MISMATCH",
    "gl": {
      "id": "GL-3",
      "date": "2026-10-03",
      "ref": "INV-1003",
      "amount": 3150.0
    },
    "bank": {
      "id": "BK-3",
      "date": "2026-10-03",
      "ref": "INV-1003",
      "amount": 3135.0
    },
    "difference": 15.0
  },
  {
    "type": "MISSING_IN_BANK",
    "gl": {
      "id": "GL-5",
      "date": "2026-10-05",
      "ref": "INV-1005",
      "amount": 4999.0
    }
  },
  {
    "type": "MISSING_IN_LEDGER",
    "bank": {
      "id": "BK-5",
      "date": "2026-10-04",
      "ref": "PAY-SUP-77",
      "amount": -9200.0
    }
  },
  {
    "type": "MISSING_IN_LEDGER",
    "bank": {
      "id": "BK-6",
      "date": "2026-10-06",
      "ref": "BANK CHARGES",
      "amount": -45.0
    }
  }
]
```

</details>

<details><summary>🧑‍💼 Reconciliation Analyst (agent)</summary>

### Break 1: AMOUNT_MISMATCH
- **GL Entry:**
  - ID: GL-3
  - Date: 2026-10-03
  - Ref: INV-1003
  - Amount: 3150.0
- **Bank Entry:**
  - ID: BK-3
  - Date: 2026-10-03
  - Ref: INV-1003
  - Amount: 3135.0
- **Difference:** 15.0

**Root Cause:** **Short Payment / Fee**

**Evidence:**
- The difference in the amount is relatively small (15.0), which is consistent with a fee or a short payment. This could be a bank processing fee, a rounding error, or a small discrepancy that is typically associated with short payments or fees.

### Break 2: MISSING_IN_BANK
- **GL Entry:**
  - ID: GL-5
  - Date: 2026-10-05
  - Ref: INV-1005
  - Amount: 4999.0
- **Bank Entry:**
  - ID: BK-5
  - Date: 2026-10-05
  - Ref: INV-1005
  - Amount: 0.0
- **Difference:** 4999.0

**Root Cause:** **Unrecorded Bank Charge**

**Evidence:**
- The GL entry is present, but the corresponding bank entry is missing. This suggests that there might be an unrecorded bank charge or a transaction that was not properly reflected in the bank statement. The large amount (4999.0) indicates that it is likely a significant transaction that should have been recorded.

### Break 3: MISSING_IN_LEDGER
- **Bank Entry:**
  - ID: BK-5
  - Date: 2026-10-04
  - Ref: PAY-SUP-77
  - Amount: -9200.0
- **GL Entry:**
  - ID: GL-5
  - Date: 2026-10-04
  - Ref: PAY-SUP-77
  - Amount: 0.0
- **Difference:** -9200.0

**Root Cause:** **Timing**

**Evidence:**
- The bank entry is present, but the corresponding GL entry is missing. This suggests that the transaction was recorded in the bank statement but not in the GL. The negative amount (-9200.0) indicates that it is a payment or a credit entry. The timing discrepancy could be due to a delay in recording the transaction in the GL, possibly due to system processing delays or manual entry delays.

### Break 4: MISSING_IN_LEDGER
- **Bank Entry:**
  - ID: BK-6
  - Date: 2026-10-06
  - Ref: BANK CHARGES
  - Amount: -45.0
- **GL Entry:**
  - ID: GL-6
  - Date: 2026-10-06
  - Ref: BANK CHARGES
  - Amount: 0.0
- **Difference:** -45.0

**Root Cause:** **Timing**

**Evidence:**
- The bank entry is present, but the corresponding GL entry is missing. This suggests that the transaction was recorded in the bank statement but not in the GL. The negative amount (-45.0) indicates that it is a bank charge or a fee. The timing discrepancy could be due to a delay in recording the transaction in the GL, possibly due to system processing delays or manual entry delays.

</details>

**🦙 Ollama:**

### Action Table and Summary

#### Break 1: AMOUNT_MISMATCH
- **Type:** AMOUNT_MISMATCH
- **GL Entry:**
  - ID: GL-3
  - Date: 2026-10-03
  - Ref: INV-1003
  - Amount: 3150.0
- **Bank Entry:**
  - ID: BK-3
  - Date: 2026-10-03
  - Ref: INV-1003
  - Amount: 3135.0
- **Difference:** 15.0
- **Root Cause:** Short Payment / Fee
- **Evidence:** The difference is relatively small (15.0), consistent with a fee or a short payment.
- **Resolution Action:** Journal Entry
- **Owner:** Jane Doe
- **Priority:** Low
- **Summary:** This break is likely due to a small fee or short payment. A journal entry will be made to adjust the GL to match the bank statement.

#### Break 2: MISSING_IN_BANK
- **Type:** MISSING_IN_BANK
- **GL Entry:**
  - ID: GL-5
  - Date: 2026-10-05
  - Ref: INV-1005
  - Amount: 4999.0
- **Bank Entry:**
  - ID: BK-5
  - Date: 2026-10-05
  - Ref: INV-1005
  - Amount: 0.0
- **Difference:** 4999.0
- **Root Cause:** Unrecorded Bank Charge
- **Evidence:** The GL entry is present, but the corresponding bank entry is missing, suggesting an unrecorded bank charge.
- **Resolution Action:** Bank Claim
- **Owner:** John Smith
- **Priority:** High
- **Summary:** This break indicates a significant unrecorded transaction. A bank claim will be filed to resolve the discrepancy.

#### Break 3: MISSING_IN_LEDGER
- **Type:** MISSING_IN_LEDGER
- **Bank Entry:**
  - ID: BK-5
  - Date: 2026-10-04
  - Ref: PAY-SUP-77
  - Amount: -9200.0
- **GL Entry:**
  - ID: GL-5
  - Date: 2026-10-04
  - Ref: PAY-SUP-77
  - Amount: 0.0
- **Difference:** -9200.0
- **Root Cause:** Timing
- **Evidence:** The bank entry is present, but the corresponding GL entry is missing, indicating a timing discrepancy.
- **Resolution Action:** Journal Entry
- **Owner:** Emily Johnson
- **Priority:** Medium
- **Summary:** This break is due to a timing issue. A journal entry will be made to record the missing GL entry.

#### Break 4: MISSING_IN_LEDGER
- **Type:** MISSING_IN_LEDGER
- **Bank Entry:**
  - ID: BK-6
  - Date: 2026-10-06
  - Ref: BANK CHARGES
  - Amount: -45.0
- **GL Entry:**
  - ID: GL-6
  - Date: 2026-10-06
  - Ref: BANK CHARGES
  - Amount: 0.0
- **Difference:** -45.0
- **Root Cause:** Timing
- **Evidence:** The bank entry is present, but the corresponding GL entry is missing, indicating a timing discrepancy.
- **Resolution Action:** Journal Entry
- **Owner:** Michael Brown
- **Priority:** Medium
- **Summary:** This break is due to a timing issue. A journal entry will be made to record the missing GL entry.

### Overall Recon Summary
- **Break 1:** AMOUNT_MISMATCH - Resolved by Journal Entry, Low Priority
- **Break 2:** MISSING_IN_BANK - Resolved by Bank Claim, High Priority
- **Break 3:** MISSING_IN_LEDGER - Resolved by Journal Entry, Medium Priority
- **Break 4:** MISSING_IN_LEDGER - Resolved by Journal Entry, Medium Priority

This summary outlines the resolution actions, owners, and priorities for each break, ensuring that the discrepancies are addressed efficiently.


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/43_reconciliation_exception_agent/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
