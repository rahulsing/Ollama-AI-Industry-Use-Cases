# 27 · Portfolio Rebalancing Agent

![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) ![Pattern](https://img.shields.io/badge/pattern-Tool--calling%20agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📈 Wealth & Investment Management

## 🏦 The business problem (new to banking? start here)

**In the business today:** Markets move, so a client's portfolio drifts away from its agreed mix (e.g. too much in equities after a rally). Advisers rebalance by selling some winners and buying underweight assets, minding taxes.

**Who does this work:** Portfolio managers and advisers.

**Why it's hard:** Rebalancing too little lets risk creep up; doing it carelessly triggers unnecessary taxes and costs.

### Key terms
- **Rebalancing**: Buying and selling to bring a portfolio back to its target allocation after markets move it.
- **Asset allocation**: How a portfolio is split between asset classes (equity, bonds, gold, cash). The biggest driver of risk and return.
- **Capital gains tax**: Tax on profit from selling an investment. Often lower for long-term holdings, so trade timing matters.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Detects drift from target allocation and proposes tax-aware rebalancing trades.

### How it works
Agent uses `current_allocation` and `rebalance_trades` tools and explains each trade.

```mermaid
flowchart LR
    QU["💬 Your question"] --> AG["🤖 LangChain agent<br/>decides which tool to call"]
    AG <-->|"🔧 calls & results"| T["🐍 Python tools<br/>current_allocation()<br/>rebalance_trades()"]
    IN["📄 Holdings + target allocation"] --> T
    AG <-.->|"💬 reasoning"| LLM(["🦙 Ollama"])
    AG --> OUT["📝 Rebalancing trades + reasons"]
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

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 21 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** Review my portfolio and rebalance if needed.

<details><summary>🔧 Tool calls</summary>

```text
current_allocation() -> {"total_value": 174670, "by_class": {"US equity": {"value": 119700, "weight_pct": 68.5, "target_pct": 45, "drift_pp": 23.5}, "Intl equity": {"value": 19200, "weight_pct": 11.0, "target_pct": 20, "drift_pp": -9.0}, "Bonds": {"value": 18850, "weight_pct": 10.8, "target_pct": 25, "drift_pp": -14.2}, "REITs": {"value": 7920, "weight_pct": 4.5, "target_pct": 5, "drift_pp": -0.5}, "Cash": {"value": 9000
rebalance_trades(current_allocation={'Bonds': {'drift_pp': -14.2, 'target_pct': 25, 'value': 18850, 'weight_pct': 10.8}, 'Cash': {'drift_pp': 0.2, 'target_pct': 5, 'value': 9000, 'weight_pct': 5.2}, 'Intl equity': {'drift_pp': -9, 'target_pct': 20, 'value': 19200, 'weight_pct': 11}, 'REITs': {'drift_pp': -0.5, 'target_pct': 5, 'value': 7920, 'weight_pct': 4.5}, 'US equity': {'drift_pp': 23.5, 'target_pct': 45, 'value': 119700, 'weight_pct': 68.5}}) -> [{"ticker": "VTI", "action": "SELL", "amount": 41098, "units": 144.2, "est_gain": 13700, "term": "long-term"}, {"ticker": "VXUS", "action": "BUY", "amount": 15734, "units": 245.8}, {"ticker": "BND", "action": "BUY", "amount": 24818, "units": 342.3}, {"ticker": "VNQ", "action": "BUY", "amount": 814, "units": 9.2}]
```

</details>

**🦙 Ollama:**

Based on the current allocation, we need to rebalance the portfolio to align with the target weights. Here's the drift analysis:

1. **US Equity**: Currently at 68.5%, target is 45%. Drift of +23.5 percentage points.
2. **Intl Equity**: Currently at 11.0%, target is 20%. Drift of -9.0 percentage points.
3. **Bonds**: Currently at 10.8%, target is 25%. Drift of -14.2 percentage points.
4. **REITs**: Currently at 4.5%, target is 5%. Drift of -0.5 percentage points.
5. **Cash**: Currently at 5.2%, target is 5%. Drift of +0.2 percentage points.

To rebalance, we will call the `rebalance_trades` function to determine the exact trades needed. This will ensure we make the necessary adjustments without inventing trade amounts or tax outcomes.

Let's proceed with the rebalance.


To rebalance the portfolio, the following trades are recommended:

1. **Sell VTI (US Equity)**
   - **Action**: SELL
   - **Amount**: $41,098
   - **Units**: 144.2
   - **Estimated Gain**: $13,700 (long-term capital gain)
   - **Explanation**: This sale will help reduce the overweight in US equity, bringing the allocation closer to the target.

2. **Buy VXUS (Intl Equity)**
   - **Action**: BUY
   - **Amount**: $15,734
   - **Units**: 245.8
   - **Explanation**: This purchase will increase the allocation in international equity, aligning it with the target weight.

3. **Buy BND (Bonds)**
   - **Action**: BUY
   - **Amount**: $24,818
   - **Units**: 342.3
   - **Explanation**: This purchase will increase the bond allocation, bringing it closer to the target weight.

4. **Buy VNQ (REITs)**
   - **Action**: BUY
   - **Amount**: $814
   - **Units**: 9.2
   - **Explanation**: This small purchase will help align the REITs allocation with the target weight.

These trades will help restore the portfolio to its target allocation. The estimated gain from the sale of VTI is a long-term capital gain, which is generally more favorable for tax purposes.

**Client Summary:**
Your portfolio has drifted significantly from the target allocation, particularly in US equity. To rebalance, we will sell $41,098 worth of VTI, which will result in a long-term capital gain of $13,700. We will use the proceeds to buy $15,734 worth of VXUS, $24,818 worth of BND, and $814 worth of VNQ. This will help align your portfolio with the target allocation, ensuring better diversification and risk management.


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/27_portfolio_rebalancer/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
