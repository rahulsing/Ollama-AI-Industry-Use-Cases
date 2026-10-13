"""Turn a recorded run (sample_output.txt) into a chat-style conversation.

The README and the interactive explorer replay it as: the user asks -> the steps that really ran
(Python facts, each agent's work, every tool call) -> the model's answer.

Apps that take a question print it themselves ("Question", "Customer", "Q: ...", "You: ...");
for apps that process a batch of sample data, the question comes from ASK in business.py.
"""

import re

from flows import role_icon

USER_SECTIONS = {"Question", "Customer"}
ANSWER_SECTIONS = {"Answer", "Assistant", "Plan", "Quote"}
USER_PREFIXES = ("Q: ", "You: ")
SUMMARY_SECTIONS = {"Summary", "Overall", "Quality report", "Validation", "Cross-document checks"}


def looks_like_data(body: str) -> bool:
    return body.lstrip()[:1] in "{[" or bool(re.search(r'^\s*"[^"]+":', body, re.M)) or "{'" in body


def step(title: str, body: str, pattern: str) -> dict:
    if title == "Tool calls":
        return {"icon": "🔧", "label": "Tool calls", "body": body, "code": True}
    if title.startswith("Agent: "):
        role = title.split(": ", 1)[1]
        return {"icon": role_icon(role), "label": f"{role} (agent)", "body": body, "code": False}
    if pattern == "Structured extraction" and looks_like_data(body) and title not in SUMMARY_SECTIONS:
        return {"icon": "🧾", "label": f"Extracted · {title}", "body": body, "code": True}
    return {"icon": "🐍", "label": f"Python · {title}", "body": body, "code": looks_like_data(body)}


def load(d, slug: str) -> dict | None:
    path = d.path / slug / "sample_output.txt"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    model = re.search(r"^\s*model: (\S+)", text, re.M)
    runtime = re.search(r"^\s*runtime: (\d+)s", text, re.M)
    body = re.sub(r"\A\s*=+\n.*?\n=+\n", "", text, flags=re.S)
    parts = re.split(r"^--- (.+) ---$", body, flags=re.M)
    sections = [(t.strip(), b.strip()) for t, b in zip(parts[1::2], parts[2::2])]
    return {"model": model.group(1) if model else "local model",
            "seconds": int(runtime.group(1)) if runtime else None, "sections": sections}


def conversation(d, u) -> dict | None:
    """{"model", "seconds", "turns": [{"ask", "steps": [...], "answer"}]} or None if no recording."""
    slug, pattern = u[0], u[4]
    rec = load(d, slug)
    if not rec:
        return None
    sections = rec["sections"]
    turns, pending, ask = [], [], None
    if any(t in USER_SECTIONS or t.startswith(USER_PREFIXES) for t, _ in sections):
        for title, body in sections:
            if title.startswith(USER_PREFIXES):
                turns.append({"ask": title.split(": ", 1)[1], "steps": pending, "answer": re.sub(r"^Bot: ", "", body)})
                pending = []
            elif title in USER_SECTIONS:
                ask = body
            elif title in ANSWER_SECTIONS:
                turns.append({"ask": ask, "steps": pending, "answer": body})
                pending, ask = [], None
            else:
                pending.append(step(title, body, pattern))
    else:
        assert slug in d.ask, f"{d.folder}/business.py has no ASK entry for {slug}"
        *before, (last_title, last_body) = sections
        per_item = pattern == "Structured extraction" and last_title not in SUMMARY_SECTIONS
        if per_item:  # each item's extraction is the answer, e.g. one verdict per complaint
            answer = "\n\n".join(f"#### {t}\n```\n{b}\n```" for t, b in sections)
            turns.append({"ask": d.ask[slug], "steps": [], "answer": answer})
        else:
            turns.append({"ask": d.ask[slug], "steps": [step(t, b, pattern) for t, b in before], "answer": last_body})
    return {"model": rec["model"], "seconds": rec["seconds"], "turns": turns}


def readme_section(conv: dict | None) -> str:
    if not conv:
        return ""
    took = f", {conv['seconds']} s" if conv["seconds"] else ""
    out = ["## 💬 Sample conversation", "",
           f"A real recorded run on `{conv['model']}` (local, on a laptop{took}). Expand a step to see what happened",
           "behind the answer. LLM wording changes from run to run; the numbers from Python stay the same.", ""]
    for turn in conv["turns"]:
        out += [f"> **👤 You:** {turn['ask']}", ""]
        for s in turn["steps"]:
            body = f"```{'json' if s['code'] and s['body'].lstrip()[:1] in '{[' else 'text'}\n{s['body']}\n```" if s["code"] else s["body"]
            out += [f"<details><summary>{s['icon']} {s['label']}</summary>", "", body, "", "</details>", ""]
        out += ["**🦙 Ollama:**", "", turn["answer"], "", "---", ""]
    return "\n".join(out[:-2]) + "\n\n"

