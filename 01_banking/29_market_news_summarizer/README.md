# 29 · Market News Briefing for RMs

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📈 Wealth & Investment Management

## 🏦 The business problem (new to banking? start here)

**In the business today:** Every morning, relationship managers need to know what happened in markets and which of their clients are affected, so they can call them proactively.

**Who does this work:** Relationship managers, investment strategists.

**Why it's hard:** News volume is huge; linking it to each client's holdings by hand is impossible at scale.

### Key terms
- **Relationship Manager (RM)**: The banker who owns a client relationship and is their main point of contact.
- **Asset allocation**: How a portfolio is split between asset classes (equity, bonds, gold, cash). The biggest driver of risk and return.
- **Guidance**: Management's forecast of future results. Investors watch closely for upgrades, downgrades or softer wording.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Summarises market news and maps it to client holdings for relationship managers.

### How it works
Market Analyst agent summarises themes; RM Briefing agent links them to each client's portfolio with talking points.

```mermaid
flowchart LR
    IN["📄 Market news + client portfolios"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🧑‍💼 Market Analyst"]
        A2["🧠 RM Briefing Specialist"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    IN -->|"📋 case data"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 RM morning briefing"]
    OUT --> HU["🧑‍⚖️ Human review"]
    classDef data fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    classDef rules fill:#d1fae5,stroke:#059669,color:#064e3b
    classDef ai fill:#ede9fe,stroke:#7c3aed,color:#3b0764
    classDef llm fill:#1f2937,stroke:#111827,color:#ffffff
    classDef out fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef human fill:#f3f4f6,stroke:#6b7280,color:#111827
    class IN data
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
--- RM morning briefing ---
### Per-client Briefing

#### Mr. Kapoor (Retired, Conservative)

**Impact on Holdings:**
- **Interest Rate and Inflation Dynamics:** Neutral to Positive. Given Mr. Kapoor's conservative profile, his bond-heavy portfolio (40% Long-duration gilt fund, 30% Bank FDs) may face some pressure as bond yields could potentially rise. However, the overall impact is likely to be minimal due to his conservative stance.
- **Supply Disruptions and Energy Prices:** Negative. The potential increase in energy costs could impact his holdings in the Paint & chemicals stocks (15%) and possibly the large-cap fund, which may have exposure to these sectors.
- **Technology Sector Headwinds:** Negative. The negative impact on IT services stocks (45% of Ms. Rao's portfolio) could indirectly affect Mr. Kapoor's large-cap fund (20%) if it has significant exposure to IT services.
- **Government Incentives and Manufacturing:** Positive. The semiconductor theme fund (20%) and the Nifty index fund (40%) could benefit from government incentives, which could positively impact his overall portfolio.

**Talking Points:**
1. **Interest Rate and Inflation Dynamics:** "Given the central bank's signals of a potential rate cut, it's important to review your bond holdings to ensure they are well-positioned for any potential yield curve shifts. We can discuss strategies to balance your fixed-income portfolio."
2. **Supply Disruptions and Energy Prices:** "With the recent increase in crude oil prices, it's crucial to monitor your holdings in sectors like paint and chemicals. We can explore diversification strategies to mitigate potential risks."
3. **Government Incentives and Manufacturing:** "The government's incentives for semiconductor manufacturing could be a positive for your portfolio. We can discuss how to capitalize on these opportunities through your investments in the semiconductor theme fund."

**Proactive Call Warranted:** Yes. Given the potential risks and opportunities, a proactive call is warranted to review and adjust his portfolio.

---

#### Ms. Rao (Tech Founder, Aggressive)

**Impact on Holdings:**
- **Interest Rate and Inflation Dynamics:** Neutral to Positive. Ms. Rao's portfolio is heavily weighted in equities, particularly in IT services stocks (45%) and semiconductor theme fund (20%). The potential for equity markets to benefit from lower borrowing costs could be significant.
- **Supply Disruptions and Energy Prices:** Negative. The increase in energy costs could negatively impact her holdings in IT services stocks and semiconductor theme fund, which may have indirect exposure to energy costs.
- **Technology Sector Headwinds:** Negative. The negative outlook for IT services could directly impact her IT services stocks and indirectly affect her small-cap fund (25%).
- **Government Incentives and Manufacturing:** Positive. The capital subsidy for semiconductor manufacturing could be a significant positive for her semiconductor theme fund and the Nifty index fund (20%).

**Talking Points:**
1. **Interest Rate and Inflation Dynamics:** "Given the potential for lower interest rates, we can discuss strategies to leverage this environment for your equity-heavy portfolio. We can explore opportunities in sectors that are likely to benefit from lower borrowing costs."
2. **Supply Disruptions and Energy Prices:** "The increase in energy costs could pose risks to your portfolio. We can discuss hedging strategies or diversification options to mitigate these risks."
3. **Technology Sector Headwinds:** "The slowdown in technology spending could impact your IT services stocks and small-cap fund. We can explore alternative growth opportunities within the technology sector that may be less affected by this slowdown."

**Proactive Call Warranted:** Yes. Given the significant exposure to sectors that may be negatively impacted, a proactive call is warranted to review and adjust her portfolio.

---

#### Sharma Family Office (Balanced)

**Impact on Holdings:**
- **Interest Rate and Inflation Dynamics:** Neutral to Positive. The family office's balanced portfolio (15% Aviation stocks, 40% Nifty index fund, 30% Corporate bond fund, 15% Paint & chemicals stocks) is well-diversified. The potential for equity markets to benefit from lower borrowing costs could be positive, while bond yields could rise but are likely to be managed through the corporate bond fund.
- **Supply Disruptions and Energy Prices:** Negative. The increase in energy costs could negatively impact their holdings in paint and chemicals stocks (15%).
- **Technology Sector Headwinds:** Negative. The negative outlook for IT services could indirectly affect their Nifty index fund (40%) and corporate bond fund (30%).
- **Government Incentives and Manufacturing:** Positive. The capital subsidy for semiconductor manufacturing could be a positive for their Nifty index fund and corporate bond fund, which may have exposure to the semiconductor sector.

**Talking Points:**
1. **Interest Rate and Inflation Dynamics:** "Given the potential for lower interest rates, we can discuss strategies to leverage this environment for your balanced portfolio. We can explore opportunities in sectors that are likely to benefit from lower borrowing costs."
2. **Supply Disruptions and Energy Prices:** "The increase in energy costs could pose risks to your portfolio. We can discuss hedging strategies or diversification options to mitigate these risks."
3. **Government Incentives and Manufacturing:** "The government's incentives for semiconductor manufacturing could be a significant positive for your portfolio. We can discuss how to capitalize on these opportunities through your investments in the Nifty index fund and corporate bond fund."

**Proactive Call Warranted:** Yes. Given the potential risks and opportunities, a proactive call is warranted to review and adjust their portfolio.

---

### Summary

- **Proactive Calls Warranted:** Yes for all clients.
- **Key Talking Points:** Tailored to each client's portfolio and the current market themes.
- **Strategies:** Diversification, hedging, and leveraging market opportunities based on the current economic environment.
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/29_market_news_summarizer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
