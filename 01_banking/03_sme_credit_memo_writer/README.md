# 03 · SME Credit Memo Writer

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏦 Credit & Lending

## 🏦 The business problem (new to banking? start here)

**In the business today:** Before lending to a small or mid-sized business, a relationship manager and credit analyst write a 'credit memo': who the business is, how it is performing, whether it can repay, and what protections the bank will take.

**Who does this work:** Corporate/SME relationship managers and credit analysts.

**Why it's hard:** Writing a memo takes days of spreadsheet work and drafting; analysts spend more time writing than analysing.

### Key terms
- **Credit memo**: The written paper a credit committee reads before approving a business loan: who the borrower is, the numbers, risks and recommendation.
- **DSCR (Debt Service Coverage Ratio)**: Cash profit (EBITDA) divided by loan repayments due. Below 1.0x the business cannot cover its debt from operations.
- **EBITDA / EBIT**: Earnings before interest, tax, depreciation and amortisation (EBITDA), or before interest and tax (EBIT): a measure of operating profit.
- **Leverage (debt-to-equity)**: How much a company relies on borrowing. Higher leverage means higher risk if earnings fall.
- **Covenant**: A promise in a loan agreement, e.g. 'keep debt below 3x EBITDA'. Breaking it lets the bank act early.
- **Collateral**: An asset the bank can take if the loan is not repaid, e.g. property or stock.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Turns SME financials into a bank-style credit memo (business profile, ratios, risks, mitigants).

### How it works
Ratios (DSCR, current ratio, leverage, margins) are computed in Python; a Financial Analyst agent analyses them and a Credit Writer agent drafts the memo.

```mermaid
flowchart LR
    IN["📄 SME financial statements"] --> PY["🐍 Python<br/>DSCR · current ratio · leverage · margins"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🧑‍💼 SME Financial Analyst"]
        A2["✍️ Credit Memo Writer"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Bank-style credit memo"]
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

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 40 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** Write the credit memo for GreenLeaf Foods: a 25M working capital line plus a 15M term loan for their new packaging unit.

<details><summary>🐍 Python · Computed ratios</summary>

```json
{
  "FY2024": {
    "ebitda_margin_pct": 12.0,
    "net_margin_pct": 4.7,
    "dscr": 2.27,
    "current_ratio": 1.5,
    "debt_to_equity": 1.1,
    "debt_to_ebitda": 2.54
  },
  "FY2025": {
    "ebitda_margin_pct": 11.5,
    "net_margin_pct": 4.6,
    "dscr": 2.19,
    "current_ratio": 1.39,
    "debt_to_equity": 1.03,
    "debt_to_ebitda": 2.51
  },
  "revenue_growth_pct": 17.1
}
```

</details>

<details><summary>🧑‍💼 SME Financial Analyst (agent)</summary>

### Analytical Notes

#### Profitability
- **Revenue Growth:** GreenLeaf Foods Pvt Ltd has shown a significant revenue growth of 17.1% from FY2024 to FY2025, indicating a strong market position and operational efficiency.
- **EBITDA Margin:** The EBITDA margin decreased slightly from 12.0% in FY2024 to 11.5% in FY2025. This suggests a marginal decline in operational efficiency or cost management.
- **Net Margin:** The net margin has remained relatively stable at 4.7% and 4.6% respectively, indicating consistent profitability despite the slight decrease in EBITDA margin.
- **Net Profit:** The net profit increased from 9,800 to 11,200, which is a positive trend, but the increase is relatively small compared to the revenue growth.

#### Liquidity
- **Current Ratio:** The current ratio decreased from 1.5 in FY2024 to 1.39 in FY2025, indicating a slight reduction in short-term liquidity. This could be a concern if the company faces unexpected short-term obligations.
- **Debt to Equity:** The debt to equity ratio improved from 1.1 in FY2024 to 1.03 in FY2025, suggesting better capital structure and reduced financial leverage.
- **Debt to EBITDA:** The debt to EBITDA ratio remained relatively stable at 2.54, indicating that the company can cover its debt obligations with its EBITDA.

#### Leverage
- **Debt to Equity:** As mentioned, the debt to equity ratio improved, which is a positive sign. However, a ratio of 1.03 still indicates that the company is moderately leveraged.
- **Debt to EBITDA:** The debt to EBITDA ratio is also stable, suggesting that the company can manage its debt obligations effectively.

#### Repayment Capacity
- **Debt Service Coverage Ratio (DSCR):** The DSCR decreased from 2.27 in FY2024 to 2.19 in FY2025. This indicates a slight reduction in the company's ability to cover its debt obligations with its EBITDA. However, a DSCR of 2.19 is still considered healthy, as it is above 2, which is generally the minimum threshold for lenders.
- **Principal Repaid:** The principal repayment increased from 6,000 to 7,000, which is a positive sign, indicating that the company is managing its debt effectively.

#### Red Flags
- **EBITDA Margin Decline:** The slight decrease in EBITDA margin could be a red flag, as it suggests potential operational or cost issues that need to be addressed.
- **Current Ratio Decrease:** The decrease in the current ratio is a concern, as it indicates a reduction in short-term liquidity. This could be a sign of potential cash flow issues or increased working capital needs.
- **Slight DSCR Decrease:** The slight decrease in DSCR is a minor red flag, but the company still has a healthy DSCR, which is reassuring.

### Conclusion
GreenLeaf Foods Pvt Ltd appears to be in a relatively strong financial position, with consistent profitability, improved capital structure, and the ability to manage its debt obligations. However, there are some areas of concern, particularly the slight decrease in EBITDA margin and current ratio. These issues should be monitored closely, and the company should focus on maintaining operational efficiency and managing working capital effectively.

</details>

**🦙 Ollama:**

**Credit Memo**

**1. Borrower Overview**
GreenLeaf Foods Pvt Ltd is a packaged food manufacturing company with 9 years of operational history. The company has requested a working capital line of 25,000,000 and a term loan of 15,000,000 for the establishment of a new packaging unit. The company's primary assets include factory land and building (valued at 60,000,000), stock, and receivables, which will be hypothecated as collateral.

**2. Facility Request**
The facility requested includes a working capital line of 25,000,000 and a term loan of 15,000,000 for the new packaging unit. The term loan will be used to finance the construction and initial operational costs of the new packaging unit, while the working capital line will support ongoing operational needs.

**3. Financial Analysis**
- **EBITDA Margin:** The EBITDA margin decreased from 12.0% in FY2024 to 11.5% in FY2025, indicating a marginal decline in operational efficiency or cost management.
- **Net Margin:** The net margin remained stable at 4.7% and 4.6% respectively, suggesting consistent profitability.
- **Net Profit:** The net profit increased from 9,800 to 11,200, indicating a positive trend.
- **Current Ratio:** The current ratio decreased from 1.5 in FY2024 to 1.39 in FY2025, indicating a slight reduction in short-term liquidity.
- **Debt to Equity:** The debt to equity ratio improved from 1.1 in FY2024 to 1.03 in FY2025, suggesting better capital structure and reduced financial leverage.
- **Debt to EBITDA:** The debt to EBITDA ratio remained stable at 2.54, indicating that the company can cover its debt obligations with its EBITDA.
- **DSCR:** The DSCR decreased from 2.27 in FY2024 to 2.19 in FY2025, indicating a slight reduction in the company's ability to cover its debt obligations with its EBITDA. However, a DSCR of 2.19 is still considered healthy.

**4. Key Risks & Mitigants**
- **EBITDA Margin Decline:** The slight decrease in EBITDA margin could be a red flag, indicating potential operational or cost issues. The company should focus on maintaining operational efficiency and cost management.
- **Current Ratio Decrease:** The decrease in the current ratio is a concern, indicating a reduction in short-term liquidity. The company should manage its working capital effectively to ensure sufficient liquidity.
- **Slight DSCR Decrease:** The slight decrease in DSCR is a minor red flag, but the company still has a healthy DSCR. The company should continue to monitor and manage its debt obligations.

**5. Covenants**
The borrower will be required to maintain the following covenants:
- **EBITDA Margin:** Maintain an EBITDA margin of at least 11.0%.
- **Current Ratio:** Maintain a current ratio of at least 1.4.
- **Debt to EBITDA:** Maintain a debt to EBITDA ratio of no more than 2.6.
- **DSCR:** Maintain a DSCR of at least 2.0.

**6. Recommendation**
Based on the financial analysis and the borrower's operational history, GreenLeaf Foods Pvt Ltd appears to be in a relatively strong financial position with consistent profitability and improved capital structure. However, there are some areas of concern, particularly the slight decrease in EBITDA margin and current ratio. These issues should be monitored closely, and the company should focus on maintaining operational efficiency and managing working capital effectively. We recommend approving the facility with the specified covenants to ensure the company's ability to manage its debt obligations and maintain financial stability.

**End of Credit Memo**


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/03_sme_credit_memo_writer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
