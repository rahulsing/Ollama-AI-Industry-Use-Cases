# 09 · AML Transaction Monitoring Agent

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🕵️ Financial Crime & Compliance

## 🏦 The business problem (new to banking? start here)

**In the business today:** Banks must monitor transactions for money laundering. Rules generate alerts (e.g. repeated cash deposits just under the reporting limit); investigators review each alert and decide whether to report it.

**Who does this work:** AML transaction monitoring analysts and the MLRO (Compliance / Financial Crime).

**Why it's hard:** Most alerts are false positives, yet missing a real case can bring huge fines. Investigation is slow and manual.

### Key terms
- **AML (Anti-Money Laundering)**: Laws and controls that stop criminals disguising illegal money as legitimate. Banks must monitor and report suspicious activity.
- **Money laundering stages**: Placement (getting cash into the system), layering (moving it to hide the trail), integration (using it as 'clean' money).
- **Structuring (smurfing)**: Splitting cash deposits into amounts just under a reporting threshold to avoid triggering a report. Itself an offence.
- **CTR (Currency Transaction Report)**: A report banks file for large cash transactions (e.g. 10,000 or more).
- **SAR / STR**: Suspicious Activity (or Transaction) Report: what a bank files with the financial intelligence unit when it suspects money laundering.
- **MLRO**: Money Laundering Reporting Officer: the senior person accountable for deciding whether to file SARs.
- **False positive**: An alert that turns out to be innocent, e.g. a name that looks like a sanctioned person but is someone else. Usually most alerts are false positives.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Detects structuring, rapid movement and high-risk-geography patterns and triages the alert.

### How it works
Python rules raise alerts; an AML Investigator agent reviews the evidence and a Compliance Officer agent decides close / escalate / file SAR.

```mermaid
flowchart LR
    IN["📄 Customer profile + transactions"] --> PY["🐍 Python<br/>AML rules: structuring, high-risk countries, CTR"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🕵️ AML Investigator"]
        A2["👔 MLRO / Compliance Officer"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Close / escalate / file SAR"]
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
--- Rule alerts ---
[
  {
    "rule": "STRUCTURING",
    "evidence": [
      [
        "2026-09-01",
        9500
      ],
      [
        "2026-09-02",
        9800
      ],
      [
        "2026-09-03",
        9700
      ]
    ]
  },
  {
    "rule": "RAPID_PASS_THROUGH",
    "evidence": [
      [
        "2026-09-15",
        48000,
        "Lindell Holdings Ltd"
      ],
      [
        "2026-09-16",
        47500,
        "Kestrel Imports"
      ]
    ]
  },
  {
    "rule": "HIGH_RISK_JURISDICTION",
    "evidence": [
      [
        "2026-09-15",
        48000,
        "VG"
      ]
    ]
  },
  {
    "rule": "PROFILE_DEVIATION",
    "evidence": "2026-09 turnover 154,930 vs expected 15,000"
  }
]


--- Alert triage ---
Decision: FILE_SAR

Risk Score: 8

Justification: The transactions involving multiple small cash deposits, rapid pass-through of large sums of money through high-risk jurisdictions, and significant profile deviation from the expected monthly turnover raise substantial red flags. These indicators are consistent with potential money laundering activities. Given the medium risk rating and the suspicious nature of the transactions, it is prudent to file a Suspicious Activity Report (SAR) to ensure regulatory compliance and to further investigate the legitimacy of the transactions.

Next Steps:
1. **RFI to Customer:** Request detailed information about the business dealings with Lindell Holdings Ltd and Kestrel Imports, including the nature of the transactions, the purpose of the wire transfers, and any relevant documentation.
2. **EDD:** Conduct an Enhanced Due Diligence (EDD) on Marco Rinaldi, including a deeper review of his business background, financial history, and any other relevant information to determine the legitimacy of the transactions.
3. **Account Restrictions:** Place temporary restrictions on the account to prevent further suspicious activities until the investigation is complete. This may include limiting cash deposits and requiring prior approval for large transactions.
4. **Follow-Up:** Monitor the account for any further suspicious activities and provide regular updates to the relevant authorities.
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/09_aml_transaction_monitoring/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
