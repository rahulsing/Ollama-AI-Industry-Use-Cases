# 48 · Earnings Call Analyzer

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏢 Enterprise Analytics & Audit

## 🏦 The business problem (new to banking? start here)

**In the business today:** After quarterly results, management hold an earnings call. Analysts and investors listen for changes in outlook and signs of trouble.

**Who does this work:** Equity research, investor relations and credit analysts.

**Why it's hard:** Calls are long and the important signals are often subtle changes in wording.

### Key terms
- **Guidance**: Management's forecast of future results. Investors watch closely for upgrades, downgrades or softer wording.
- **NIM (Net Interest Margin)**: A bank's interest income minus interest paid, as a % of assets. The core measure of lending profitability.
- **Delinquency / NPA / NPL**: A delinquent loan is behind on payments. After about 90 DPD it becomes a Non-Performing Asset / Loan.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Extracts guidance, sentiment and risks from an earnings call transcript.

### How it works
Transcript Analyst agent extracts key points; Sentiment Analyst agent rates management tone and risks.

```mermaid
flowchart LR
    IN["📄 Earnings call transcript"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🧑‍💼 Transcript Analyst"]
        A2["🧑‍💼 Sentiment & Risk Analyst"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    IN -->|"📋 case data"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Earnings call note"]
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

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** Summarise Meridian Bank's Q3 FY26 earnings call. How confident did management sound, and what are the risks?

**🦙 Ollama:**

### Investor Note: Tone Score, Top 3 Positives, Top 3 Risks, Watch-list, One-line Takeaway

**Tone Score:** -2

**Reasons for Tone Score:**
- The management seems cautious and realistic about the outlook, which is reflected in the lowered guidance for loan growth and credit costs.
- There is a slight negative tone due to the lowered loan growth guidance, which is a key driver for the bank's performance.

**Top 3 Positives:**
1. **Stable Net Interest Margin:** The guidance for the net interest margin to stabilise is a positive sign, indicating that the bank is managing its interest rate risk effectively.
2. **Maintained Credit Quality:** The gross NPA and provision coverage ratios are maintained, suggesting that the bank is managing credit risks well.
3. **Strong Deposit Growth:** The 9% growth in deposits, coupled with a LDR of 88%, indicates a healthy funding base, which is crucial for the bank's stability.

**Top 3 Risks:**
1. **Lowered Loan Growth Guidance:** The guidance for loan growth has been lowered, which could impact revenue growth and overall profitability.
2. **Credit Costs Increase:** The rise in credit costs to 68 bps from 52 bps is a concern, especially given the increase in unsecured personal loans and credit cards.
3. **Dependence on Retail Deposits:** The bank's reliance on granular retail deposits for funding could be risky if there is a sudden shift in customer behavior or if the bank needs to moderate loan growth.

**Watch-list:**
1. **Loan Growth:** Monitor the actual loan growth in Q4 FY26 to see if it meets the lower end of the guidance.
2. **Credit Costs:** Keep a close eye on credit costs to ensure they do not rise further, which could impact the provision coverage ratio.
3. **Deposits:** Watch for any changes in deposit growth and the LDR to ensure the bank maintains a healthy funding mix.

**One-line Takeaway:**
The bank's management is being realistic about the challenges ahead, with lowered loan growth and increased credit costs, but the strong deposit base and stable credit quality provide some reassurance.


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/48_earnings_call_analyzer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
