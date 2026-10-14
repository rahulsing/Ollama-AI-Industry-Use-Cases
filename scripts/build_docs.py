"""Generate all READMEs from each industry's catalog.py and business.py.

Writes:
  README.md                      top level: industry navigation
  NN_industry/README.md          industry catalog
  NN_industry/PRIMER.md          how the industry works + glossary
  NN_industry/NN_slug/README.md  one per use case

Run:  python scripts/build_docs.py
"""

import json

from domains import ROOT, load_domains, load_labs
from flows import LEGEND, PATTERN_CHAINS, ROOT_FLOW, use_case_flow
from samples import conversation, readme_section

DEMO_GIF = ROOT / "docs" / "demo.gif"
REPO_URL = "https://github.com/rahulsing/Ollama-AI-Industry-Use-Cases"
SITE_URL = "https://rahulsing.github.io/Ollama-AI-Industry-Use-Cases/"

FW_BADGE = {
    "CrewAI": "![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-FF5A50)",
    "LangChain": "![LangChain](https://img.shields.io/badge/LangChain-agent-1C3C3C)",
}


def code_badge(link: str) -> str:
    return f"[![Code](https://img.shields.io/badge/Code-Python-3776AB?logo=python&logoColor=white)]({link})"


def anchor(text: str) -> str:
    """GitHub heading anchor for `text`."""
    return "".join(c for c in text.lower().replace(" ", "-") if c.isalnum() or c in "-_")


# --------------------------------------------------------------------------- #
# Industry-level pages
# --------------------------------------------------------------------------- #
def areas_table(d) -> str:
    rows = ["| Department | What it does | Use cases |", "|---|---|---|"]
    for key, name, what in d.areas:
        cases = ", ".join(f"[{u[0][:2]}]({u[0]}/)" for u in d.use_cases if u[2] == key)
        rows.append(f"| {d.categories[key].split(' ', 1)[0]} **{name}** | {what} | {cases} |")
    return "\n".join(rows)


def catalog_tables(d) -> str:
    out = []
    for key, label in d.categories.items():
        rows = [u for u in d.use_cases if u[2] == key]
        out += [f"### {label}\n", "| # | Use Case | Description | Framework | Pattern | Code |",
                "|---|----------|-------------|-----------|---------|------|"]
        out += [f"| {s[:2]} | **{t}** | {desc} | {fw} | {pat} | {code_badge(s + '/')} |"
                for s, t, _, fw, pat, desc, _ in rows]
        out.append("")
    return "\n".join(out)


def framework_lists(d) -> str:
    out = []
    for fw in ("CrewAI", "LangChain"):
        rows = [u for u in d.use_cases if u[3] == fw]
        if not rows:
            continue
        out += [f"### {FW_BADGE[fw]} {fw} ({len(rows)})\n", "| # | Use Case | Pattern | Code |", "|---|---|---|---|"]
        out += [f"| {u[0][:2]} | {u[1]} | {u[4]} | {code_badge(u[0] + '/')} |" for u in rows]
        out.append("")
    return "\n".join(out)


def domain_readme(d) -> str:
    n_crew = sum(u[3] == "CrewAI" for u in d.use_cases)
    first = d.use_cases[0][0]
    return f"""# {d.icon} {d.name}: {len(d.use_cases)} AI Use Cases

**{d.tagline}.** {d.description}

[⬅ All industries](../README.md) · [New to {d.name.lower()}?](#-new-to-{d.name.lower()}) · [Use cases](#-use-cases) · [Primer & glossary](PRIMER.md)

![Use cases](https://img.shields.io/badge/use%20cases-{len(d.use_cases)}-success)
![CrewAI](https://img.shields.io/badge/CrewAI-{n_crew}-FF5A50)
![LangChain](https://img.shields.io/badge/LangChain-{len(d.use_cases) - n_crew}-1C3C3C)

```bash
# from the repo root, with Ollama running
python {d.folder}/{first}/app.py
```

---

## 🎓 New to {d.name.lower()}?

{d.industry_101}
Every use case README starts with **"The business problem"**: what happens today, who does the work, why it's hard,
and the key terms explained. For more, see the **[{d.name} Primer & glossary](PRIMER.md)** ({len(d.glossary)} terms).

{areas_table(d)}

---

## 📚 Use Cases

{catalog_tables(d)}
## 🧩 By Framework

{framework_lists(d)}
---

[⬅ Back to all industries](../README.md)
"""


def primer(d) -> str:
    groups = {}
    for term, (group, definition) in d.glossary.items():
        groups.setdefault(group, []).append((term, definition))
    glossary = []
    for group, items in groups.items():
        glossary.append(f"### {group}\n")
        glossary += [f"- <a id=\"{anchor(t)}\"></a>**{t}**: {desc}" for t, desc in sorted(items, key=lambda x: x[0].lower())]
        glossary.append("")
    return f"""# {d.icon} {d.name} Primer: the business behind the use cases

New to {d.name.lower()}? This page explains how the industry works, which department each use case helps, and every
term used in these use cases, in plain English.

[⬅ Back to {d.name} use cases](README.md)

---

## How it works

{d.industry_101}
## Departments and use cases

{areas_table(d)}

---

## Glossary

{chr(10).join(glossary)}
---

*Definitions are simplified for learning. Exact rules vary by country and regulator.*
"""


# --------------------------------------------------------------------------- #
# Use-case pages
# --------------------------------------------------------------------------- #
def use_case_readme(d, u) -> str:
    slug, title, cat, fw, pattern, desc, how = u
    today, who, why, terms = d.business[slug]
    term_lines = "\n".join(f"- **{t}**: {d.glossary[t][1]}" for t in terms)
    pattern_badge = pattern.replace("-", "--").replace(" ", "%20")
    return f"""# {slug[:2]} · {title}

{FW_BADGE[fw]} ![Pattern](https://img.shields.io/badge/pattern-{pattern_badge}-blue) ![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

**Industry:** {d.icon} {d.name} · **Category:** {d.categories[cat]}

## {d.icon} The business problem (new to {d.name.lower()}? start here)

**In the business today:** {today}

**Who does this work:** {who}

**Why it's hard:** {why}

### Key terms
{term_lines}

More terms: [{d.name} Primer & glossary](../PRIMER.md#glossary)

---

## 🤖 What the AI does
{desc}

### How it works
{how}

```mermaid
{use_case_flow(d, u)}
```

<sub>{LEGEND}</sub>

{readme_section(conversation(d, u))}## Run
```bash
# from the repo root, with Ollama running
python {d.folder}/{slug}/app.py
```

## Customize
- Replace the sample data at the top of `app.py` with your own data source (CSV, database, API).
- Tune thresholds and rules in the Python functions. These are the auditable part of the solution.
- Change the model with `OLLAMA_MODEL` (see the root [README](../../README.md#-model-recommendations)).

> Sample data is fictional; calculations are simplified for learning.

[⬅ Back to {d.name} use cases](../README.md#-use-cases) · [All industries](../../README.md)
"""


# --------------------------------------------------------------------------- #
# Top-level README
# --------------------------------------------------------------------------- #
def labs_table(labs) -> str:
    rows = []
    for lab in labs:
        path = f"labs/{lab['slug']}"
        rows.append(f"| {lab['slug'][:2]} | {lab['icon']} **[{lab['title']}]({path}/)** | {lab['summary']} "
                    f"[Walkthrough with screenshots]({path}/{lab['walkthrough']}) · [Open in the explorer]({SITE_URL}#/labs/{lab['slug']}) "
                    f"| {lab['runs_on']} ({lab['llm'].split(' (')[0].replace('Databricks ', '')}) |")
    return "\n".join(rows)


def root_readme(domains, labs) -> str:
    total = sum(len(d.use_cases) for d in domains)
    n_crew = sum(u[3] == "CrewAI" for d in domains for u in d.use_cases)
    demo = ("\n![Demo: pick an industry and use case, run it on a local LLM, read the result](docs/demo.gif)\n"
            if DEMO_GIF.exists() else "")
    industries = ["| # | Industry | What's inside | Use cases | Explore |", "|---|---|---|---|---|"]
    for d in domains:
        cats = " · ".join(c.split(" ", 1)[1] for c in d.categories.values())
        industries.append(f"| {d.folder[:2]} | {d.icon} **[{d.name}]({d.folder}/)** | {d.tagline}: {cats} | "
                          f"**{len(d.use_cases)}** | [Use cases]({d.folder}/) · [Primer]({d.folder}/PRIMER.md) |")
    sections = []
    for d in domains:
        lines = [f"### {d.icon} [{d.name}]({d.folder}/)\n", d.description, ""]
        for key, label in d.categories.items():
            items = [f"[{u[1]}]({d.folder}/{u[0]}/)" for u in d.use_cases if u[2] == key]
            lines.append(f"- **{label}** ({len(items)}): " + " · ".join(items))
        lines.append("")
        sections.append("\n".join(lines))
    first = domains[0]
    example = f"{first.folder}/{first.use_cases[0][0]}"
    return f"""<div align="center">

# 🦙 Ollama AI Industry Use Cases

### Simple, local AI agents for real business problems, built with **Ollama**, **CrewAI** and **LangChain**

**[🌐 Interactive Explorer]({SITE_URL})** · [Industries](#-industries) · [Hands-on Labs](#-hands-on-labs) · [Quick Start](#-quick-start) · [How It Works](#-how-it-works) · [Project Structure](#-project-structure) · [Contribute](#-contributing)

![Python](https://img.shields.io/badge/Python-3.10--3.13-3776AB?logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/LLM-Ollama%20(local)-000000)
![Industries](https://img.shields.io/badge/industries-{len(domains)}-blueviolet)
![Use cases](https://img.shields.io/badge/use%20cases-{total}-success)
![CrewAI](https://img.shields.io/badge/CrewAI-{n_crew}-FF5A50)
![LangChain](https://img.shields.io/badge/LangChain-{total - n_crew}-1C3C3C)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
{demo}
</div>

---

> **🌐 Browse without installing anything:** the [Interactive Explorer]({SITE_URL}) lets you pick an industry,
> search every solution, read the business problem in plain English, see how the AI flows, replay a real
> conversation with the model, and view the implementation code.

## 💡 What is this?

A hands-on collection of **{total} runnable AI solutions across {len(domains)} industries**. Each one solves a real business
problem with a small, readable Python file.

- **100% local LLMs via [Ollama](https://ollama.com)**: no data leaves your machine. CrewAI telemetry and trace upload are switched off.
- **Two popular frameworks**: [CrewAI](https://github.com/crewAIInc/crewAI) for multi-agent crews and [LangChain](https://github.com/langchain-ai/langchain) for tool-calling agents, chains, extraction and RAG.
- **One file per use case** (`app.py`, ~60-120 lines) with realistic sample data, so each is easy to read, run and adapt.
- **Reliable pattern**: deterministic Python does the maths, rules and thresholds (auditable), and the LLM does the reasoning, explanation and writing.
- **Beginner-friendly**: every industry has a plain-English primer and glossary, and every use case explains the business problem first.

---

## 🏭 Industries

{chr(10).join(industries)}

{chr(10).join(sections)}
---

## 🧪 Hands-on Labs

Longer, guided labs that teach one AI engineering idea step by step. They live in [`labs/`](labs/) and run
outside Ollama, so they're kept apart from the use cases above.

| # | Lab | What you learn | Runs on |
|---|---|---|---|
{labs_table(labs)}

---

## 🚀 Quick Start

```bash
# 1. Install Ollama (https://ollama.com/download) and pull a model
ollama pull qwen2.5:7b-instruct        # default: strong tool calling at 7B
ollama pull nomic-embed-text           # embeddings for the RAG use cases

# 2. Clone and install (Python 3.10 - 3.13)
git clone https://github.com/rahulsing/Ollama-AI-Industry-Use-Cases.git
cd Ollama-AI-Industry-Use-Cases
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env                                   # optional: change model / Ollama URL

# 3. Run any use case: python <industry>/<use-case>/app.py
python {example}/app.py

# 4. Or use the web UI: pick an industry and use case, then click Run
#    (or "Replay a recorded run" to try it without Ollama)
streamlit run ui.py
```

### 🧠 Model recommendations

| Model | Size | Notes |
|-------|------|-------|
| `qwen2.5:7b-instruct` | 4.7 GB | **Default.** Reliable tool calling & JSON output on a laptop |
| `llama3.1:8b` | 4.9 GB | Good all-rounder |
| `qwen2.5:14b` / `gemma3:27b` | 9-17 GB | Better reasoning for the CrewAI report writers |
| `gpt-oss:20b`, `qwen2.5:72b` | 13-47 GB | Best quality if you have the GPU memory |

Switch with `OLLAMA_MODEL=llama3.1:8b python ...` or in `.env`. Set `CREW_VERBOSE=true` to watch CrewAI agents think, or `SHOW_STEPS=true` to also print each agent's work and
every tool call (this is what the sample conversations show).

---

## ⚙️ How It Works

Every use case follows the same idea: **Python does the maths and the rules, the AI explains and writes**, and
everything runs on your own machine.

```mermaid
{ROOT_FLOW}
```

<sub>{LEGEND}</sub>

Each use case README has its own diagram showing the real agents and tools from its code.

| Pattern | Flow | When to use | Examples |
|---------|------|-------------|----------|
| **Multi-agent (CrewAI)** | {PATTERN_CHAINS['Multi-agent']} | Analysis + review + write-up, like a committee | [Credit risk](01_banking/01_credit_risk_assessment/), [AML](01_banking/09_aml_transaction_monitoring/), [Claims fraud](03_insurance/01_claims_triage_fraud/) |
| **Tool-calling agent (LangChain)** | {PATTERN_CHAINS['Tool-calling agent']} | Questions that need live calculations or system lookups | [Loan underwriting](01_banking/02_loan_underwriting_assistant/), [Replenishment](02_retail/01_demand_forecasting_agent/), [Motor quote](03_insurance/03_motor_quote_agent/) |
| **Chain (LangChain)** | {PATTERN_CHAINS['Chain']} | Python decides, the LLM explains | [Card fraud](01_banking/13_card_fraud_explainer/), [Liquidity](01_banking/20_liquidity_lcr_nsfr_monitor/) |
| **Structured extraction** | {PATTERN_CHAINS['Structured extraction']} | Unstructured text to a validated schema | [Loan documents](01_banking/08_loan_document_extractor/), [Product reviews](02_retail/02_product_review_analyzer/) |
| **RAG** | {PATTERN_CHAINS['RAG']} | Q&A grounded in policies or documents | [Bank policy Q&A](01_banking/24_policy_qa_rag/), [Insurance coverage Q&A](03_insurance/02_policy_coverage_qa/) |

### Framework comparison

| | CrewAI | LangChain |
|---|---|---|
| Best for | Role-based collaboration, long-form reports | Tools, chains, extraction, RAG, chatbots |
| Multi-agent | ✅ native (crews, tasks, context) | ✅ via LangGraph |
| Local LLM (Ollama) | ✅ `LLM(model="ollama/...")` | ✅ `ChatOllama` |
| Used here for | {n_crew} use cases | {total - n_crew} use cases |

---

## 📁 Project Structure

```
├── 01_banking/                 # one numbered folder per industry
│   ├── README.md               # industry catalog (generated)
│   ├── PRIMER.md               # how the industry works + glossary (generated)
│   ├── catalog.py              # use-case list for this industry
│   ├── business.py             # plain-English business context + glossary
│   └── 01_credit_risk_assessment/
│       ├── app.py              # self-contained runnable use case
│       ├── sample_output.txt   # real output from a local run (scripts/capture_samples.py)
│       └── README.md
├── 02_retail/  03_insurance/   # same layout
├── labs/                       # guided hands-on labs (not Ollama; see labs/README.md)
├── common/                     # shared Ollama helpers (LangChain + CrewAI) and RAG retriever
├── scripts/build_docs.py       # regenerates every README, primer, flow diagram and the explorer
├── scripts/capture_samples.py  # records a real run of every use case for the sample conversations
├── ui.py                       # optional Streamlit front end
├── docs/                       # GitHub Pages: index.html (interactive explorer, generated) + demo.gif
├── requirements.txt
└── .env.example
```

---

## 🤝 Contributing

**Add a use case:** copy a folder with the same pattern into the industry folder, keep it self-contained (one
`app.py`, sample data inline, Ollama only), add it to that industry's `catalog.py` and `business.py` (business context, a `FLOWS` entry for the
diagram and, if the app takes no question, an `ASK` entry for the sample conversation), then run `python scripts/capture_samples.py --missing` (saves a real sample response) and
`python scripts/build_docs.py`.

**Add an industry:** create `04_<industry>/` with a `catalog.py` and `business.py` (copy `02_retail/` as a template)
and at least one use case. The README, primer and UI pick it up automatically.

Ideas welcome: healthcare, telecom, energy, manufacturing, public sector...

---

## 📄 License

[MIT](LICENSE) © 2026 DataTechBridge. Free to use, modify and share, including commercially.

---

## ⚠️ Disclaimer

All data, people, companies, policies and regulations in this repo are **fictional sample data** for education.
Calculations are simplified illustrations of industry concepts and are **not** production models or professional
(financial, insurance or legal) advice. Validate any model and keep a human in the loop before real use.

<div align="center">

⭐ **If this helps you, star the repo!** ⭐

</div>
"""


# --------------------------------------------------------------------------- #
# Interactive explorer (GitHub Pages: docs/index.html)
# --------------------------------------------------------------------------- #
def site(domains, labs) -> str:
    data = {"repo": REPO_URL, "root_flow": ROOT_FLOW, "legend": LEGEND, "industries": [],
            "labs": labs}
    for d in domains:
        cases = []
        for u in d.use_cases:
            slug, title, cat, fw, pattern, desc, how = u
            today, who, why, terms = d.business[slug]
            cases.append({"slug": slug, "title": title, "category": cat, "framework": fw, "pattern": pattern,
                          "description": desc, "how": how, "today": today, "who": who, "why": why, "terms": terms,
                          "code": (d.path / slug / "app.py").read_text(encoding="utf-8"),
                          "flow": use_case_flow(d, u), "chat": conversation(d, u)})
        data["industries"].append({"folder": d.folder, "name": d.name, "icon": d.icon, "tagline": d.tagline,
                                   "description": d.description, "industry_101": d.industry_101,
                                   "categories": d.categories, "areas": d.areas, "glossary": d.glossary,
                                   "use_cases": cases})
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")  # safe inside <script>
    template = (ROOT / "scripts" / "site_template.html").read_text(encoding="utf-8")
    return template.replace("__DATA__", payload)


def main():
    domains = load_domains()
    labs = load_labs()
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs" / "index.html").write_text(site(domains, labs), encoding="utf-8", newline="\n")
    (ROOT / "README.md").write_text(root_readme(domains, labs), encoding="utf-8", newline="\n")
    pages = 1
    for d in domains:
        (d.path / "README.md").write_text(domain_readme(d), encoding="utf-8", newline="\n")
        (d.path / "PRIMER.md").write_text(primer(d), encoding="utf-8", newline="\n")
        pages += 2
        for u in d.use_cases:
            folder = d.path / u[0]
            assert (folder / "app.py").exists(), f"missing {folder / 'app.py'}"
            assert u[0] in d.business, f"{d.folder}/business.py has no BUSINESS entry for {u[0]}"
            missing = [t for t in d.business[u[0]][3] if t not in d.glossary]
            assert not missing, f"{d.folder}: glossary missing {missing}"
            assert u[0] in d.flows, f"{d.folder}/business.py has no FLOWS entry for {u[0]}"
            (folder / "README.md").write_text(use_case_readme(d, u), encoding="utf-8", newline="\n")
            pages += 1
    print(f"Wrote docs/index.html and {pages} pages for {len(domains)} industries: "
          + ", ".join(f"{d.name} ({len(d.use_cases)})" for d in domains) + f"; {len(labs)} lab(s)")


if __name__ == "__main__":
    main()
