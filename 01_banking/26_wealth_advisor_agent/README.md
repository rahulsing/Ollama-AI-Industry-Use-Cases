# 26 · AI Wealth Advisor

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📈 Wealth & Investment Management

## 🏦 The business problem (new to banking? start here)

**In the business today:** Wealth advisers understand a client's goals (education, retirement, a home), assess their risk tolerance, recommend a portfolio and document why it is suitable.

**Who does this work:** Financial advisers / relationship managers, checked by compliance.

**Why it's hard:** Good advice is personal and time-consuming, so it is usually only available to wealthier clients.

### Key terms
- **Wealth management**: Advice and investment services for individuals, from mass affluent to private banking clients.
- **Asset allocation**: How a portfolio is split between asset classes (equity, bonds, gold, cash). The biggest driver of risk and return.
- **Risk profile**: How much investment risk a client is willing and able to take, usually from a questionnaire.
- **Suitability**: The rule that a recommended product must fit the client's risk profile, knowledge, goals and time horizon.
- **SIP**: Systematic Investment Plan: investing a fixed amount every month into a fund.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Builds a goals-based investment plan for a client with suitability checks.

### How it works
Client Profiler, Portfolio Strategist and Compliance Reviewer agents collaborate to produce a personalised plan.

```mermaid
flowchart LR
    IN["📄 Client goals + model portfolios"] --> PY["🐍 Python<br/>Future value · required monthly SIP"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🧑‍💼 Client Profiler"]
        A2["♟️ Portfolio Strategist"]
        A3["🔍 Compliance Reviewer"]
        A1 -->|"hands over"| A2
        A2 -->|"hands over"| A3
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A3 --> OUT["📝 Personalised investment plan"]
    OUT --> HU["🧑‍⚖️ Human review"]
    classDef data fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    classDef rules fill:#d1fae5,stroke:#059669,color:#064e3b
    classDef ai fill:#ede9fe,stroke:#7c3aed,color:#3b0764
    classDef llm fill:#1f2937,stroke:#111827,color:#ffffff
    classDef out fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef human fill:#f3f4f6,stroke:#6b7280,color:#111827
    class IN data
    class PY rules
    class A1,A2,A3 ai
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
--- Computed facts ---
{
  "goals": [
    {
      "goal": "Children's higher education",
      "years": 10,
      "today_cost": 4000000,
      "inflated_cost": 7163391,
      "assumed_return_pct": 10.0,
      "required_monthly_sip": 34970
    },
    {
      "goal": "Retirement corpus",
      "years": 22,
      "today_cost": 30000000,
      "inflated_cost": 108106122,
      "assumed_return_pct": 10.0,
      "required_monthly_sip": 113417
    },
    {
      "goal": "Family vacation home",
      "years": 10,
      "today_cost": 5000000,
      "inflated_cost": 8954238,
      "assumed_return_pct": 10.0,
      "required_monthly_sip": 43712
    }
  ],
  "net_worth": 1500000,
  "est_monthly_investable_surplus_post_tax": 148000,
  "total_required_monthly_sip": 192099,
  "monthly_shortfall": 44099,
  "existing_investable_assets": 5400000,
  "emergency_fund_months": 6.0
}


--- Advice ---
### Client-Ready Advice Letter

#### Summary

Dear [Client's Name],

Thank you for entrusting us with your financial planning. Based on our analysis, we have developed a comprehensive plan to help you achieve your financial goals. Here is a detailed summary of the plan and the actions required to ensure your financial security.

---

#### 1. **Emergency Fund**
- **Current Allocation:** The Nairs have an emergency fund that can cover 6 months of expenses, which is a good start.
- **Action:** Increase the emergency fund to cover 3-6 months of living expenses. This will provide a more robust financial cushion.
- **Required Amount:** 3-6 months of living expenses (150,000 INR/month) = 450,000 - 900,000 INR.
- **Action:** Use part of the existing investable assets (5,400,000 INR) to build the emergency fund. For example, allocate 600,000 INR to the emergency fund, leaving 4,800,000 INR for other goals.

---

#### 2. **Children's Higher Education**
- **Required Monthly SIP:** 34,970 INR.
- **Action:** Allocate a portion of the monthly surplus to this goal. Given the shortfall, we will prioritize this goal.
- **Monthly Allocation:** 34,970 INR.

---

#### 3. **Retirement Corpus**
- **Required Monthly SIP:** 113,417 INR.
- **Action:** Allocate a significant portion of the remaining surplus to this goal, as it is a long-term goal.
- **Monthly Allocation:** 113,417 INR.

---

#### 4. **Family Vacation Home**
- **Required Monthly SIP:** 43,712 INR.
- **Action:** Allocate a portion of the remaining surplus to this goal.
- **Monthly Allocation:** 43,712 INR.

---

#### 5. **Rebalance Investment Portfolio**
- **Current Allocation:** The Nairs have a moderate to conservative allocation with a significant portion in fixed deposits and equity stocks.
- **Action:** Rebalance the portfolio to better align with their moderate risk tolerance and goals.
- **Recommended Allocation:**
  - **Conservative (score <40):** 25% equity, 60% debt, 10% gold, 5% cash.
  - **Moderate (40-65):** 50% equity, 35% debt, 10% gold, 5% cash.
  - **Growth (65-80):** 70% equity, 20% debt, 5% gold, 5% cash.
  - **Aggressive (>80):** 85% equity, 10% debt, 5% gold, 0% cash.

Given their moderate risk tolerance, we will use the **Moderate (40-65)** allocation for the majority of their investments.

---

#### 6. **Immediate Actions**
- **Insurance Review:** Ensure that their term life and health insurance coverage is adequate and up-to-date. Consider reviewing the coverage limits and adding any necessary riders or additional policies.
- **Debt Management:** If they have any outstanding debts, prioritize paying them off to reduce financial stress and improve their overall financial health.

---

### Summary of Allocations

1. **Children's Higher Education:** 34,970 INR
2. **Retirement Corpus:** 113,417 INR
3. **Family Vacation Home:** 43,712 INR
4. **Equity:** 2,400,000 INR
5. **Debt:** 1,680,000 INR
6. **Gold:** 480,000 INR
7. **Cash:** 240,000 INR
8. **Emergency Fund:** 600,000 INR

By following this plan, the Nairs can better align their financial strategy with their goals and ensure a more secure financial future.

---

### Risk Disclosures and Disclaimers

1. **Risk of Market Fluctuations:** The value of investments can fluctuate, and there is no guarantee that the investments will achieve their intended goals. Past performance is not a reliable indicator of future performance.
2. **No Guaranteed Returns:** The returns on investments are not guaranteed and can be affected by various factors, including market conditions, economic factors, and other risks.
3. **Emergency Fund:** While the emergency fund is designed to provide financial security, it is not a substitute for insurance or other financial protection measures.
4. **Rebalancing:** Rebalancing the portfolio may result in tax implications and transaction costs. It is important to consider these factors before making any changes.
5. **Insurance Coverage:** The adequacy of insurance coverage is subject to review and may need to be adjusted based on changes in family needs and other factors.

We recommend that you review this plan with your financial advisor and make any necessary adjustments. Regular reviews and rebalancing will help ensure that your financial strategy remains aligned with your goals.

Thank you for your trust and cooperation.

Best regards,

[Your Name]  
[Your Title]  
[Your Contact Information]  
[Date]

---

This advice letter is designed to be client-ready and includes all necessary disclosures and risk statements to ensure that the client is fully informed about the potential risks and uncertainties associated with the proposed financial plan.
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/26_wealth_advisor_agent/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
