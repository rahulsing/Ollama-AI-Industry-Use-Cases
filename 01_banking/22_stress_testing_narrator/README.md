# 22 · Stress Testing Scenario Narrator

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📜 Regulatory & Risk Reporting

## 🏦 The business problem (new to banking? start here)

**In the business today:** Banks simulate severe recessions to check they would still have enough capital, then explain the results to the board and regulator.

**Who does this work:** Stress testing / ICAAP teams (Risk), economists, the board risk committee.

**Why it's hard:** Results must be turned into a clear story of what breaks, why, and what management would do.

### Key terms
- **Stress testing**: Simulating a severe recession (GDP down, unemployment up) to check the bank would still have enough capital.
- **ICAAP**: Internal Capital Adequacy Assessment Process: the bank's own assessment of the capital it needs, reviewed by the regulator.
- **PD / LGD / EAD**: Probability of Default, Loss Given Default (% lost if default happens) and Exposure at Default (amount owed).
- **Capital ratio**: Capital / RWA. E.g. a CET1 ratio of 12% vs a 7% minimum means 5 percentage points of headroom.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Applies macro stress scenarios to a portfolio and writes the stress-test narrative for the board.

### How it works
Python shocks PD/LGD by scenario; an Economist agent describes scenarios and a Risk Reporter agent explains capital impact.

```mermaid
flowchart LR
    IN["📄 Loan portfolio + scenarios"] --> PY["🐍 Python<br/>PD / LGD shocks · losses · capital impact"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["📊 Chief Economist"]
        A2["👔 Stress Testing Lead"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Board stress-test summary"]
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
--- Stress results ---
{
  "Baseline": {
    "macro": {
      "gdp": 2.5,
      "unemployment": 4.5,
      "house_prices": 3
    },
    "losses_by_portfolio": {
      "Residential mortgages": 19,
      "Commercial real estate": 24,
      "SME loans": 81,
      "Large corporate": 67,
      "Credit cards": 90
    },
    "total_credit_loss": 281,
    "cet1_ratio_start": 9.75,
    "cet1_ratio_end": 10.67,
    "hurdle_pct": 7.0
  },
  "Adverse": {
    "macro": {
      "gdp": -1.5,
      "unemployment": 7.5,
      "house_prices": -12
    },
    "losses_by_portfolio": {
      "Residential mortgages": 48,
      "Commercial real estate": 54,
      "SME loans": 180,
      "Large corporate": 151,
      "Credit cards": 191
    },
    "total_credit_loss": 624,
    "cet1_ratio_start": 9.75,
    "cet1_ratio_end": 9.49,
    "hurdle_pct": 7.0
  },
  "Severely adverse": {
    "macro": {
      "gdp": -4.0,
      "unemployment": 10.0,
      "house_prices": -25
    },
    "losses_by_portfolio": {
      "Residential mortgages": 101,
      "Commercial real estate": 105,
      "SME loans": 346,
      "Large corporate": 294,
      "Credit cards": 354
    },
    "total_credit_loss": 1201,
    "cet1_ratio_start": 9.75,
    "cet1_ratio_end": 7.72,
    "hurdle_pct": 7.0
  }
}


--- Results table ---
| Scenario | Credit loss (m) | CET1 start | CET1 end | vs 7% hurdle |
|---|---|---|---|---|
| Baseline | 281 | 9.75% | 10.67% | PASS |
| Adverse | 624 | 9.75% | 9.49% | PASS |
| Severely adverse | 1,201 | 9.75% | 7.72% | PASS |


--- Board summary ---
### Board-Level Stress Testing Summary

#### Key Messages

The stress testing results for our bank under various economic scenarios indicate that our capital adequacy ratio (CET1) remains resilient, even under severe economic conditions. The bank has successfully passed the 7% CET1 capital adequacy hurdle in all scenarios, ensuring that we maintain a robust capital buffer to absorb potential losses.

#### Most Vulnerable Portfolios

The stress testing results highlight the most vulnerable portfolios under adverse and severely adverse economic conditions:

1. **Residential Mortgages:**
   - **Baseline Scenario:** Losses of 19 million.
   - **Adverse Scenario:** Losses of 48 million.
   - **Severely Adverse Scenario:** Losses of 101 million.

2. **Commercial Real Estate:**
   - **Baseline Scenario:** Losses of 24 million.
   - **Adverse Scenario:** Losses of 54 million.
   - **Severely Adverse Scenario:** Losses of 105 million.

3. **SME Loans:**
   - **Baseline Scenario:** Losses of 81 million.
   - **Adverse Scenario:** Losses of 180 million.
   - **Severely Adverse Scenario:** Losses of 346 million.

4. **Large Corporate:**
   - **Baseline Scenario:** Losses of 67 million.
   - **Adverse Scenario:** Losses of 151 million.
   - **Severely Adverse Scenario:** Losses of 294 million.

5. **Credit Cards:**
   - **Baseline Scenario:** Losses of 90 million.
   - **Adverse Scenario:** Losses of 191 million.
   - **Severely Adverse Scenario:** Losses of 354 million.

#### Management Actions

To address the identified vulnerabilities and ensure continued resilience, the following management actions are proposed:

1. **Capital Management:**
   - **Baseline and Adverse Scenarios:** Maintain current capital levels, as the CET1 ratio remains above the 7% hurdle.
   - **Severely Adverse Scenario:** Increase capital buffers by 100 million to ensure a minimum CET1 ratio of 8.72%, providing a buffer of 1% above the 7% hurdle.

2. **Risk Appetite:**
   - Review and adjust risk appetite limits for high-risk portfolios, particularly SME loans and credit cards, to ensure they are aligned with the bank's risk tolerance and capital constraints.

3. **Hedging Strategies:**
   - Implement hedging strategies to mitigate exposure to interest rate and credit risk, particularly in the severely adverse scenario where the CET1 ratio drops to 7.72%.

4. **Scenario Analysis and Stress Testing:**
   - Regularly update and refine stress testing scenarios to incorporate new economic indicators and market trends, ensuring that the bank remains prepared for a wide range of economic conditions.

By taking these actions, we can ensure that our bank remains resilient and well-positioned to withstand potential economic downturns, maintaining our commitment to financial stability and regulatory compliance.

Thank you for your attention.
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/22_stress_testing_narrator/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
