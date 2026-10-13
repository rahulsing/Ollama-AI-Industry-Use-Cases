# 02 · Policy Coverage Q&A (RAG)

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-RAG-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🛡️ Insurance · **Category:** 🙋 Policy & Customer Service

## 🛡️ The business problem (new to insurance? start here)

**In the business today:** Customers call the helpline asking 'am I covered for this?'. Staff check the policy wording and the customer's schedule, then explain the answer and the excess.

**Who does this work:** Contact centre and claims helpline teams.

**Why it's hard:** Policy wordings are long and full of exclusions and conditions. Answers depend on which add-ons the customer bought, and wrong answers lead to complaints.

### Key terms
- **Policy wording / schedule**: The wording is the full contract (what is and isn't covered); the schedule lists this customer's chosen covers and limits.
- **Exclusion**: Something the policy specifically does not cover, e.g. wear and tear.
- **Add-on cover**: Optional extra cover bought on top of the core policy, e.g. accidental damage.
- **Excess (deductible)**: The amount the customer pays towards each claim before the insurer pays the rest.

More terms: [Insurance Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Answers 'am I covered?' questions from the policy wording and the customer's schedule, with clause citations.

### How it works
Relevant clauses are retrieved (the schedule and excess are always included); the LLM fills a coverage checklist (matching section, conditions met) and checks each exclusion sentence; Python decides COVERED / NOT COVERED from the customer's schedule; the LLM explains the decision with citations.

```mermaid
flowchart LR
    QU["❓ Your question"] --> R["🔎 Retriever<br/>finds the most relevant passages"]
    IN["📚 Policy wording + schedule"] -->|"🧮 embeddings"| R
    R -->|"📎 top passages"| G["🔗 LangChain<br/>answer only from passages"]
    G <-.->|"💬"| LLM(["🦙 Ollama"])
    G -->|"📋 checklist"| PY["🐍 Python<br/>COVERED / NOT COVERED decision"]
    PY -->|"✍️ explained"| OUT["📝 Answer with clause citations"]
    OUT --> HU["🧑‍⚖️ Human review"]
    classDef data fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    classDef rules fill:#d1fae5,stroke:#059669,color:#064e3b
    classDef ai fill:#ede9fe,stroke:#7c3aed,color:#3b0764
    classDef llm fill:#1f2937,stroke:#111827,color:#ffffff
    classDef out fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef human fill:#f3f4f6,stroke:#6b7280,color:#111827
    class IN,QU data
    class PY rules
    class R,G ai
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
--- Q: My washing machine hose burst and flooded the kitchen. Am I covered? ---
**COVERED** (Section 1.1 Escape of water)

Yes, you are covered for the damage caused by the burst washing machine hose, as per Section 1.1 Escape of water. According to your policy, this type of incident falls under the coverage for escape of water. However, please note that the excess for escape of water claims is 500, so you will need to pay this amount out of pocket before the insurance covers the rest.


--- Q: I dropped my TV while moving it. Can I claim? ---
**NOT COVERED** (Section 1.4 Accidental damage)

I'm sorry, but your claim for dropping your TV is not covered under your policy. According to Section 1.4 Accidental damage, accidental damage to contents like your TV is only covered if Accidental Damage cover is included in your schedule, and it appears that this cover is not included for you. There is no excess to pay in this case since the claim is not covered.


--- Q: My named Trek bike was stolen outside a cafe; I had locked it to a railing. ---
**COVERED** (Section 2 Personal Possessions add-on)

Your Trek bicycle, valued at 1,450, was covered under the Personal Possessions add-on (Section 2) because it was stolen while left unattended but locked to a fixed object outside your home. According to the policy, this meets the condition for coverage. However, please note that you will need to pay the excess of 250 for this claim.


--- Q: A storm blew down my garden shed. ---
**NOT COVERED** (Section 1.2 Storm and flood)

I'm sorry, but the damage to your garden shed caused by the storm is not covered under your policy. According to Section 1.2 Storm and flood, we do not cover damage to gates, fences, hedges, or garden sheds caused by storm or flood. There is no excess to pay in this case as the claim is not covered.
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 03_insurance/02_policy_coverage_qa/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Insurance use cases](../README.md#-use-cases) · [All industries](../../README.md)
