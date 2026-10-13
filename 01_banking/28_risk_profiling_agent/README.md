# 28 · Investor Risk Profiling Agent

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Chain-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📈 Wealth & Investment Management

## 🏦 The business problem (new to banking? start here)

**In the business today:** Before giving investment advice, banks must assess a client's risk profile, usually through a questionnaire, and explain the result to the client.

**Who does this work:** Advisers / RMs.

**Why it's hard:** Answers are often contradictory (e.g. wants high growth but cannot tolerate losses), and these need a conversation.

### Key terms
- **Risk profile**: How much investment risk a client is willing and able to take, usually from a questionnaire.
- **Suitability**: The rule that a recommended product must fit the client's risk profile, knowledge, goals and time horizon.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Scores a risk questionnaire and explains the resulting risk profile to the client.

### How it works
Questionnaire answers are scored in Python; the LLM writes a profile summary and flags inconsistencies.

```mermaid
flowchart LR
    IN["📄 Risk questionnaire answers"] --> PY["🐍 Python<br/>Risk score · profile band"]
    PY -->|"✅ decision & numbers"| CH["🔗 LangChain prompt<br/>explain, don't decide"]
    CH <-.->|"💬"| LLM(["🦙 Ollama"])
    CH --> OUT["📝 Risk profile + inconsistencies"]
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

## 💬 Sample conversation

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 4 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** Here are the client's risk questionnaire answers. What is their risk profile, and is anything inconsistent?

<details><summary>🐍 Python · Score</summary>

```json
{
  "points": {
    "Investment horizon": 5,
    "Reaction to a 20% portfolio fall": 1,
    "Primary objective": 5,
    "Investment experience": 2,
    "Share of savings being invested": 1,
    "Income stability": 5
  },
  "score_pct": 54,
  "profile": "Moderate",
  "inconsistencies": [
    "Wants maximum growth but would sell everything after a 20% fall",
    "Aggressive objective with limited investment experience"
  ]
}
```

</details>

**🦙 Ollama:**

Based on your responses, your risk profile is moderate. You have a long-term investment horizon and want maximum growth, which is great for potential long-term gains. However, your reaction to a 20% portfolio fall (selling everything) and your limited investment experience suggest a more cautious approach might be better for now.

Here are a few follow-up questions to help us better understand your situation:

1. How comfortable are you with the potential ups and downs of the market?
2. Are there any specific financial goals you're trying to achieve in the next few years?
3. How do you feel about balancing growth with some level of stability in your investments?


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/28_risk_profiling_agent/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
