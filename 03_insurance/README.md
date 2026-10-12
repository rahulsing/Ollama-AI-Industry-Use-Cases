# 🛡️ Insurance: 3 AI Use Cases

**Property & casualty, motor and home insurers.** AI agents for claims handling, fraud detection, coverage questions and pricing.

[⬅ All industries](../README.md) · [New to insurance?](#-new-to-insurance) · [Use cases](#-use-cases) · [Primer & glossary](PRIMER.md)

![Use cases](https://img.shields.io/badge/use%20cases-3-success)
![CrewAI](https://img.shields.io/badge/CrewAI-1-FF5A50)
![LangChain](https://img.shields.io/badge/LangChain-2-1C3C3C)

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

Every use case README starts with **"The business problem"**: what happens today, who does the work, why it's hard,
and the key terms explained. For more, see the **[Insurance Primer & glossary](PRIMER.md)** (19 terms).

| Department | What it does | Use cases |
|---|---|---|
| 🧾 **Claims & Fraud** | Handles losses reported by customers, pays valid claims and investigates suspicious ones. | [01](01_claims_triage_fraud/) |
| 🙋 **Policy & Customer Service** | Answers customers' questions about their cover and handles policy changes. | [02](02_policy_coverage_qa/) |
| 📝 **Underwriting & Pricing** | Decides which risks to accept and at what premium. | [03](03_motor_quote_agent/) |

---

## 📚 Use Cases

### 🧾 Claims & Fraud

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 01 | **Claims Triage & Fraud Detection** | Triages new claims into fast-track, adjuster review or fraud investigation, and spots recovery opportunities. | CrewAI | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](01_claims_triage_fraud/) |

### 🙋 Policy & Customer Service

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 02 | **Policy Coverage Q&A (RAG)** | Answers 'am I covered?' questions from the policy wording and the customer's schedule, with clause citations. | LangChain | RAG | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](02_policy_coverage_qa/) |

### 📝 Underwriting & Pricing

| # | Use Case | Description | Framework | Pattern | Code |
|---|----------|-------------|-----------|---------|------|
| 03 | **Motor Insurance Quote Agent** | Prices a car insurance policy, explains what drives the premium and answers what-if questions. | LangChain | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](03_motor_quote_agent/) |

## 🧩 By Framework

### ![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) CrewAI (1)

| # | Use Case | Pattern | Code |
|---|---|---|---|
| 01 | Claims Triage & Fraud Detection | Multi-agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](01_claims_triage_fraud/) |

### ![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C) LangChain (2)

| # | Use Case | Pattern | Code |
|---|---|---|---|
| 02 | Policy Coverage Q&A (RAG) | RAG | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](02_policy_coverage_qa/) |
| 03 | Motor Insurance Quote Agent | Tool-calling agent | [![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)](03_motor_quote_agent/) |

---

[⬅ Back to all industries](../README.md)
