# 23 · IFRS 9 ECL Calculator & Explainer

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📜 Regulatory & Risk Reporting

## 🏦 The business problem (new to banking? start here)

**In the business today:** Under IFRS 9, banks set aside provisions for loans they expect to go bad, based on each loan's stage and probability of default.

**Who does this work:** Credit risk / impairment team and Finance.

**Why it's hard:** Provisions directly hit profit; auditors challenge every staging decision and number.

### Key terms
- **IFRS 9**: The accounting standard that makes banks set aside provisions for expected (not just actual) loan losses.
- **ECL (Expected Credit Loss)**: The loss a bank expects on a loan: PD x LGD x EAD. Booked as a provision in the accounts.
- **PD / LGD / EAD**: Probability of Default, Loss Given Default (% lost if default happens) and Exposure at Default (amount owed).
- **IFRS 9 stages**: Stage 1 performing (12-month ECL), Stage 2 significant increase in credit risk (lifetime ECL), Stage 3 credit-impaired.
- **SICR**: Significant Increase in Credit Risk since the loan was made. Moves a loan from Stage 1 to Stage 2.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Stages loans (1/2/3) and calculates expected credit loss, then explains drivers.

### How it works
Agent calls `stage_loan` and `calculate_ecl` tools; explains SICR triggers and 12-month vs. lifetime ECL.

```mermaid
flowchart LR
    QU["💬 Your question"] --> AG["🤖 LangChain agent<br/>decides which tool to call"]
    AG <-->|"🔧 calls & results"| T["🐍 Python tools<br/>list_loans()<br/>stage_loan()<br/>calculate_ecl()<br/>portfolio_ecl()"]
    IN["📄 Loan book"] --> T
    AG <-.->|"💬 reasoning"| LLM(["🦙 Ollama"])
    AG --> OUT["📝 IFRS 9 stages + ECL"]
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

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 14 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** Calculate the ECL for the whole portfolio and explain it.

<details><summary>🔧 Tool calls</summary>

```text
portfolio_ecl() -> {"loans": [{"loan": "LN-1", "stage": 1, "pd_used": 0.01, "lgd": 0.35, "ead": 500000, "ecl": 1750, "coverage": "0.35%", "triggers": ["No SICR"]}, {"loan": "LN-2", "stage": 2, "pd_used": 0.18, "lgd": 0.4, "ead": 250000, "ecl": 18000, "coverage": "7.20%", "triggers": [">30 DPD backstop", "PD increased >=2.5x since origination (SICR)"]}, {"loan": "LN-3", "stage": 2, "pd_used": 0.12, "lgd": 0.45, "ead"
```

</details>

**🦙 Ollama:**

Here is the table summarizing the ECL for each loan in the portfolio, along with the total ECL and coverage percentage:

| Loan | Stage | Triggers | ECL (€) | Coverage % |
|------|-------|----------|--------|-----------|
| LN-1 | 1     | No SICR  | 1,750  | 0.35%     |
| LN-2 | 2     | >30 DPD backstop, PD increased >=2.5x since origination (SICR) | 18,000 | 7.20%     |
| LN-3 | 2     | PD increased >=2.5x since origination (SICR), On credit watchlist | 43,200 | 5.40%     |
| LN-4 | 3     | Credit-impaired: >90 DPD / default | 72,000 | 60.00%    |

**Total ECL for the portfolio: €134,950**

### Explanation of 12-Month vs Lifetime ECL

- **12-Month Expected Credit Loss (ECL):** This is the expected loss over the next 12 months. It is calculated using the 12-month Probability of Default (PD) for Stage 1 loans. For Stage 2 and Stage 3 loans, the lifetime PD is used, but the loss is only recognized over the next 12 months.
  
- **Lifetime Expected Credit Loss (ECL):** This is the total expected loss over the entire life of the loan. It is calculated using the lifetime PD for all stages. The lifetime ECL is a more conservative measure as it accounts for the full expected loss over the loan's entire term.

### Main Drivers of ECL

- **Probability of Default (PD):** The higher the PD, the higher the ECL. For example, LN-4 has a 100% PD, which significantly increases its ECL.
  
- **Loss Given Default (LGD):** This represents the percentage of the exposure at default that is expected to be lost. A higher LGD increases the ECL. For instance, LN-4 has a 60% LGD, contributing to its high ECL.
  
- **Exposure at Default (EAD):** This is the total amount of credit exposure. A higher EAD increases the ECL. LN-3 has the highest EAD, which contributes to its significant ECL despite a lower PD.

In summary, the total ECL of €134,950 is driven by the combination of high PD, LGD, and EAD for the loans in the portfolio, with LN-4 being the primary contributor due to its high PD and EAD.


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/23_ifrs9_ecl_calculator/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
