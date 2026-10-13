# 31 · ESG Investment Screener

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📈 Wealth & Investment Management

## 🏦 The business problem (new to banking? start here)

**In the business today:** More clients want investments that match their values, such as no tobacco or weapons and low carbon. Advisers screen funds and explain the trade-offs.

**Who does this work:** Investment advisers and ESG / product teams.

**Why it's hard:** ESG data is messy and greenwashing is a regulatory risk.

### Key terms
- **ESG**: Environmental, Social and Governance factors used to screen investments for sustainability.
- **Asset allocation**: How a portfolio is split between asset classes (equity, bonds, gold, cash). The biggest driver of risk and return.
- **Suitability**: The rule that a recommended product must fit the client's risk profile, knowledge, goals and time horizon.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Screens a fund universe against ESG preferences and exclusions.

### How it works
Python applies exclusions and score thresholds; ESG Analyst and Advisor agents explain trade-offs and shortlist funds.

```mermaid
flowchart LR
    IN["📄 Funds + client ESG preferences"] --> PY["🐍 Python<br/>Exclusions · ESG score thresholds"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🧑‍💼 ESG Analyst"]
        A2["🤖 Investment Advisor"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 ESG fund shortlist"]
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
--- Screening ---
[
  {
    "fund": "Global Clean Energy Fund",
    "passes": true,
    "fail_reasons": []
  },
  {
    "fund": "World Index Tracker",
    "passes": false,
    "fail_reasons": [
      "ESG score 58 < 70",
      "carbon intensity 140",
      "weapons exposure 1%",
      "tobacco exposure 1%",
      "fossil fuel 6%"
    ]
  },
  {
    "fund": "ESG Leaders Equity",
    "passes": true,
    "fail_reasons": []
  },
  {
    "fund": "Emerging Markets Value",
    "passes": false,
    "fail_reasons": [
      "ESG score 41 < 70",
      "carbon intensity 310",
      "tobacco exposure 3%",
      "fossil fuel 14%"
    ]
  },
  {
    "fund": "Green Bond Fund",
    "passes": true,
    "fail_reasons": []
  },
  {
    "fund": "Aerospace & Defence Opportunities",
    "passes": false,
    "fail_reasons": [
      "ESG score 49 < 70",
      "carbon intensity 120",
      "weapons exposure 35%"
    ]
  }
]


--- Recommendation ---
### Shortlist and Allocation

Based on the screening results and the client's values, I recommend the following shortlist and allocation among the passing funds:

1. **Global Clean Energy Fund** - 30%
2. **ESG Leaders Equity** - 40%
3. **Green Bond Fund** - 30%

### Rationale and Trade-Offs

1. **Global Clean Energy Fund (30%)**
   - **ESG Score**: 82 (meets the minimum threshold of 70)
   - **Carbon Intensity**: 45
   - **Fossil Fuel Pct**: 0%
   - **Weapons Pct**: 0%
   - **Tobacco Pct**: 0%
   - ** TER Pct**: 0.85%
   - **5-Year Return**: 9.1%
   - **Explanation**: This fund meets all the criteria, including an ESG score of 82, which is above the minimum threshold. It also has a low carbon intensity and no exposure to weapons or tobacco, aligning well with the client's values. The TER of 0.85% is relatively high, which could be a trade-off for the strong ESG performance and low carbon footprint. However, the 30% allocation ensures that the client still benefits from the fund's strong ESG credentials.

2. **ESG Leaders Equity (40%)**
   - **ESG Score**: 76 (meets the minimum threshold of 70)
   - **Carbon Intensity**: 70
   - **Fossil Fuel Pct**: 1%
   - **Weapons Pct**: 0%
   - **Tobacco Pct**: 0%
   - ** TER Pct**: 0.3%
   - **5-Year Return**: 9.8%
   - **Explanation**: This fund meets the criteria with an ESG score of 76, which is above the minimum threshold. It has a moderate carbon intensity and no exposure to weapons or tobacco, aligning well with the client's values. The TER of 0.3% is relatively low, making it a balanced choice between ESG performance and cost. The 40% allocation ensures that the client benefits from the strong ESG performance and low TER, while still maintaining a significant portion of the portfolio.

3. **Green Bond Fund (30%)**
   - **ESG Score**: 79 (meets the minimum threshold of 70)
   - **Carbon Intensity**: 30
   - **Fossil Fuel Pct**: 0%
   - **Weapons Pct**: 0%
   - **Tobacco Pct**: 0%
   - ** TER Pct**: 0.25%
   - **5-Year Return**: 3.4%
   - **Explanation**: This fund meets the criteria with an ESG score of 79, which is above the minimum threshold. It has a very low carbon intensity and no exposure to weapons or tobacco, aligning well with the client's values. The TER of 0.25% is the lowest among the funds, making it a cost-effective choice. However, the lower return of 3.4% might be a trade-off for the strong ESG performance and low carbon footprint. The 30% allocation ensures that the client still benefits from the fund's strong ESG credentials and low TER.

### Trade-Offs to Discuss with the Client

- **Global Clean Energy Fund**: The client will benefit from a fund with a strong ESG score and low carbon intensity, but the TER of 0.85% is relatively high. This could be a trade-off for the strong ESG performance and low carbon footprint.
- **ESG Leaders Equity**: The client will benefit from a balanced approach with a high ESG score, low carbon intensity, and no exposure to weapons or tobacco. The TER of 0.3% is relatively low, making it a cost-effective choice. However, the 5-year return of 9.8% is slightly lower than the other funds.
- **Green Bond Fund**: The client will benefit from a cost-effective choice with the lowest TER and the highest ESG score. However, the 5-year return of 3.4% is the lowest among the funds, which could be a trade-off for the strong ESG performance and low carbon footprint.

By diversifying the portfolio across these three funds, the client can achieve a balance between ESG performance, cost, and expected return.
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/31_esg_investment_screener/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
