# 🛡️ Insurance: 10 AI Use Cases

**Property & casualty, motor and home insurers.** AI agents for claims handling, fraud detection, coverage questions, underwriting, pricing, reserving and catastrophe risk.

[⬅ All industries](../README.md) · [New to insurance?](#-new-to-insurance) · [Use cases](#-use-cases) · [Primer & glossary](PRIMER.md)

![Use cases](https://img.shields.io/badge/use%20cases-10-success)
![CrewAI](https://img.shields.io/badge/CrewAI-4-FF5A50)
![LangChain](https://img.shields.io/badge/LangChain-6-1C3C3C)

```bash
# from the repo root, with Ollama running
python 03_insurance/01_claims_triage_fraud/app.py
```

---

## 🎓 New to insurance?

**How an insurer makes money:** customers pay a *premium* to transfer a risk (a car crash, a burglary) to the
insurer. The insurer pools many customers' premiums and pays the *claims* of the few who suffer a loss. Profit comes
from pricing risk correctly (premiums > claims + costs) and from investing premiums before claims are paid.

**What makes it hard:**
1. **Pricing (underwriting):** charge each customer the right premium for their risk. Too low loses money; too high loses customers.
2. **Claims:** pay genuine claims quickly and fairly, while catching fraud, which adds costs for every honest customer.
3. **Clarity:** policies are long legal documents. Customers need clear answers about what they are covered for.
4. **Reserves and catastrophes:** claims are paid over years, so insurers must set aside enough money for claims not yet
   paid (or even reported), and make sure one big storm or flood can't sink the company, using *reinsurance*.

Every use case README starts with **"The business problem"**: what happens today, who does the work, why it's hard,
and the key terms explained. For more, see the **[Insurance Primer & glossary](PRIMER.md)** (52 terms).

| Department | What it does | Use cases |
|---|---|---|
| 🧾 **Claims & Fraud** | Handles losses reported by customers, pays valid claims and investigates suspicious ones. | [01](01_claims_triage_fraud/), [05](05_fnol_claim_intake/), [07](07_total_loss_settlement/), [10](10_claims_leakage_auditor/) |
| 🙋 **Policy & Customer Service** | Answers customers' questions about their cover and handles policy changes. | [02](02_policy_coverage_qa/) |
| 📝 **Underwriting & Pricing** | Decides which risks to accept and at what premium. | [03](03_motor_quote_agent/), [04](04_home_underwriting_assessor/), [06](06_renewal_pricing_advisor/) |
| 📊 **Actuarial & Risk** | Sets aside money for future claims and limits how much one catastrophe could cost. | [08](08_claims_reserving_analyst/), [09](09_cat_exposure_monitor/) |

---

## 📚 Use Cases

### 🧾 Claims & Fraud

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 01 | **Claims Triage & Fraud Detection** | Triages new claims into fast-track, adjuster review or fraud investigation, and spots recovery opportunities. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](01_claims_triage_fraud/) |
| 05 | **FNOL Claim Intake** | Turns first-notice-of-loss emails into checked claims, routed to the right team with urgent cases first. | LangChain | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](05_fnol_claim_intake/) |
| 07 | **Motor Total Loss Settlement Agent** | Explains a write-off settlement: what the car is worth, why it's a write-off and who gets paid what. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](07_total_loss_settlement/) |
| 10 | **Claims Leakage Auditor** | Re-checks closed claims for overpayments and missed recoveries, and plans how to recover money and fix the process. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](10_claims_leakage_auditor/) |

### 🙋 Policy & Customer Service

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 02 | **Policy Coverage Q&A (RAG)** | Answers 'am I covered?' questions from the policy wording and the customer's schedule, with clause citations. | LangChain | RAG | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](02_policy_coverage_qa/) |

### 📝 Underwriting & Pricing

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 03 | **Motor Insurance Quote Agent** | Prices a car insurance policy, explains what drives the premium and answers what-if questions. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](03_motor_quote_agent/) |
| 04 | **Home Insurance Underwriting Assessor** | Decides whether to accept, refer or decline new home insurance applications, with terms and a premium. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](04_home_underwriting_assessor/) |
| 06 | **Renewal Pricing & Retention Advisor** | Prices motor renewals fairly and explains to each customer why their price went up or down. | LangChain | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](06_renewal_pricing_advisor/) |

### 📊 Actuarial & Risk

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 08 | **Claims Reserving Analyst (Chain-Ladder)** | Estimates how much money to hold for future claim payments and whether today's reserves are enough. | LangChain | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](08_claims_reserving_analyst/) |
| 09 | **Catastrophe Exposure Monitor** | Checks whether a 1-in-200 storm or flood would cost more than the board's risk appetite, and what to change. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](09_cat_exposure_monitor/) |

## 🧩 By Framework

### ![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) CrewAI (4)

| # | Use Case | Pattern | Code |
|---|---|---|---|
| 01 | Claims Triage & Fraud Detection | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](01_claims_triage_fraud/) |
| 04 | Home Insurance Underwriting Assessor | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](04_home_underwriting_assessor/) |
| 09 | Catastrophe Exposure Monitor | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](09_cat_exposure_monitor/) |
| 10 | Claims Leakage Auditor | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](10_claims_leakage_auditor/) |

### ![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) LangChain (6)

| # | Use Case | Pattern | Code |
|---|---|---|---|
| 02 | Policy Coverage Q&A (RAG) | RAG | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](02_policy_coverage_qa/) |
| 03 | Motor Insurance Quote Agent | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](03_motor_quote_agent/) |
| 05 | FNOL Claim Intake | Structured extraction | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](05_fnol_claim_intake/) |
| 06 | Renewal Pricing & Retention Advisor | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](06_renewal_pricing_advisor/) |
| 07 | Motor Total Loss Settlement Agent | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](07_total_loss_settlement/) |
| 08 | Claims Reserving Analyst (Chain-Ladder) | Chain | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](08_claims_reserving_analyst/) |

---

[⬅ Back to all industries](../README.md)
