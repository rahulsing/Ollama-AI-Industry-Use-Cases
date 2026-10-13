# 32 · Suitability & Mis-selling Checker

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Structured%20extraction-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📈 Wealth & Investment Management

## 🏦 The business problem (new to banking? start here)

**In the business today:** Before a product is sold, a check confirms it suits the client's risk profile, knowledge, time horizon and need for cash.

**Who does this work:** Sales supervisors and compliance / conduct teams.

**Why it's hard:** Mis-selling (especially to elderly or vulnerable customers) leads to compensation and fines.

### Key terms
- **Suitability**: The rule that a recommended product must fit the client's risk profile, knowledge, goals and time horizon.
- **Mis-selling**: Selling a product that is unsuitable or not properly explained. Leads to compensation and regulatory fines.
- **Vulnerable customer**: Someone more likely to suffer harm (e.g. due to age, illness, bereavement). Banks must take extra care with them.
- **Risk profile**: How much investment risk a client is willing and able to take, usually from a questionnaire.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Checks whether a recommended product is suitable for a client's profile before sale.

### How it works
Rules compare product risk vs. client risk, horizon and concentration; LLM returns a structured suitability verdict.

```mermaid
flowchart LR
    IN["📄 Client profile + product proposals"] --> PY["🐍 Python<br/>Risk, horizon & concentration rules"]
    PY -->|"✅ rule findings"| EX["🧾 LangChain structured output<br/>text → Pydantic schema"]
    EX -->|"validated verdict"| OUT["📝 Suitable / not suitable verdict"]
    EX <-.->|"💬"| LLM(["🦙 Ollama"])
    OUT --> HU["🧑‍⚖️ Human review"]
    classDef data fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    classDef rules fill:#d1fae5,stroke:#059669,color:#064e3b
    classDef ai fill:#ede9fe,stroke:#7c3aed,color:#3b0764
    classDef llm fill:#1f2937,stroke:#111827,color:#ffffff
    classDef out fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef human fill:#f3f4f6,stroke:#6b7280,color:#111827
    class IN data
    class PY rules
    class EX ai
    class LLM llm
    class OUT out
    class HU human
```

<sub>🟦 data · 🟩 Python: maths & rules (auditable) · 🟪 AI: reasoning & writing · ⬛ local LLM · 🟨 result</sub>

## 💬 Sample conversation

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 12 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** We plan to offer Mrs. Lata Desai (71, conservative) these three products. Are they suitable?

**🦙 Ollama:**

#### Structured note linked to small-cap index, capital at risk, 5-year lock-in
```
Rule findings: ['Product risk 5 > client risk 2', 'Lock-in 5y exceeds horizon 2y', 'Concentration >50% of liquid net worth', 'Complex product for inexperienced client']
{
  "verdict": "NOT_SUITABLE",
  "vulnerable_customer": true,
  "reasons": [
    "The product risk rating (5) is significantly higher than the client's risk profile (2/5).",
    "The lock-in period (5 years) exceeds the client's investment horizon (2 years).",
    "The investment amount (1.8 million) represents more than 60% of the client's liquid net worth (3 million), which is a high concentration risk.",
    "The structured note is a complex product, and the client has limited experience with financial instruments beyond fixed deposits."
  ],
  "required_actions": [
    "Recommend alternative products with lower risk and shorter lock-in periods.",
    "Advise on diversifying the investment portfolio to reduce concentration risk.",
    "Suggest simpler investment options that align with the client's experience and risk tolerance."
  ]
}
```

#### Senior citizen savings scheme (government-backed)
```
Rule findings: ['Lock-in 5y exceeds horizon 2y']
{
  "verdict": "NOT_SUITABLE",
  "vulnerable_customer": true,
  "reasons": [
    "The lock-in period of 5 years exceeds the client's investment horizon of 2 years, which could lock up funds that the client may need sooner.",
    "The client is conservative and has a fixed deposit-only experience, suggesting a preference for liquidity and lower risk."
  ],
  "required_actions": [
    "Recommend a product with a lock-in period that aligns with the client's horizon years (2 years).",
    "Consider a product that offers better liquidity or flexibility to meet the client's need for regular monthly income."
  ]
}
```

#### Short-duration high-quality debt fund
```
Rule findings: none
{
  "verdict": "SUITABLE",
  "vulnerable_customer": true,
  "reasons": [
    "Mrs. Lata Desai is a conservative investor with a risk profile of 2/5, which aligns well with the proposed short-duration high-quality debt fund with a risk rating of 2.",
    "The client's liquidity needs are met as the product has a lock-in period of 0 years, allowing for easy access to funds.",
    "Given her age (71) and experience (fixed deposits only), the proposed product is appropriate and aligns with her risk tolerance and investment history.",
    "The client's regular monthly income requirement can be met by this type of investment, providing a steady stream of income."
  ],
  "required_actions": []
}
```


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/32_suitability_checker/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
