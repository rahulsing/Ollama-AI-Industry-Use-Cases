# 10 · KYC Onboarding Verifier

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🕵️ Financial Crime & Compliance

## 🏦 The business problem (new to banking? start here)

**In the business today:** Before opening an account, the bank must verify identity and address documents and check they match the application.

**Who does this work:** KYC / onboarding operations teams.

**Why it's hard:** Checks are repetitive; small mismatches (spelling, expired IDs) are easy to miss and delay customers.

### Key terms
- **KYC (Know Your Customer)**: Verifying who a customer is (ID, address) and understanding what they do, before and during the relationship.
- **CDD / EDD**: Customer Due Diligence (standard checks) and Enhanced Due Diligence (deeper checks for high-risk customers, such as source of wealth).

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Checks customer onboarding data for completeness, document validity and consistency.

### How it works
Agent uses `check_document_expiry`, `validate_id_format` and `compare_fields` tools and returns a KYC checklist with pass/fail.

```mermaid
flowchart LR
    QU["💬 Your question"] --> AG["🤖 LangChain agent<br/>decides which tool to call"]
    AG <-->|"🔧 calls & results"| T["🐍 Python tools<br/>get_application()<br/>validate_id_format()<br/>check_document_expiry()<br/>address_proof_recency()"]
    IN["📄 Onboarding application + ID documents"] --> T
    AG <-.->|"💬 reasoning"| LLM(["🦙 Ollama"])
    AG --> OUT["📝 KYC checklist: pass / fail"]
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

## 💬 Sample conversation

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 8 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** Verify the current onboarding application.

<details><summary>🔧 Tool calls</summary>

```text
get_application() -> {"form": {"full_name": "Ananya R. Iyer", "dob": "1991-04-22", "address": "14 Lake View Rd, Bengaluru 560001", "pan": "AKPPI4521L", "occupation": "Architect", "source_of_funds": "Salary"}, "id_document": {"type": "Passport", "number": "Z4829175", "name": "ANANYA RAMESH IYER", "dob": "1991-04-22", "expiry": "2026-08-30"}, "address_proof": {"type": "Utility bill", "address": "14 Lakeview Road, Bangal
validate_id_format(id_type='Passport', number='Z4829175') -> Passport Z4829175: VALID format
check_document_expiry(expiry='2026-08-30') -> Expired 43 days ago
address_proof_recency(issue_date='2026-06-10', max_age_days=90) -> Issued 124 days ago - TOO OLD (limit 90)
```

</details>

**🦙 Ollama:**

Based on the provided information and the results from the tools, here is the checklist:

- **ID Format**: PASS
- **ID Expiry**: FAIL (Expired 43 days ago)
- **Name Match**: PASS (Allowing middle-name/initial differences)
- **DOB Match**: PASS
- **Address Match**: PASS (Allowing spelling and abbreviation variants like Bangalore/Bengaluru)
- **Address-Proof Recency**: REVIEW (Issued 124 days ago - TOO OLD (limit 90))

Given the issues with the ID expiry and the address proof recency, the final status is:

- **Final Status**: PENDING (list documents needed: Valid passport and recent address proof)

Please provide a valid passport and a recent address proof issued within the last 90 days.


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/10_kyc_onboarding_verifier/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
