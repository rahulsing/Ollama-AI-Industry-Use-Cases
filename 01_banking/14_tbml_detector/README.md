# 14 · Trade-Based Money Laundering Detector

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🕵️ Financial Crime & Compliance

## 🏦 The business problem (new to banking? start here)

**In the business today:** Trade finance teams check that goods, prices and shipping routes make commercial sense, because criminals use fake trade invoices to move money across borders.

**Who does this work:** Trade finance operations and financial crime specialists.

**Why it's hard:** Requires knowing what goods normally cost and how they normally ship; red flags are subtle.

### Key terms
- **TBML (Trade-Based Money Laundering)**: Disguising criminal money as trade, e.g. invoicing goods at fake prices to move value across borders.
- **Trade finance**: Bank services that help importers and exporters trade safely, e.g. Letters of Credit and guarantees.
- **Letter of Credit (LC)**: A bank's promise to pay an exporter if they present documents that exactly match the LC's terms.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Flags over/under-invoicing and suspicious trade routes in trade finance transactions.

### How it works
Python compares unit prices to benchmarks; a Trade Finance Analyst and a TBML Specialist agent assess red flags.

```mermaid
flowchart LR
    IN["📄 Trade invoices + shipping routes"] --> PY["🐍 Python<br/>Unit price vs. benchmark · transhipment hubs"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🧑‍💼 Trade Finance Analyst"]
        A2["🧠 TBML Specialist"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 TBML risk assessment"]
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

A real recorded run on `qwen2.5:7b-instruct` (local, on a laptop, 42 s). Expand a step to see what happened
behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.

> **👤 You:** Check these three trade finance deals for trade-based money laundering red flags.

<details><summary>🐍 Python · Pricing & route analysis</summary>

```json
[
  {
    "lc": "LC-301",
    "unit_price": 3.3,
    "deviation_pct": 3,
    "flags": []
  },
  {
    "lc": "LC-302",
    "unit_price": 824.0,
    "deviation_pct": 358,
    "flags": [
      "Over-invoicing: unit price 824.00 vs benchmark 180.0 (+358%)",
      "Transhipment via AE not required for route",
      "Beneficiary free-zone entity, not the manufacturer"
    ]
  },
  {
    "lc": "LC-303",
    "unit_price": 2.45,
    "deviation_pct": -74,
    "flags": [
      "Under-invoicing: unit price 2.45 vs benchmark 9.5 (-74%)",
      "Transhipment via PA not required for route"
    ]
  }
]
```

</details>

<details><summary>🧑‍💼 Trade Finance Analyst (agent)</summary>

### Per-LC Commercial Assessment

#### LC-301: Cotton T-shirts
- **Unit Price**: $3.30 per T-shirt
- **Deviation Pct**: 3%
- **Flags**: None

**Commercial Rationale**:
- **Unit Price**: The unit price of $3.30 per T-shirt is within a reasonable range for cotton T-shirts, considering the typical cost of production and the market price in the destination country (Germany). The deviation of 3% from the benchmark is minimal, indicating that the pricing is commercially plausible.
- **Shipping Route**: The goods are being shipped directly from Bangladesh (BD) to Germany (DE), which is a common route for textile imports. There is no transhipment via another country, which is also typical for such shipments.
- **Applicant and Beneficiary**: Nordmode GmbH, a German company, is the applicant, and Dhaka Knit Ltd, a Bangladeshi company, is the beneficiary. This is a standard arrangement for textile imports, where the German company sources the goods from a Bangladeshi manufacturer.

**Conclusion**: The trade for cotton T-shirts is commercially plausible and aligns with typical trade practices.

---

#### LC-302: Used Laptops
- **Unit Price**: $824.00 per laptop
- **Deviation Pct**: 358%
- **Flags**: 
  - **Over-invoicing**: The unit price of $824.00 is significantly higher than the benchmark of $180.00, indicating over-invoicing by 358%.
  - **Transhipment**: Transhipment via the United Arab Emirates (AE) is not required for the route from China (CN) to Nigeria (NG).
  - **Beneficiary**: The beneficiary, Gulf Star Trading FZE, is a free-zone entity, which is not the manufacturer of the goods.

**Commercial Rationale**:
- **Unit Price**: The unit price of $824.00 per laptop is extremely high, which is not typical for used laptops. This could indicate over-invoicing, which is a red flag in trade finance.
- **Transhipment**: Transhipment via the UAE is not necessary, and the goods can be shipped directly from China to Nigeria, which is more cost-effective and reduces the risk of delays.
- **Beneficiary**: The beneficiary is a free-zone entity, which is not the manufacturer of the goods. This could suggest that the goods are being resold or that there is a discrepancy in the supply chain.

**Conclusion**: The trade for used laptops is commercially questionable due to the high unit price and the presence of over-invoicing. Additionally, the transhipment and the beneficiary being a free-zone entity raise concerns about the authenticity and legitimacy of the trade.

---

#### LC-303: Frozen Shrimp (kg)
- **Unit Price**: $0.245 per kg
- **Deviation Pct**: -74%
- **Flags**: 
  - **Under-invoicing**: The unit price of $0.245 per kg is significantly lower than the benchmark of $9.50 per kg, indicating under-invoicing by 74%.
  - **Transhipment**: Transhipment via Panama (PA) is not required for the route from Vietnam (VN) to the United States (US).

**Commercial Rationale**:
- **Unit Price**: The unit price of $0.245 per kg is unusually low for frozen shrimp, which is not typical for such high-value seafood. This could indicate under-invoicing, which is a significant risk in trade finance.
- **Transhipment**: Transhipment via Panama is not necessary, and the goods can be shipped directly from Vietnam to the United States, which is more cost-effective and reduces the risk of delays.

**Conclusion**: The trade for frozen shrimp is commercially questionable due to the low unit price and the presence of under-invoicing. Additionally, the transhipment is not required, which further raises concerns about the authenticity and legitimacy of the trade.

### Summary
- **LC-301 (Cotton T-shirts)**: Commercially plausible.
- **LC-302 (Used Laptops)**: Commercially questionable due to over-invoicing and other discrepancies.
- **LC-303 (Frozen Shrimp)**: Commercially questionable due to under-invoicing and other discrepancies.

</details>

**🦙 Ollama:**

### Per-LC Risk Rating, Red Flags, and Recommended Actions

#### LC-301: Cotton T-shirts
- **Per-LC Risk Rating**: LOW
- **Red Flags**: None
- **Recommended Actions**: None

**Commercial Rationale**:
- The unit price of $3.30 per T-shirt is within a reasonable range, and the deviation of 3% from the benchmark is minimal.
- The shipping route is direct from Bangladesh to Germany, which is typical for such shipments.
- The applicant and beneficiary are standard for textile imports.

**Conclusion**: The trade for cotton T-shirts is commercially plausible and aligns with typical trade practices.

---

#### LC-302: Used Laptops
- **Per-LC Risk Rating**: MEDIUM
- **Red Flags**: Over-invoicing, Beneficiary is a free-zone entity, Transhipment via UAE is not required
- **Recommended Actions**:
  - **Request Price Justification**: Verify the justification for the high unit price of $824.00 per laptop.
  - **Verify Shipment via Vessel Tracking**: Ensure the shipment is not transhipped via the UAE, as it is not required.
  - **EDD on Beneficiary**: Conduct enhanced due diligence (EDD) on the beneficiary, Gulf Star Trading FZE, to verify its legitimacy and connection to the goods.

**Commercial Rationale**:
- The unit price of $824.00 per laptop is extremely high, which is not typical for used laptops.
- Transhipment via the UAE is not necessary, and the goods can be shipped directly from China to Nigeria.
- The beneficiary is a free-zone entity, which is not the manufacturer of the goods.

**Conclusion**: The trade for used laptops is commercially questionable due to the high unit price and the presence of over-invoicing. Additionally, the transhipment and the beneficiary being a free-zone entity raise concerns about the authenticity and legitimacy of the trade.

---

#### LC-303: Frozen Shrimp (kg)
- **Per-LC Risk Rating**: MEDIUM
- **Red Flags**: Under-invoicing, Transhipment via Panama is not required
- **Recommended Actions**:
  - **Request Price Justification**: Verify the justification for the low unit price of $0.245 per kg.
  - **Verify Shipment via Vessel Tracking**: Ensure the shipment is not transhipped via Panama, as it is not required.
  - **EDD on Beneficiary**: Conduct enhanced due diligence (EDD) on the beneficiary to verify its legitimacy and connection to the goods.

**Commercial Rationale**:
- The unit price of $0.245 per kg is unusually low for frozen shrimp, which is not typical for such high-value seafood.
- Transhipment via Panama is not necessary, and the goods can be shipped directly from Vietnam to the United States.
- The beneficiary is a free-zone entity, which is not the manufacturer of the goods.

**Conclusion**: The trade for frozen shrimp is commercially questionable due to the low unit price and the presence of under-invoicing. Additionally, the transhipment is not required, which further raises concerns about the authenticity and legitimacy of the trade.

### Summary
- **LC-301 (Cotton T-shirts)**: LOW risk, no red flags, no recommended actions.
- **LC-302 (Used Laptops)**: MEDIUM risk, over-invoicing, free-zone beneficiary, and unnecessary transhipment, recommend price justification, vessel tracking, and EDD.
- **LC-303 (Frozen Shrimp)**: MEDIUM risk, under-invoicing, free-zone beneficiary, and unnecessary transhipment, recommend price justification, vessel tracking, and EDD.


## Run
```bash
# from the repo root, with Ollama running
python 01_banking/14_tbml_detector/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
