# 21 · Regulatory Change Impact Analyzer

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📜 Regulatory & Risk Reporting

## 🏦 The business problem (new to banking? start here)

**In the business today:** Regulators publish new rules constantly. Compliance must work out what each new rule requires, which teams and systems are affected, and what must change by the deadline.

**Who does this work:** Compliance and regulatory change management teams.

**Why it's hard:** Legal text is dense, and missing one obligation can lead to enforcement action.

### Key terms
- **Regulatory circular**: A notice from a regulator introducing new rules that banks must implement by a deadline.
- **Regulatory reporting**: Regular returns banks must send to their regulator (capital, liquidity, large exposures...). Errors can mean fines.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Reads a new regulatory circular and maps obligations to impacted business units and controls.

### How it works
Regulatory Analyst agent extracts obligations; Compliance Impact agent maps them to the bank's process inventory and gaps.

```mermaid
flowchart LR
    IN["📄 New regulator circular + process list"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🧑‍💼 Regulatory Analyst"]
        A2["⚖️ Compliance Impact Assessor"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    IN -->|"📋 case data"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Impact assessment + gaps"]
    OUT --> HU["🧑‍⚖️ Human review"]
    classDef data fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    classDef rules fill:#d1fae5,stroke:#059669,color:#064e3b
    classDef ai fill:#ede9fe,stroke:#7c3aed,color:#3b0764
    classDef llm fill:#1f2937,stroke:#111827,color:#ffffff
    classDef out fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef human fill:#f3f4f6,stroke:#6b7280,color:#111827
    class IN data
    class A1,A2 ai
    class LLM llm
    class OUT out
    class HU human
```

<sub>🟦 data · 🟩 Python: maths & rules (auditable) · 🟪 AI: reasoning & writing · ⬛ local LLM · 🟨 result</sub>

## 💬 Sample conversation

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 24 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** A new circular on digital lending (2026/14) just came out. What does it mean for our processes?

<details><summary>🧑‍💼 Regulatory Analyst (agent)</summary>

1. ID: 2026/14-1
   Requirement: Regulated entities shall provide a Key Fact Statement (KFS) with the all-in annual percentage rate (APR) to every digital loan applicant before contract execution.
   Effective Date: 1 April 2027

2. ID: 2026/14-2
   Requirement: Loan disbursements and repayments shall flow only between the borrower's account and the lender's account; no pass-through via third-party lending service provider (LSP) accounts.
   Effective Date: 1 April 2027

3. ID: 2026/14-3
   Requirement: A cooling-off period of at least 3 days shall be given during which the borrower may exit by repaying principal and proportionate APR without penalty.
   Effective Date: 1 April 2027

4. ID: 2026/14-4
   Requirement: Each lender shall appoint a nodal grievance redressal officer for digital lending; complaints not resolved in 30 days may be escalated to the Ombudsman.
   Effective Date: 1 April 2027

5. ID: 2026/14-5
   Requirement: Lenders shall report all digital lending apps (DLAs) used, including those of LSPs, to the regulator quarterly.
   Effective Date: 1 April 2027

</details>

**🦙 Ollama:**

### Gap Table

| Obligation | Impacted Unit | Current State | Gap | Action | Owner | Priority (H/M/L) |
|------------|---------------|---------------|-----|--------|--------|------------------|
| 2026/14-1  | Loan Origination System | No APR shown, shows flat interest rate | Does not provide all-in APR | Update Loan Origination System to include all-in APR | IT & Product Teams | H |
| 2026/14-2  | Retail Lending, Compliance | EMI collected via QuickCred's escrow account | Disbursements and repayments flow through third-party accounts | Modify Retail Lending process to ensure direct flow between borrower and lender accounts | Retail Lending & Compliance Teams | H |
| 2026/14-3  | Product Team | No cooling-off feature | No cooling-off period available | Implement cooling-off feature in product design and update terms & conditions | Product Team | H |
| 2026/14-4  | Compliance | No nodal grievance redressal officer appointed | No designated officer for digital lending complaints | Appoint a nodal grievance redressal officer for digital lending | Compliance Team | H |
| 2026/14-5  | Compliance | No DLA register exists | No record of digital lending apps used | Establish and maintain a DLA register for all digital lending apps, including LSPs | Compliance Team | H |

### Executive Summary

1. **Obligation 2026/14-1**: The current Loan Origination System does not display the all-in APR, which is required by the new regulation. The IT and Product Teams must update the system to include this information to ensure compliance.
2. **Obligation 2026/14-2**: The current process allows EMIs to be collected via QuickCred's escrow account, which is not compliant with the new regulation. The Retail Lending and Compliance Teams need to modify the process to ensure that all disbursements and repayments flow directly between the borrower and the lender.
3. **Obligation 2026/14-3**: The Product Team currently does not have a cooling-off feature, which is required by the new regulation. The Product Team must implement this feature and update the terms and conditions to reflect the new requirement.
4. **Obligation 2026/14-4**: There is no designated nodal grievance redressal officer for digital lending, which is required by the new regulation. The Compliance Team must appoint such an officer to ensure that complaints are handled promptly.
5. **Obligation 2026/14-5**: The Compliance Team does not maintain a DLA register, which is required by the new regulation. The Compliance Team must establish and maintain a register for all digital lending apps, including those of LSPs, to ensure compliance.

All identified gaps are high priority and must be addressed by the respective teams to ensure the bank is fully compliant by the effective date of 1 April 2027.


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/21_regulatory_change_tracker/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
