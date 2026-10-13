# 30 · Retirement Planning Assistant

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📈 Wealth & Investment Management

## 🏦 The business problem (new to banking? start here)

**In the business today:** Customers ask 'can I retire at 60?'. Advisers estimate the savings needed, project current savings forward and work out the gap.

**Who does this work:** Financial planners and digital advice tools.

**Why it's hard:** The maths (inflation, returns, years in retirement) is unfamiliar to most customers; clear what-ifs help them act.

### Key terms
- **Retirement corpus**: The total savings needed at retirement to fund living costs for the rest of one's life.
- **SIP**: Systematic Investment Plan: investing a fixed amount every month into a fund.
- **Asset allocation**: How a portfolio is split between asset classes (equity, bonds, gold, cash). The biggest driver of risk and return.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Projects a retirement corpus, gap and required monthly savings.

### How it works
Agent uses a `retirement_plan` tool (corpus needed, projection, gap, extra saving) and re-runs it for what-if questions.

```mermaid
flowchart LR
    QU["💬 Your question"] --> AG["🤖 LangChain agent<br/>decides which tool to call"]
    AG <-->|"🔧 calls & results"| T["🐍 Python tools<br/>retirement_plan()"]
    IN["📄 Customer's age, savings & goal"] --> T
    AG <-.->|"💬 reasoning"| LLM(["🦙 Ollama"])
    AG --> OUT["📝 Retirement plan + gap"]
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

## 💬 Sample response

Real output from `qwen2.5:7b-instruct` running locally on a laptop. LLM wording changes from run to run; the numbers from
Python stay the same.

<details>
<summary><b>Show the full output</b></summary>

````text
--- Question ---
I'm 40, have 150,000 saved, save 1,000 a month and spend 3,500 a month. Can I retire at 60?


--- Plan ---
To retire at age 60, you would need a total corpus of approximately $1,520,117. Based on your current savings and monthly contributions, you are projected to have a corpus of about $1,126,737 at retirement. This leaves a gap of $393,380.

To bridge this gap, you would need to save an additional $755 per month. Alternatively, you could consider the following practical levers:

1. **Retire Later**: If you were to retire at age 65 instead of 60, the required corpus would be lower, and you might be on track with your current savings. Let's check this:
   
   

Retiring at age 65 would require a total corpus of approximately $1,762,232. Based on your current savings and monthly contributions, you are projected to have a corpus of about $1,668,884 at retirement. This leaves a gap of $93,348.

To bridge this gap, you would need to save an additional $115 per month. Alternatively, you could consider the following practical levers:

1. **Retire Later**: Retiring at age 65 would reduce the required corpus and make it easier to achieve your retirement goals with your current savings and monthly contributions.
2. **Save More**: Increasing your monthly savings to $1,115 would help close the gap and ensure you meet your retirement needs.
3. **Adjust Allocation**: Optimizing your investment allocation to potentially achieve a higher return before retirement could also help reduce the required corpus and the gap.

These adjustments can help you better align your retirement savings with your goals.
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/30_retirement_planner/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
