# 45 · FX Hedging Advisor

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 💱 Treasury, Payments & Operations

## 🏦 The business problem (new to banking? start here)

**In the business today:** Companies that buy or sell abroad face currency risk. Bank FX sales teams help them measure it and lock in rates with forwards or options.

**Who does this work:** FX sales / treasury advisers for corporate clients.

**Why it's hard:** Clients need clear explanations of risk in their own currency, and advice must be about protection, not speculation.

### Key terms
- **FX exposure / hedging**: Risk that currency moves change the home-currency value of foreign receipts or payments; hedging locks in a rate.
- **FX forward**: A contract to exchange currency at a fixed rate on a future date. Removes uncertainty for a known cash flow.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Measures a corporate's FX exposure and suggests a hedging approach.

### How it works
Agent uses `net_exposure` and `forward_rate` tools and compares forward vs. unhedged outcomes.

```mermaid
flowchart LR
    QU["💬 Your question"] --> AG["🤖 LangChain agent<br/>decides which tool to call"]
    AG <-->|"🔧 calls & results"| T["🐍 Python tools<br/>net_exposure()<br/>forward_rate()"]
    IN["📄 FX exposures + market rates"] --> T
    AG <-.->|"💬 reasoning"| LLM(["🦙 Ollama"])
    AG --> OUT["📝 Hedging advice"]
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
--- Advice ---
Based on the provided exposures and forward rates, here is the analysis and hedging recommendations:

### Net Exposure
- **USD 3m**: Long 1,200,000 USD
- **EUR 6m**: Short 1,200,000 EUR

### Forward Rates and Risk Analysis
- **USD 3m**:
  - Forward Rate: 84.67 INR/USD
  - 1-sigma Spot Range: 82.31 - 86.09 INR/USD
  - Risk: If the spot rate at maturity is at the 1-sigma level, the worst-case scenario would be a spot rate of 82.31 INR/USD. This would result in a loss of approximately 2.6% (1200000 * (84.67 - 82.31) / 84.67) on the exposure.

- **EUR 6m**:
  - Forward Rate: 93.31 INR/EUR
  - 1-sigma Spot Range: 87.29 - 95.71 INR/EUR
  - Risk: If the spot rate at maturity is at the 1-sigma level, the worst-case scenario would be a spot rate of 95.71 INR/EUR. This would result in a loss of approximately 2.6% (1200000 * (95.71 - 93.31) / 93.31) on the exposure.

### Hedging Recommendations
1. **USD 3m Exposure**:
   - **Hedge Ratio**: 100% (since the exposure is net long)
   - **Instrument**: Forward
   - **Reasoning**: A forward contract locks in the exchange rate at 84.67 INR/USD, providing certainty and eliminating the risk of adverse movements in the spot rate.

2. **EUR 6m Exposure**:
   - **Hedge Ratio**: 100% (since the exposure is net short)
   - **Instrument**: Forward
   - **Reasoning**: A forward contract locks in the exchange rate at 93.31 INR/EUR, providing certainty and eliminating the risk of adverse movements in the spot rate.

### Natural Hedges
- **USD 3m**: If the client has a natural exposure to USD, such as a receivable or a liability denominated in USD, this exposure can be naturally hedged against the USD 3m exposure.
- **EUR 6m**: If the client has a natural exposure to EUR, such as a receivable or a liability denominated in EUR, this exposure can be naturally hedged against the EUR 6m exposure.

By implementing these forward contracts, the client can manage the risk associated with the foreign currency exposures and ensure that the financial performance is not adversely affected by exchange rate fluctuations.
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/45_fx_hedging_advisor/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
