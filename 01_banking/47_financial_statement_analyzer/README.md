# 47 · Financial Statement Analyzer

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🏢 Enterprise Analytics & Audit

## 🏦 The business problem (new to banking? start here)

**In the business today:** Before lending to or investing in a company, analysts study its financial statements to judge profitability, debt and cash generation.

**Who does this work:** Credit analysts and equity / credit research analysts.

**Why it's hard:** Headline growth can hide weak cash flow or rising debt; spotting this takes careful ratio analysis.

### Key terms
- **Financial statements**: Income statement (profit), balance sheet (what is owned and owed) and cash flow statement.
- **EBITDA / EBIT**: Earnings before interest, tax, depreciation and amortisation (EBITDA), or before interest and tax (EBIT): a measure of operating profit.
- **Margins**: Profit as a % of revenue (gross, operating, net). Falling margins signal pricing pressure or rising costs.
- **Leverage (debt-to-equity)**: How much a company relies on borrowing. Higher leverage means higher risk if earnings fall.
- **Liquidity ratios (current ratio)**: Current assets / current liabilities: can the company pay its bills due within a year?
- **Free cash flow**: Operating cash flow minus capital expenditure: the cash really available to repay debt or pay dividends.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Analyses a company's income statement and balance sheet and writes an equity-style summary.

### How it works
Ratios and YoY growth computed in Python; Financial Analyst and Report Writer agents interpret them.

```mermaid
flowchart LR
    IN["📄 Company financial statements"] --> PY["🐍 Python<br/>Ratios · YoY growth"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🧑‍💼 Financial Analyst"]
        A2["✍️ Research Report Writer"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Research report"]
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

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 39 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** Analyse Northwind Consumer Goods' last two years of financial statements and write a research report.

<details><summary>🐍 Python · Ratios</summary>

```json
{
  "2024": {
    "gross_margin_pct": 38.0,
    "ebit_margin_pct": 11.0,
    "net_margin_pct": 6.8,
    "roe_pct": 13.5,
    "interest_cover": 6.2,
    "current_ratio": 1.42,
    "debt_to_equity": 0.65,
    "dso_days": 52,
    "dio_days": 100,
    "free_cash_flow": 260,
    "operating_cash_flow_to_net_income_pct": 158
  },
  "2025": {
    "gross_margin_pct": 35.7,
    "ebit_margin_pct": 9.5,
    "net_margin_pct": 5.5,
    "roe_pct": 11.0,
    "interest_cover": 4.5,
    "current_ratio": 1.34,
    "debt_to_equity": 0.77,
    "dso_days": 61,
    "dio_days": 111,
    "free_cash_flow": 40,
    "operating_cash_flow_to_net_income_pct": 121
  },
  "yoy_growth_pct": {
    "revenue": 6.8,
    "net_income": -14.5,
    "total_debt": 23.8,
    "inventory": 23.2,
    "receivables": 24.6
  }
}
```

</details>

<details><summary>🧑‍💼 Financial Analyst (agent)</summary>

### Analytical Notes

#### Profitability
- **Revenue Growth**: Northwind Consumer Goods plc experienced a 6.8% increase in revenue from 2024 to 2025, which is a positive sign. However, the net income declined by 14.5%, indicating that the company's profitability has weakened.
- **Gross Margin**: The gross margin decreased from 38.0% in 2024 to 35.7% in 2025, suggesting that the cost of goods sold (COGS) has increased relative to revenue. This could be due to higher input costs or inefficiencies in production.
- **EBIT Margin**: The EBIT margin decreased from 11.0% to 9.5%, indicating a decline in operating efficiency.
- **Net Margin**: The net margin decreased from 6.8% to 5.5%, further confirming the decline in overall profitability.
- **Return on Equity (ROE)**: The ROE decreased from 13.5% to 11.0%, suggesting that the company's ability to generate returns on shareholders' equity has diminished.

#### Efficiency
- **Operating Efficiency**: The operating cash flow to net income ratio decreased from 158% in 2024 to 121% in 2025, indicating that the company is generating less cash from its operations relative to its net income. This could be due to higher working capital requirements or lower operating efficiency.
- **Receivables Turnover**: The days sales outstanding (DSO) increased from 52 days to 61 days, suggesting that the company is taking longer to collect receivables. This could indicate a potential issue with credit terms or customer payment behavior.
- **Inventory Turnover**: The days inventory outstanding (DIO) increased from 100 days to 111 days, indicating that the company is holding onto its inventory for a longer period. This could be due to overstocking or inefficiencies in inventory management.

#### Liquidity
- **Current Ratio**: The current ratio decreased from 1.42 to 1.34, indicating a slight decline in short-term liquidity. This is concerning as it suggests that the company may have difficulty meeting its short-term obligations.
- **Debt to Equity Ratio**: The debt to equity ratio increased from 0.65 to 0.77, indicating a higher reliance on debt financing. While this is not necessarily a concern, it is important to monitor as it could impact the company's financial flexibility and risk profile.

#### Leverage
- **Interest Coverage Ratio**: The interest coverage ratio decreased from 6.2 to 4.5, indicating that the company's ability to service its debt has weakened. This is a significant concern as it suggests that the company may struggle to meet its interest obligations in the future.

#### Cash Flow Quality
- **Free Cash Flow**: The free cash flow decreased from 260 to 40, indicating a decline in the company's ability to generate cash from its operations after accounting for capital expenditures. This is a concerning trend as it suggests that the company may be investing heavily in its operations or facing cash flow constraints.

### Concerns
1. **Declining Profitability**: The significant decline in net income and profitability ratios (gross margin, EBIT margin, net margin) is a major concern.
2. **Reduced Operating Efficiency**: The decrease in operating cash flow to net income ratio and the increase in DSO and DIO suggest that the company is facing challenges in managing its working capital.
3. **Liquidity Concerns**: The decrease in the current ratio and the increase in the debt to equity ratio indicate that the company may have liquidity issues.
4. **Debt Service Risk**: The decrease in the interest coverage ratio suggests that the company may struggle to meet its debt obligations, which could lead to financial distress.

In conclusion, Northwind Consumer Goods plc is facing significant challenges in maintaining its profitability and operational efficiency. These issues, coupled with liquidity and debt service concerns, warrant close monitoring and potential corrective actions to address the underlying issues.

</details>

**🦙 Ollama:**

### Summary
- **Revenue Growth**: Northwind Consumer Goods plc experienced a 6.8% increase in revenue from 2024 to 2025, but net income declined by 14.5%, indicating a weakening in overall profitability.
- **Profitability**: Gross margin and EBIT margin decreased, while net margin and ROE also declined, suggesting operational inefficiencies and cost pressures.
- **Cash Flow**: Free cash flow decreased significantly, and operating cash flow to net income ratio declined, indicating reduced cash generation from operations.

### Performance
- **Revenue Growth**: 6.8% increase from 2024 to 2025.
- **Gross Margin**: 38.0% in 2024 to 35.7% in 2025.
- **EBIT Margin**: 11.0% in 2024 to 9.5% in 2025.
- **Net Margin**: 6.8% in 2024 to 5.5% in 2025.
- **ROE**: 13.5% in 2024 to 11.0% in 2025.

### Balance Sheet & Liquidity
- **Current Ratio**: 1.42 in 2024 to 1.34 in 2025.
- **Debt to Equity**: 0.65 in 2024 to 0.77 in 2025.
- **DSO Days**: 52 in 2024 to 61 in 2025.
- **DIO Days**: 100 in 2024 to 111 in 2025.

### Cash Flow
- **Free Cash Flow**: 260 in 2024 to 40 in 2025.
- **Operating Cash Flow to Net Income**: 158% in 2024 to 121% in 2025.

### Key Risks / Red Flags
1. **Declining Profitability**: Gross margin, EBIT margin, and net margin all decreased, indicating operational inefficiencies.
2. **Reduced Operating Efficiency**: Operating cash flow to net income ratio declined, and DSO and DIO increased, suggesting challenges in managing working capital.
3. **Liquidity Concerns**: Current ratio decreased, and debt to equity ratio increased, indicating potential liquidity issues.
4. **Debt Service Risk**: Interest coverage ratio decreased, indicating reduced ability to service debt.

### Questions for Management
1. What steps are being taken to address the declining gross margin and EBIT margin?
2. How are the company's efforts to improve working capital management and reduce DSO and DIO?
3. What strategies are in place to enhance liquidity and reduce reliance on debt financing?
4. How is the company planning to improve its interest coverage ratio and ensure debt sustainability?

### Overall View
**Neutral**

Northwind Consumer Goods plc is facing significant challenges in maintaining profitability and operational efficiency. While the company has shown some revenue growth, the decline in profitability and cash flow metrics is concerning. The company needs to address these issues proactively to avoid further deterioration in financial health. Close monitoring and potential corrective actions are warranted to ensure the company can navigate these challenges successfully.


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/47_financial_statement_analyzer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
