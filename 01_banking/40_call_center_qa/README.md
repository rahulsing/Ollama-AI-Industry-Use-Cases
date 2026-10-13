# 40 · Call Center QA Analyzer

![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50) ![Pattern](https://img.shields.io/badge/pattern-Multi--agent-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** 🏦 Banking · **Category:** 🙋 Retail Banking & Customer Experience

## 🏦 The business problem (new to banking? start here)

**In the business today:** Quality teams listen to a sample of calls to check agents verified customers securely, handled fraud correctly and treated customers well.

**Who does this work:** Contact centre quality assurance and team leaders.

**Why it's hard:** Only a tiny fraction of calls can be reviewed manually; security failures can enable fraud.

### Key terms
- **Call quality assurance (QA)**: Reviewing a sample of calls to check staff follow security, compliance and service standards.
- **Card fraud / CNP**: Unauthorised card use. Card-Not-Present (online/phone) fraud is the most common type.
- **Vulnerable customer**: Someone more likely to suffer harm (e.g. due to age, illness, bereavement). Banks must take extra care with them.

More terms: [Banking Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
Scores call transcripts for compliance, empathy and resolution and coaches the agent.

### How it works
QA Auditor agent scores against a checklist; Coach agent writes improvement feedback.

```mermaid
flowchart LR
    IN["📄 Call transcript + QA checklist"]
    subgraph CREW["🤖 CrewAI crew: agents work in turn"]
        A1["🔍 QA Auditor"]
        A2["🧑‍🏫 Team Coach"]
        A1 -->|"hands over"| A2
    end
    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4
    IN -->|"📋 case data"| A1
    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])
    A2 --> OUT["📝 QA score + coaching feedback"]
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
--- QA report ---
### Coaching Feedback for the Agent

**Strengths:**
- **Greeting & Identification:** The agent greeted the customer professionally and identified themselves correctly.
- **Ownership & Resolution:** The agent handled the situation with a sense of responsibility and provided a clear timeline for the new card.
- **Closing:** The agent ended the call with a summary and a reference number, ensuring the customer understood the next steps.

**Top 3 Improvements with Better Phrasing Examples:**

1. **Secure Verification:**
   - **Current:** "Agent: Okay. Can you give me your full card number and the CVV so I can check?"
   - **Improved:** "Agent: I'm sorry, but I need to verify your account. Could you please provide your last four digits of your card and your date of birth? I will use this information to secure your account."

2. **Listening & Empathy:**
   - **Current:** "Agent: Yes I see it. It's probably a subscription you forgot. Not much I can do really."
   - **Improved:** "Agent: I understand how concerning this must be for you. Let me check your account again. Could you please provide your date of birth and postcode? I will verify this information to ensure everything is correct."

3. **Correct Handling of Suspected Fraud:**
   - **Current:** "Agent: Okay, blocked. New card in 5 days. Bye."
   - **Improved:** "Agent: I've blocked your account to prevent any unauthorized transactions. I will also raise a fraud claim on your behalf. A new card will be issued within 5 business days. I will send you a reference number for your records. Is there anything else I can assist you with before we end the call?"

**Compliance Escalation Needed:**
- The agent must be trained on secure verification procedures to avoid asking for sensitive information like full card numbers, CVV, PINs, or OTPs. This is a critical fail and must be addressed immediately to ensure customer data security.

By focusing on these areas, the agent can significantly improve their performance and ensure compliance with security protocols.
````

</details>

## Run
```bash
# from the repo root, with Ollama running
python 01_banking/40_call_center_qa/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to Banking use cases](../README.md#-use-cases) · [All industries](../../README.md)
