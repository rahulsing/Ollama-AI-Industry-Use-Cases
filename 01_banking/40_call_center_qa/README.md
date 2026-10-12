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
