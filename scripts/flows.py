"""Mermaid flow diagrams with icons, used by build_docs.py in the READMEs and the explorer.

One template per pattern. Labels come from each industry's FLOWS (business.py); CrewAI agent
roles and LangChain tool names are read from the use case's app.py, so diagrams match the code.
Colours: blue = data, green = Python (auditable), purple = AI, amber = result.
"""

import re

STYLES = """\
    classDef data fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    classDef rules fill:#d1fae5,stroke:#059669,color:#064e3b
    classDef ai fill:#ede9fe,stroke:#7c3aed,color:#3b0764
    classDef llm fill:#1f2937,stroke:#111827,color:#ffffff
    classDef out fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef human fill:#f3f4f6,stroke:#6b7280,color:#111827"""

LEGEND = "🟦 data · 🟩 Python: maths & rules (auditable) · 🟪 AI: reasoning & writing · ⬛ local LLM · 🟨 result"

ROOT_FLOW = f"""flowchart LR
    U["👤 You"] -->|"▶️ run app.py<br/>or the web UI"| D
    subgraph PC["🔒 Your machine: no data leaves it"]
        D["📄 Business data<br/>application · claims · sales"] --> P["🐍 Python rules<br/>ratios · scores · limits"]
        P -->|"✅ hard facts"| A["🤖 AI agents<br/>CrewAI · LangChain"]
        A <-.->|"💬 prompt / reply"| L(["🦙 Ollama<br/>local LLM"])
        A --> O["📝 Result<br/>memo · decision · answer"]
    end
    O --> H["🧑‍⚖️ Human review<br/>& sign-off"]
{STYLES}
    class D data
    class P rules
    class A ai
    class L llm
    class O out
    class U,H human
    style PC fill:none,stroke:#64748b,stroke-dasharray:5 4"""

# Role keywords -> icon, first match wins
ROLE_ICONS = [("Investigator", "🕵️"), ("Writer", "✍️"), ("Copywriter", "✍️"), ("Coach", "🧑‍🏫"), ("Economist", "📊"),
              ("Strategist", "♟️"), ("Reviewer", "🔍"), ("Auditor", "🔍"), ("Validator", "🔍"), ("Checker", "🔍"),
              ("Assessor", "⚖️"), ("Officer", "👔"), ("Manager", "👔"), ("Head", "👔"), ("Lead", "👔"),
              ("Chief", "👔"), ("Specialist", "🧠"), ("Adjuster", "🧑‍💼"), ("Profiler", "🧑‍💼"), ("Analyst", "🧑‍💼")]


def role_icon(role: str) -> str:
    return next((icon for word, icon in ROLE_ICONS if word in role), "🤖")


def q(text: str) -> str:
    """Make text safe inside a quoted Mermaid label."""
    return text.replace('"', "'")


def code_facts(source: str) -> tuple[list[str], list[str]]:
    agents = re.findall(r'make_agent\(\s*"([^"]+)"', source)
    tools = re.findall(r"@tool[^\n]*\n\s*def (\w+)", source)
    return agents, tools


def use_case_flow(d, u) -> str:
    slug, _, _, _, pattern, _, _ = u
    inp, py, out, *opts = d.flows[slug]
    rules_first = "rules_first" in opts
    agents, tools = code_facts((d.path / slug / "app.py").read_text(encoding="utf-8"))
    lines = ["flowchart LR"]
    add = lines.append
    py_node = f'PY["🐍 Python<br/>{q(py)}"]'
    classes = {"data": ["IN"], "rules": [], "ai": [], "llm": ["LLM"], "out": ["OUT"], "human": ["HU"]}

    if pattern == "Multi-agent":
        start = "IN"
        if py:
            add(f'    IN["📄 {q(inp)}"] --> {py_node}')
            start, first_edge = "PY", '-->|"✅ facts"|'
            classes["rules"].append("PY")
        else:
            add(f'    IN["📄 {q(inp)}"]')
            first_edge = '-->|"📋 case data"|'
        add('    subgraph CREW["🤖 CrewAI crew: agents work in turn"]')
        for i, role in enumerate(agents, 1):
            add(f'        A{i}["{role_icon(role)} {q(role)}"]')
        for i in range(1, len(agents)):
            add(f'        A{i} -->|"hands over"| A{i + 1}')
        add("    end")
        add("    style CREW fill:none,stroke:#7c3aed,stroke-dasharray:5 4")
        add(f"    {start} {first_edge} A1")
        add('    CREW <-.->|"💬 prompts"| LLM(["🦙 Ollama"])')
        add(f'    A{len(agents)} --> OUT["📝 {q(out)}"]')
        classes["ai"] += [f"A{i}" for i in range(1, len(agents) + 1)]

    elif pattern == "Tool-calling agent":
        tool_list = "<br/>".join(f"{t}()" for t in tools)
        add('    QU["💬 Your question"] --> AG["🤖 LangChain agent<br/>decides which tool to call"]')
        add(f'    AG <-->|"🔧 calls & results"| T["🐍 Python tools<br/>{tool_list}"]')
        add(f'    IN["📄 {q(inp)}"] --> T')
        add('    AG <-.->|"💬 reasoning"| LLM(["🦙 Ollama"])')
        add(f'    AG --> OUT["📝 {q(out)}"]')
        classes["data"].append("QU")
        classes["rules"].append("T")
        classes["ai"].append("AG")

    elif pattern == "Chain":
        add(f'    IN["📄 {q(inp)}"] --> {py_node}')
        add('    PY -->|"✅ decision & numbers"| CH["🔗 LangChain prompt<br/>explain, don\'t decide"]')
        add('    CH <-.->|"💬"| LLM(["🦙 Ollama"])')
        add(f'    CH --> OUT["📝 {q(out)}"]')
        classes["rules"].append("PY")
        classes["ai"].append("CH")

    elif pattern == "Structured extraction":
        ex = 'EX["🧾 LangChain structured output<br/>text → Pydantic schema"]'
        if py and rules_first:
            add(f'    IN["📄 {q(inp)}"] --> {py_node}')
            add(f'    PY -->|"✅ rule findings"| {ex}')
            add(f'    EX -->|"validated verdict"| OUT["📝 {q(out)}"]')
        elif py:
            add(f'    IN["📄 {q(inp)}"] --> {ex}')
            add(f'    EX -->|"validated fields"| {py_node}')
            add(f'    PY --> OUT["📝 {q(out)}"]')
        else:
            add(f'    IN["📄 {q(inp)}"] --> {ex}')
            add(f'    EX --> OUT["📝 {q(out)}"]')
        add('    EX <-.->|"💬"| LLM(["🦙 Ollama"])')
        classes["rules"] += ["PY"] if py else []
        classes["ai"].append("EX")

    elif pattern == "RAG":
        add('    QU["❓ Your question"] --> R["🔎 Retriever<br/>finds the most relevant passages"]')
        add(f'    IN["📚 {q(inp)}"] -->|"🧮 embeddings"| R')
        add('    R -->|"📎 top passages"| G["🔗 LangChain<br/>answer only from passages"]')
        add('    G <-.->|"💬"| LLM(["🦙 Ollama"])')
        if py:
            add(f'    G -->|"📋 checklist"| {py_node}')
            add(f'    PY -->|"✍️ explained"| OUT["📝 {q(out)}"]')
            classes["rules"].append("PY")
        else:
            add(f'    G --> OUT["📝 {q(out)}"]')
        classes["data"].append("QU")
        classes["ai"] += ["R", "G"]

    else:
        raise ValueError(f"no flow template for pattern {pattern!r} ({slug})")

    add('    OUT --> HU["🧑‍⚖️ Human review"]')
    lines.append(STYLES)
    lines += [f"    class {','.join(ids)} {name}" for name, ids in classes.items() if ids]
    return "\n".join(lines)


# Short icon chains for the pattern table in the root README
PATTERN_CHAINS = {
    "Multi-agent": "📄 → 🐍 → 🧑‍💼 → 👔 → 📝",
    "Tool-calling agent": "💬 → 🤖 ⇄ 🔧🐍 → 📝",
    "Chain": "📄 → 🐍 decides → 🦙 explains → 📝",
    "Structured extraction": "📄 → 🧾 schema → 🐍 checks → 📝",
    "RAG": "❓ → 🔎 📚 → 🦙 → 💬 + sources",
}
