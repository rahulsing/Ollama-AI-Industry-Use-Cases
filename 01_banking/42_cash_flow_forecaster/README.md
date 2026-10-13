# 42 · Corporate Cash Flow Forecaster

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 💱 Treasury, Payments & Operations

## 🏦 The business problem (new to banking? start here)

**In the business today:** Corporate bankers help business clients forecast cash for the coming weeks to spot shortfalls and arrange funding in time.

**Who does this work:** Corporate relationship managers and transaction banking / treasury advisers.

**Why it's hard:** Running out of cash, even for a week, can sink a profitable business.

### Key terms
- **Cash flow forecasting**: Projecting future cash in and out (often 13 weeks) so a company can plan funding.
- **Working capital**: Money tied up in day-to-day operations (stock, receivables minus payables). Banks fund it with overdrafts and credit lines.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Forecasts a corporate client's 13-week cash position and highlights funding gaps.

### How it works
Agent uses `forecast_cash` and `funding_gap` tools on historical inflows/outflows.

```mermaid
flowchart LR
    QU["💬 Your question"] --> AG["🤖 LangChain agent<br/>decides which tool to call"]
    AG <-->|"🔧 calls & results"| T["🐍 Python tools<br/>forecast_cash()<br/>funding_gap()"]
    IN["📄 Inflows, outflows + known events"] --> T
    AG <-.->|"💬 reasoning"| LLM(["🦙 Ollama"])
    AG --> OUT["📝 13-week cash view + funding gap"]
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
--- Treasury view ---
Based on the 13-week cash forecast, here is a summary of the trends and funding needs:

### Inflows vs Outflows Trend
- **Weeks 1-5**: The company experiences consistent outflows of $130,000 per week, leading to a closing cash balance of $680,000 by the end of Week 5.
- **Week 6**: A significant outflow of $580,000 (likely due to payroll bonuses) causes the cash balance to turn negative at $-30,000.
- **Weeks 7-9**: The company continues to experience outflows, with the cash balance reaching a low of $-800,000 by Week 9 due to a large tax payment.
- **Week 10-11**: The cash balance remains negative, but a large customer receipt in Week 11 brings it back to $-760,000.
- **Weeks 12-13**: The company experiences consistent outflows, leading to a closing cash balance of $-1,020,000 by the end of Week 13.

### Week Cash Turns Negative
- The company's cash balance turns negative in **Week 6** with a closing balance of $-30,000.

### Funding Gap vs Overdraft
- The lowest projected cash point is in **Week 13** at $-1,020,000.
- The overdraft limit is $500,000, which is insufficient to cover the projected shortfall of $520,000.

### Recommendations
1. **Working Capital Line**: Given the significant funding gap, it would be prudent to increase the working capital line to at least $1,520,000 to cover the projected shortfall.
2. **Invoice Discounting**: Utilize invoice discounting to free up cash from receivables, potentially reducing the need for additional funding.
3. **Payables Timing**: Negotiate with suppliers to extend payment terms, thereby delaying cash outflows.
4. **Sweeping Surplus**: Implement a cash management strategy to sweep surplus funds from non-core accounts into the primary account to maintain liquidity.

These actions will help mitigate the risk of cash shortages and ensure the company can meet its financial obligations.
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/42_cash_flow_forecaster/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
