# 25 · Model Risk Validation Assistant

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 📜 Regulatory & Risk Reporting

## 🏦 The business problem (new to banking? start here)

**In the business today:** Banks use statistical models (e.g. credit scores) to make decisions. An independent team must test each model regularly and report whether it still works.

**Who does this work:** Model validation / Model Risk Management team.

**Why it's hard:** Validation reports are long and technical; findings must be rated and explained to non-specialists.

### Key terms
- **Model risk**: The risk of losses from a model that is wrong or misused. Regulators (e.g. SR 11-7) require independent model validation.
- **Gini / KS / PSI**: Model metrics: Gini and KS measure how well a score separates good and bad customers; PSI measures how much the population has shifted.
- **PD / LGD / EAD**: Probability of Default, Loss Given Default (% lost if default happens) and Exposure at Default (amount owed).

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Reviews a credit model's performance metrics and drafts an SR 11-7 style validation report.

### How it works
Python computes Gini, KS, PSI and calibration; Model Validator and MRM Reviewer agents write findings and ratings.

```mermaid
flowchart LR
    IN["📄 Credit model scores + outcomes"] --> PY["🐍 Python<br/>Gini · KS · PSI · calibration"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🔍 Model Validator"]
        A2["👔 Head of Model Risk Management"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    PY -->|"✅ facts"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 Model validation report"]
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
--- Validation metrics ---
{
  "model": "Retail PD Scorecard v3 (logistic regression)",
  "gini_development": 0.588,
  "gini_out_of_time": 0.546,
  "ks_out_of_time": 0.421,
  "psi_dev_vs_oot": 0.135,
  "avg_predicted_pd_oot": 0.11,
  "observed_default_rate_oot": 0.122,
  "thresholds": {
    "gini_min": 0.4,
    "psi_amber": 0.1,
    "psi_red": 0.25,
    "calibration_tolerance_rel": 0.1
  }
}


--- Test results (RAG) ---
{
  "discrimination (Gini OOT)": "GREEN",
  "stability (PSI)": "AMBER",
  "calibration (predicted vs observed PD)": "GREEN (relative gap 10%)"
}


--- Validation report ---
### Validation Report Summary

#### Scope
The validation process for the Retail PD Scorecard v3 (logistic regression) was conducted to assess the model's performance in terms of discrimination, stability, and calibration. The validation was performed using both development and out-of-time (OOT) data.

#### Summary of Tests

| Test                  | Result | Gini OOT | PSI | Predicted PD OOT | Observed Default Rate OOT | Gini Min | PSI Amber | PSI Red | Calibration Tolerance Rel |
|-----------------------|--------|----------|-----|------------------|---------------------------|---------|----------|---------|---------------------------|
| Discrimination        | GREEN  | 0.588    | -   | -                | -                         | 0.4     | -        | -        | -                         |
| Stability             | AMBER  | -        | 0.135 | -                | -                         | -       | 0.1      | 0.25    | -                         |
| Calibration           | GREEN  | -        | -    | 0.11             | 0.122                     | -       | -        | -        | 0.1                       |

#### Findings with Severity and Remediation

1. **Discrimination (Gini OOT): GREEN**
   - **Meaning**: The Gini coefficient for the out-of-time (OOT) data is 0.546, which is above the minimum threshold of 0.4.
   - **Likely Causes**: The model is performing well in terms of discrimination, likely due to the effective selection of relevant features and the appropriate calibration of the logistic regression coefficients.
   - **Severity**: Low
   - **Remediation**: No immediate action required. Continue to monitor the model's performance and ensure that the relevant features remain relevant and effective.

2. **Stability (PSI): AMBER**
   - **Meaning**: The Population Stability Index (PSI) between the development and out-of-time data is 0.135, which is within the amber range (0.1 to 0.25).
   - **Likely Causes**: The model shows some degree of instability, suggesting that there might be subtle shifts in the distribution of key variables over time. This could be due to changes in customer behavior, economic conditions, or other external factors that are not fully captured by the model.
   - **Severity**: Medium
   - **Remediation**: Implement regular monitoring and periodic retraining of the model to ensure continued stability. Consider incorporating additional features or adjusting the model to better capture changes in the underlying data distribution.

3. **Calibration (Predicted vs Observed PD): GREEN (relative gap 10%)**
   - **Meaning**: The average predicted probability of default (PD) for the out-of-time data is 0.11, and the observed default rate is 0.122. The relative gap between the predicted and observed PD is 10%, which is within the acceptable range.
   - **Likely Causes**: The model is well-calibrated, meaning that the predicted probabilities align reasonably well with the actual observed outcomes. This suggests that the model's risk assessments are reliable and that the predicted PDs are close to the true default rates. The small gap (10%) is within the acceptable tolerance level, indicating that the model is performing as expected in terms of calibration.
   - **Severity**: Low
   - **Remediation**: No immediate action required. Continue to monitor the model's calibration and ensure that the model remains well-calibrated over time.

#### Overall Rating
The overall rating for the Retail PD Scorecard v3 (logistic regression) is **Fit with conditions**. While the model is performing well in terms of discrimination and calibration, there are some signs of potential instability that should be monitored and addressed to ensure long-term reliability.

#### Monitoring Recommendations
1. **Regular Monitoring**: Conduct regular performance monitoring to track changes in the model's performance metrics, particularly the PSI.
2. **Periodic Retraining**: Implement a periodic retraining schedule to ensure that the model remains stable and effective.
3. **Feature Review**: Regularly review the model's input features to ensure they remain relevant and effective.
4. **External Factor Analysis**: Analyze external factors that may impact the model's performance and adjust the model as necessary.

By following these recommendations, the model can continue to provide reliable and accurate predictions for the retail PD scorecard.
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/25_model_risk_validator/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
