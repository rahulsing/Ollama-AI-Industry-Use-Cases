# 49 · Internal Audit Assistant

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏢 Enterprise Analytics & Audit

## 🏦 The business problem (new to banking? start here)

**In the business today:** Internal auditors test samples of transactions to check controls worked, e.g. that a different person approved each payment within their authority.

**Who does this work:** Internal audit.

**Why it's hard:** Testing and report writing are labour-intensive; findings must follow a strict format for the audit committee.

### Key terms
- **Internal audit**: The independent team that tests whether the bank's controls work and reports to the board's audit committee.
- **Maker-checker**: A control where one person enters a transaction and a different person approves it (segregation of duties).

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Tests a sample of transactions against controls and drafts audit findings.

### How it works
Python runs control tests (maker-checker, limits, SoD); Auditor and Audit Manager agents write findings with risk ratings.

```mermaid
flowchart LR
    IN["📄 Payment sample + approval limits"] --> PY["🐍 Python<br/>Control tests: maker-checker, limits, SoD"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🔍 Internal Auditor"]
        A2["👔 Audit Manager"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Audit report with ratings"]
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

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 45 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** Test this quarter's payment sample against our approval controls and write the audit findings.

<details><summary>🐍 Python · Control testing</summary>

```json
{
  "sample_size": 6,
  "exceptions": [
    {
      "id": "P-02",
      "control": "Maker-checker / segregation of duties",
      "detail": "Same user made and approved"
    },
    {
      "id": "P-03",
      "control": "Delegation of authority",
      "detail": "310,000 > manager limit"
    },
    {
      "id": "P-04",
      "control": "Vendor master",
      "detail": "Payee not in approved vendor master"
    },
    {
      "id": "P-05",
      "control": "Vendor master",
      "detail": "Payee not in approved vendor master"
    },
    {
      "id": "P-04,P-05",
      "control": "Limit splitting",
      "detail": "Multiple payments just below officer limit"
    }
  ]
}
```

</details>

<details><summary>🔍 Internal Auditor (agent)</summary>

### Exception Evaluation

#### 1. Exception: P-02 - Maker-checker / Segregation of Duties
- **Control Violation**: Same user made and approved the payment.
- **Pattern**: This is a common control exception where the maker and checker roles are not segregated, which can lead to potential fraud or errors.
- **Possible Fraud Indicators**: 
  - **Conflict of Interest**: The same individual is responsible for both making and approving the payment, which can lead to self-approval or manipulation.
  - **Lack of Independent Review**: Without a separate reviewer, there is no independent check on the payment process.
- **Root Cause**: 
  - **Inadequate Segregation of Duties**: The organization may not have properly segregated the maker and checker roles.
  - **User Role Assignment**: The user "u12" may have been assigned both roles, possibly due to a lack of role-based access control or a staffing shortage.

#### 2. Exception: P-03 - Delegation of Authority
- **Control Violation**: Payment amount exceeds the manager's approval limit.
- **Pattern**: This exception indicates that the payment amount is above the manager's authority limit, which should have required higher-level approval.
- **Possible Fraud Indicators**: 
  - **Excessive Authority**: The manager may have abused their authority by approving a payment that should have required additional approval.
  - **Risk of Overpayment**: There is a risk that the payment could be excessive or unnecessary.
- **Root Cause**: 
  - **Inadequate Approval Limits**: The approval limits for the manager may be too high, allowing them to approve large payments without additional oversight.
  - **Lack of Control Over Large Payments**: There may be a lack of controls to ensure that large payments are properly reviewed and approved.

#### 3. Exception: P-04 - Vendor Master
- **Control Violation**: Payee not in approved vendor master.
- **Pattern**: This exception indicates that the vendor is not listed in the approved vendor master, which is a critical control to ensure that payments are made only to authorized vendors.
- **Possible Fraud Indicators**: 
  - **Unapproved Vendor**: The payment may be made to an unauthorized vendor, which could be a sign of fraud.
  - **Risk of Payment to Non-Existent Vendor**: There is a risk that the payment could be made to a non-existent or fraudulent vendor.
- **Root Cause**: 
  - **Inadequate Vendor Master Management**: The vendor master may not be properly maintained or updated, leading to unauthorized payments.
  - **Lack of Vendor Approval Process**: There may be a lack of a formal process to approve vendors, which could lead to unauthorized payments.

#### 4. Exception: P-05 - Vendor Master
- **Control Violation**: Payee not in approved vendor master.
- **Pattern**: This exception is similar to P-04, indicating that the vendor is not listed in the approved vendor master.
- **Possible Fraud Indicators**: 
  - **Unapproved Vendor**: The payment may be made to an unauthorized vendor, which could be a sign of fraud.
  - **Risk of Payment to Non-Existent Vendor**: There is a risk that the payment could be made to a non-existent or fraudulent vendor.
- **Root Cause**: 
  - **Inadequate Vendor Master Management**: The vendor master may not be properly maintained or updated, leading to unauthorized payments.
  - **Lack of Vendor Approval Process**: There may be a lack of a formal process to approve vendors, which could lead to unauthorized payments.

#### 5. Exception: P-04, P-05 - Limit Splitting
- **Control Violation**: Multiple payments just below officer limit.
- **Pattern**: These payments are just below the officer's approval limit, suggesting that the payments may have been split to avoid higher-level approval.
- **Possible Fraud Indicators**: 
  - **Avoiding Approval**: The payments may be split to avoid the need for higher-level approval, which could be a sign of fraud.
  - **Risk of Overpayment**: There is a risk that the payments could be excessive or unnecessary.
- **Root Cause**: 
  - **Inadequate Approval Limits**: The approval limits for the officer may be too high, allowing payments to be split to avoid higher-level approval.
  - **Lack of Control Over Large Payments**: There may be a lack of controls to ensure that large payments are properly reviewed and approved.

### Summary of Patterns and Root Causes
- **Segregation of Duties**: Inadequate segregation of maker and checker roles.
- **Approval Limits**: Inadequate approval limits for managers and officers.
- **Vendor Master Management**: Inadequate maintenance and approval of the vendor master.
- **Limit Splitting**: Inadequate controls over large payments, leading to potential avoidance of higher-level approval.

### Recommendations
1. **Segregation of Duties**: Ensure that maker and checker roles are properly segregated.
2. **Approval Limits**: Review and adjust approval limits to ensure they are appropriate and enforceable.
3. **Vendor Master Management**: Implement and maintain a robust vendor approval process.
4. **Limit Splitting**: Strengthen controls over large payments to prevent splitting and avoid higher-level approval.

These recommendations should help address the identified control weaknesses and reduce the risk of fraud and errors.

</details>

**🦙 Ollama:**

### Audit Findings

#### Finding 1: Maker-Checker / Segregation of Duties (P-02)
- **Condition**: Same user made and approved the payment.
- **Criteria**: Maker-checker / segregation of duties control is not properly enforced.
- **Cause**: Inadequate segregation of duties, possibly due to user role assignment or staffing shortages.
- **Effect**: Potential for self-approval or manipulation, lack of independent review.
- **Recommendation**: Ensure proper segregation of maker and checker roles. Review and adjust user roles to prevent conflicts of interest.
- **Rating**: High

#### Finding 2: Delegation of Authority (P-03)
- **Condition**: Payment amount exceeds the manager's approval limit.
- **Criteria**: Delegation of authority control is not properly enforced.
- **Cause**: Inadequate approval limits for managers, lack of control over large payments.
- **Effect**: Risk of overpayment and potential abuse of authority.
- **Recommendation**: Review and adjust approval limits for managers. Implement additional controls to ensure large payments are properly reviewed and approved.
- **Rating**: High

#### Finding 3: Vendor Master (P-04)
- **Condition**: Payee not in approved vendor master.
- **Criteria**: Vendor master control is not properly maintained.
- **Cause**: Inadequate vendor master management, lack of formal vendor approval process.
- **Effect**: Risk of unauthorized payments and potential fraud.
- **Recommendation**: Implement and maintain a robust vendor approval process. Regularly update and review the vendor master.
- **Rating**: High

#### Finding 4: Vendor Master (P-05)
- **Condition**: Payee not in approved vendor master.
- **Criteria**: Vendor master control is not properly maintained.
- **Cause**: Inadequate vendor master management, lack of formal vendor approval process.
- **Effect**: Risk of unauthorized payments and potential fraud.
- **Recommendation**: Implement and maintain a robust vendor approval process. Regularly update and review the vendor master.
- **Rating**: High

#### Finding 5: Limit Splitting (P-04, P-05)
- **Condition**: Multiple payments just below officer limit.
- **Criteria**: Control over large payments is inadequate.
- **Cause**: Inadequate approval limits for officers, lack of controls to prevent splitting payments.
- **Effect**: Risk of overpayment and potential avoidance of higher-level approval.
- **Recommendation**: Review and adjust approval limits for officers. Implement additional controls to ensure large payments are properly reviewed and approved.
- **Rating**: High

### Overall Control Environment Opinion
- **Opinion**: Needs Improvement

### Agreed Actions
1. **Segregation of Duties**: Ensure proper segregation of maker and checker roles. Review and adjust user roles to prevent conflicts of interest.
2. **Approval Limits**: Review and adjust approval limits for managers and officers. Implement additional controls to ensure large payments are properly reviewed and approved.
3. **Vendor Master Management**: Implement and maintain a robust vendor approval process. Regularly update and review the vendor master.
4. **Limit Splitting**: Review and adjust approval limits for officers. Implement additional controls to ensure large payments are properly reviewed and approved.

These actions should help address the identified control weaknesses and reduce the risk of fraud and errors.


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/49_internal_audit_assistant/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
