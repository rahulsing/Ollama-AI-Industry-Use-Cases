# 06 · Early Warning Signals (EWS) Monitor

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Chain-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏦 Credit & Lending

## 🏦 The business problem (new to banking? start here)

**In the business today:** For business loans, banks watch for warning signs (overdraft breaches, bounced cheques, falling sales, rating downgrades) so they can act before the borrower defaults.

**Who does this work:** Credit monitoring teams and relationship managers.

**Why it's hard:** Signals are spread across many systems; spotting them early is what makes a recovery possible.

### Key terms
- **Early Warning Signals (EWS)**: Signs that a healthy borrower may get into trouble, spotted before they miss payments.
- **SMA / watch-list**: Special Mention Account / watch-list: loans showing stress that get closer monitoring.
- **Credit risk**: The risk that a borrower does not pay back what they owe. Managing it is the core skill of any lender.
- **Covenant**: A promise in a loan agreement, e.g. 'keep debt below 3x EBITDA'. Breaking it lets the bank act early.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Detects early signs of stress in a corporate loan book and drafts watch-list commentary.

### How it works
Python flags triggers (overdraft breaches, cheque returns, rating downgrades, late financials); an LLM chain writes a watch-list note per borrower.

```mermaid
flowchart LR
    IN["📄 Borrower account behaviour"] --> PY["🐍 Python<br/>Trigger rules: overdrafts, bounces, downgrades"]
    PY -->|"✅ decision & numbers"| CH["🔗 LangChain prompt<br/>explain, don't decide"]
    CH <-.->|"💬"| LLM(["🦙 Ollama"])
    CH --> OUT["📝 Watch-list note per borrower"]
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
--- EWS scan ---
[
  {
    "name": "Apex Textiles",
    "exposure": 45000000,
    "status": "RED",
    "triggers": [
      "Persistent overdraft limit breaches",
      "Repeated cheque returns",
      "External rating downgrade / negative outlook",
      "Delay in submitting financials",
      "Sharp fall in GST turnover",
      "High promoter share pledge"
    ]
  },
  {
    "name": "Nova Logistics",
    "exposure": 30000000,
    "status": "GREEN",
    "triggers": []
  },
  {
    "name": "Sunrise Builders",
    "exposure": 80000000,
    "status": "AMBER",
    "triggers": [
      "External rating downgrade / negative outlook",
      "Delay in submitting financials"
    ]
  }
]


--- Watch-list notes ---
### Watch-List Notes

#### RED Borrower: Apex Textiles
**Situation:**
Apex Textiles is currently in a RED status due to multiple critical issues, including persistent overdraft limit breaches, repeated cheque returns, an external rating downgrade, delay in submitting financials, a sharp fall in GST turnover, and a high promoter share pledge.

**Likely Cause:**
The company is likely facing operational and financial difficulties, possibly due to poor cash flow management, operational inefficiencies, or external market pressures.

**Recommended Actions:**
1. **Client Call:** Schedule a meeting with the management to discuss the current financial situation and understand the root causes of the issues.
2. **Stock Audit:** Conduct a stock audit to verify the company's inventory levels and ensure that the financial statements are accurate.
3. **Tighten Limits:** Review and potentially tighten the credit limits to mitigate risk.
4. **SMA Classification:** Consider reclassifying the borrower to a higher risk category in the Systematic Monitoring and Analysis (SMA) framework.

**Review Date:**
Review the situation in 30 days.

---

#### GREEN Borrower: Nova Logistics
**Situation:**
Nova Logistics remains in a GREEN status with no triggering issues.

**Recommended Actions:**
No action required.

**Review Date:**
No review required at this time.

---

#### AMBER Borrower: Sunrise Builders
**Situation:**
Sunrise Builders is in an AMBER status due to an external rating downgrade and a delay in submitting financials.

**Likely Cause:**
The company may be experiencing some financial strain or operational challenges that are reflected in the rating downgrade and delayed financial submissions.

**Recommended Actions:**
1. **Client Call:** Arrange a call with the management to discuss the reasons behind the rating downgrade and the delay in submitting financials.
2. **Review Financials:** Ensure that the financials are submitted promptly and thoroughly reviewed to understand the financial health of the company.

**Review Date:**
Review the situation in 30 days.

---
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/06_early_warning_signals/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
