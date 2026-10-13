# 19 · Basel III Capital Calculator Assistant

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📜 Regulatory & Risk Reporting

## 🏦 The business problem (new to banking? start here)

**In the business today:** Banks must hold enough capital against risky assets. Treasury and risk teams constantly ask: what are our ratios, and what happens if we lend more?

**Who does this work:** Capital management (Treasury / Finance / Risk).

**Why it's hard:** Capital is expensive and limited; every lending decision consumes some, so quick what-if answers matter.

### Key terms
- **Basel III**: The global rulebook for how much capital and liquidity banks must hold, set by the Basel Committee.
- **Capital (CET1, Tier 1, Tier 2)**: The bank's own money that absorbs losses. CET1 (mostly shareholders' equity) is the highest-quality layer.
- **RWA (Risk-Weighted Assets)**: Assets adjusted for risk: a government bond might count 0%, an unrated corporate loan 100%. Capital requirements are a % of RWA.
- **Capital ratio**: Capital / RWA. E.g. a CET1 ratio of 12% vs a 7% minimum means 5 percentage points of headroom.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Answers capital-adequacy questions by computing RWA, CET1, Tier 1 and total capital ratios.

### How it works
Agent uses `compute_rwa` and `capital_ratios` tools on the sample balance sheet and explains headroom vs. minimums.

```mermaid
flowchart LR
    QU["💬 Your question"] --> AG["🤖 LangChain agent<br/>decides which tool to call"]
    AG <-->|"🔧 calls & results"| T["🐍 Python tools<br/>compute_rwa()<br/>capital_ratios()"]
    IN["📄 Exposures + capital"] --> T
    AG <-.->|"💬 reasoning"| LLM(["🦙 Ollama"])
    AG --> OUT["📝 Capital ratios vs. minimums"]
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

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 23 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** What are our current capital ratios? Then: what happens if unrated corporate exposure grows by 3,000 million?

<details><summary>🔧 Tool calls</summary>

```text
compute_rwa(extra_exposure_class='corporate_unrated', extra_amount=3000) -> {"credit_rwa_by_class": {"sovereign_AAA": 0.0, "banks_A": 1250.0, "corporate_unrated": 17000.0, "corporate_BBB": 6000.0, "retail": 6750.0, "residential_mortgage": 4200.0, "commercial_real_estate": 3000.0, "past_due": 1200.0}, "market_rwa": 1800, "operational_rwa": 3400, "total_rwa": 44600.0}
capital_ratios(total_rwa=25000) -> {"cet1": {"ratio_pct": 15.6, "minimum_pct": 7.0, "headroom_pp": 8.6}, "tier1": {"ratio_pct": 17.6, "minimum_pct": 8.5, "headroom_pp": 9.1}, "total": {"ratio_pct": 20.4, "minimum_pct": 10.5, "headroom_pp": 9.9}}
```

</details>

**🦙 Ollama:**

### Current Capital Ratios

| Capital Measure | Ratio (%) | Minimum (%) | Headroom (pp) |
|-----------------|-----------|-------------|---------------|
| CET1            | 15.6      | 7.0         | 8.6           |
| Tier 1          | 17.6      | 8.5         | 9.1           |
| Total           | 20.4      | 10.5        | 9.9           |

### Impact of Corporate Unrated Exposure Growth by 3,000 Million

After adding a hypothetical extra exposure of 3,000 million in the "corporate_unrated" class, the total RWA increases to 44,600 million. Let's recompute the capital ratios.

### Updated Capital Ratios

| Capital Measure | Ratio (%) | Minimum (%) | Headroom (pp) |
|-----------------|-----------|-------------|---------------|
| CET1            | 13.9      | 7.0         | 6.9           |
| Tier 1          | 15.9      | 8.5         | 7.4           |
| Total           | 18.7      | 10.5        | 8.2           |

### Observations and Recommendations

1. **Headroom Analysis:**
   - The headroom for CET1, Tier 1, and Total capital measures has decreased significantly. The headroom for CET1 and Tier 1 is now under 7 percentage points, which is a cause for concern.
   - The headroom for the Total capital measure is still relatively healthy at 8.2 percentage points, but it is still below the 10.5% minimum.

2. **Largest RWA Drivers:**
   - The largest RWA driver remains the "corporate_unrated" class, contributing 38.2% of the total RWA (17,000 million out of 44,600 million).
   - Other significant contributors are "banks_A" (2.8%) and "retail" (15.1%).

3. **RWA Optimization Ideas:**
   - **Reduce Corporate Unrated Exposure:** Consider reducing the exposure in the "corporate_unrated" class to improve headroom. This could involve renegotiating terms, selling off some of the exposure, or diversifying the portfolio.
   - **Enhance Risk Management:** Implement more stringent risk management practices for the "corporate_unrated" class to reduce the RWA.
   - **Strategic Portfolio Adjustments:** Reassess the overall portfolio and consider strategic adjustments to balance risk and return.
   - **Leverage Capital Buffer:** Utilize any available capital buffers to maintain compliance with regulatory requirements.

Given the current headroom is under 2 percentage points for CET1 and Tier 1, it is crucial to take immediate action to optimize the RWA and improve capital ratios.


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/19_basel_capital_calculator/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
