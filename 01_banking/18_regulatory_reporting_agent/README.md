# 18 · Regulatory Reporting Agent

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📜 Regulatory & Risk Reporting

## 🏦 The business problem (new to banking? start here)

**In the business today:** Each quarter, banks submit returns to the regulator on capital, liquidity and asset quality, with commentary explaining big movements.

**Who does this work:** Regulatory reporting team (Finance), signed off by the CFO.

**Why it's hard:** Data comes from many systems; errors or unexplained movements trigger regulator questions or fines.

### Key terms
- **Regulatory reporting**: Regular returns banks must send to their regulator (capital, liquidity, large exposures...). Errors can mean fines.
- **Capital (CET1, Tier 1, Tier 2)**: The bank's own money that absorbs losses. CET1 (mostly shareholders' equity) is the highest-quality layer.
- **RWA (Risk-Weighted Assets)**: Assets adjusted for risk: a government bond might count 0%, an unrated corporate loan 100%. Capital requirements are a % of RWA.
- **Capital ratio**: Capital / RWA. E.g. a CET1 ratio of 12% vs a 7% minimum means 5 percentage points of headroom.
- **LCR (Liquidity Coverage Ratio)**: High-quality liquid assets / expected net cash outflows over 30 days of stress. Must be at least 100%.
- **Delinquency / NPA / NPL**: A delinquent loan is behind on payments. After about 90 DPD it becomes a Non-Performing Asset / Loan.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Validates a regulatory return, explains period-on-period movements and drafts the submission commentary.

### How it works
Python runs validation and variance checks; a Data Quality agent reviews breaks and a Regulatory Reporting agent writes commentary.

```mermaid
flowchart LR
    IN["📄 Quarterly regulatory return"] --> PY["🐍 Python<br/>Validation rules · QoQ variance"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🧑‍💼 Regulatory Data Quality Analyst"]
        A2["👔 Regulatory Reporting Manager"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Submission commentary"]
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

## 💬 Sample conversation

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 46 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** Validate the Q3-2026 capital and liquidity return against Q2 and draft the submission commentary.

<details><summary>🐍 Python · Metrics</summary>

```json
{
  "Q2-2026": {
    "total_rwa": 37200,
    "cet1_ratio": 13.04,
    "tier1_ratio": 14.65,
    "total_capital_ratio": 17.07,
    "lcr": 140.0,
    "npl_ratio": 3.0
  },
  "Q3-2026": {
    "total_rwa": 41400,
    "cet1_ratio": 11.86,
    "tier1_ratio": 13.31,
    "total_capital_ratio": 15.43,
    "lcr": 119.7,
    "npl_ratio": 3.19
  }
}
```

</details>

<details><summary>🐍 Python · QoQ variance</summary>

```json
{
  "total_rwa": 4200,
  "cet1_ratio": -1.18,
  "tier1_ratio": -1.34,
  "total_capital_ratio": -1.64,
  "lcr": -20.3,
  "npl_ratio": 0.19
}
```

</details>

<details><summary>🐍 Python · Validation</summary>

All validation checks passed

</details>

<details><summary>🧑‍💼 Regulatory Data Quality Analyst (agent)</summary>

### List of Material Movements and Data-Quality Observations

#### Q2-2026 to Q3-2026 Movements:
1. **Total RWA:**
   - **Change:** 4200
   - **Percentage Change:** 11.29% (4200 / 37200 * 100)
   - **Explanation:** Increase in total RWA due to higher RWA_credit and RWA_market.

2. **CET1 Ratio:**
   - **Change:** -1.18%
   - **Percentage Change:** -1.18% (13.04 - 11.86)
   - **Explanation:** Decrease in CET1 ratio due to higher RWA_credit and RWA_market.

3. **Tier1 Ratio:**
   - **Change:** -1.34%
   - **Percentage Change:** -1.34% (14.65 - 13.31)
   - **Explanation:** Decrease in Tier1 ratio due to higher RWA_credit and RWA_market.

4. **Total Capital Ratio:**
   - **Change:** -1.64%
   - **Percentage Change:** -1.64% (17.07 - 15.43)
   - **Explanation:** Decrease in total capital ratio due to higher RWA_credit and RWA_market.

5. **Liquidity Coverage Ratio (LCR):**
   - **Change:** -20.3%
   - **Percentage Change:** -20.3% (140.0 - 119.7)
   - **Explanation:** Decrease in LCR due to higher net outflows and lower HQLA.

6. **NPL Ratio:**
   - **Change:** 0.19%
   - **Percentage Change:** 0.19% (3.0 - 3.19)
   - **Explanation:** Slight increase in NPL ratio due to higher NPL and total loans.

#### Data-Quality Observations:
1. **HQLA (High-Quality Liquid Assets):**
   - **Q2-2026:** 9800
   - **Q3-2026:** 9100
   - **Change:** -700
   - **Percentage Change:** -7.14% (700 / 9800 * 100)
   - **Explanation:** Significant decrease in HQLA, which could be due to the launch of a new FX trading desk or other business events.

2. **Net Outflows 30d:**
   - **Q2-2026:** 7000
   - **Q3-2026:** 7600
   - **Change:** 600
   - **Percentage Change:** 8.57% (600 / 7000 * 100)
   - **Explanation:** Increase in net outflows, which could be due to the launch of a new FX trading desk or other business events.

3. **Total Loans:**
   - **Q2-2026:** 52000
   - **Q3-2026:** 57300
   - **Change:** 5300
   - **Percentage Change:** 10.19% (5300 / 52000 * 100)
   - **Explanation:** Significant increase in total loans, which could be due to the large corporate loan growth in the construction sector.

4. **NPL (Non-Performing Loans):**
   - **Q2-2026:** 1560
   - **Q3-2026:** 1830
   - **Change:** 270
   - **Percentage Change:** 17.46% (270 / 1560 * 100)
   - **Explanation:** Increase in NPL, which could be due to the large corporate loan growth in the construction sector or other business events.

### Summary of Movements and Observations:
- **Total RWA, CET1 Ratio, Tier1 Ratio, Total Capital Ratio, and LCR** have significant changes that need explanation.
- **HQLA, Net Outflows 30d, Total Loans, and NPL** have notable decreases and increases that need further investigation, particularly in relation to the business events mentioned.

### Recommendations:
- **Review the business events** to understand the impact on the financial metrics.
- **Investigate the significant changes** in HQLA, Net Outflows 30d, Total Loans, and NPL to ensure they align with the business strategy and risk management policies.
- **Document the explanations** for the changes in RWA, CET1 Ratio, Tier1 Ratio, Total Capital Ratio, and LCR.

This detailed analysis will help in confirming the completeness, consistency, and adherence to regulatory thresholds.

</details>

**🦙 Ollama:**

### Commentary

#### 1. Executive Summary
The submission for the third quarter of 2026 (Q3-2026) regulatory reporting includes detailed metrics for capital adequacy, liquidity, asset quality, and data quality. The key ratios and metrics have shown significant changes compared to the previous quarter (Q2-2026). This commentary provides an in-depth analysis of these changes and highlights areas for further investigation and documentation.

#### 2. Capital Adequacy (Ratios vs Minimums & Drivers)
- **CET1 Ratio:** The CET1 ratio decreased to 11.86% from 13.04% in Q2-2026, falling short of the minimum requirement of 7.0%. The primary driver for this decrease was the increase in Risk-Weighted Assets (RWA) due to higher RWA_credit and RWA_market.
- **Tier1 Ratio:** The Tier1 ratio decreased to 13.31% from 14.65%, also below the minimum requirement of 8.5%. This decrease is attributed to the same factors as the CET1 ratio.
- **Total Capital Ratio:** The total capital ratio decreased to 15.43% from 17.07%, failing to meet the minimum requirement of 10.5%. The reduction in this ratio is primarily due to the increase in RWA_credit and RWA_market.

#### 3. Liquidity (LCR)
- **Liquidity Coverage Ratio (LCR):** The LCR decreased to 119.7% from 140.0%, falling short of the minimum requirement of 100%. The primary driver for this decrease was an increase in net outflows and a reduction in High-Quality Liquid Assets (HQLA).

#### 4. Asset Quality
- **NPL Ratio:** The NPL ratio increased to 3.19% from 3.0% in Q2-2026, which is within the acceptable range. The slight increase is due to higher NPL and total loans, particularly in the construction sector.

#### 5. Data Quality Statement
- **HQLA:** There was a significant decrease in HQLA from 9800 in Q2-2026 to 9100 in Q3-2026, representing a 7.14% decrease. This could be attributed to the launch of a new FX trading desk or other business events.
- **Net Outflows 30d:** Net outflows increased from 7000 in Q2-2026 to 7600 in Q3-2026, a 8.57% increase. This could also be due to the launch of a new FX trading desk or other business events.
- **Total Loans:** Total loans increased from 52000 in Q2-2026 to 57300 in Q3-2026, a 10.19% increase. This significant growth is primarily due to large corporate loan growth in the construction sector.
- **NPL (Non-Performing Loans):** NPL increased from 1560 in Q2-2026 to 1830 in Q3-2026, a 17.46% increase. This increase is also linked to the large corporate loan growth in the construction sector.

#### 6. Items for CFO Attention
- **Review the business events:** Conduct a thorough review of the business events that led to the significant changes in RWA, CET1 Ratio, Tier1 Ratio, Total Capital Ratio, and LCR to ensure they align with the strategic objectives and risk management policies.
- **Investigate the significant changes:** Further investigate the decreases in HQLA, increases in net outflows, and the significant increase in total loans and NPL to ensure they are consistent with the business strategy and risk management policies.
- **Document the explanations:** Provide detailed explanations for the changes in RWA, CET1 Ratio, Tier1 Ratio, Total Capital Ratio, and LCR to support the submission and ensure compliance with regulatory requirements.

This detailed analysis will help in confirming the completeness, consistency, and adherence to regulatory thresholds.


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/18_regulatory_reporting_agent/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
