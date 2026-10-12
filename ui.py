"""Simple web front end for every industry and use case.

Run:  streamlit run ui.py

Pick an industry, a category and a use case in the sidebar and press Run. Each use
case's app.py is run unchanged as a subprocess, so the UI never needs editing when
use cases or industries are added.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))
from domains import load_domains  # noqa: E402

st.set_page_config(page_title="AI Industry Use Cases", page_icon="🤖", layout="wide")


@st.cache_data
def domains():
    return {d.folder: d for d in load_domains()}


DOMAINS = domains()

with st.sidebar:
    st.title("🤖 AI Industry Use Cases")
    folder = st.selectbox("Industry", list(DOMAINS),
                          format_func=lambda f: f"{DOMAINS[f].icon} {DOMAINS[f].name} ({len(DOMAINS[f].use_cases)})")
    d = DOMAINS[folder]
    category = st.selectbox("Category", list(d.categories), format_func=d.categories.get)
    by_slug = {u[0]: u for u in d.use_cases}
    selected = st.radio("Use case", [u[0] for u in d.use_cases if u[2] == category],
                        format_func=lambda s: f"{s[:2]} · {by_slug[s][1]}")
    st.caption(f"Model: `{os.getenv('OLLAMA_MODEL', 'qwen2.5:7b-instruct')}` via Ollama")

slug, title, _, framework, pattern, description, how = by_slug[selected]
app_path = d.path / slug / "app.py"
source = app_path.read_text(encoding="utf-8")

st.header(f"{slug[:2]} · {title}")
st.caption(f"{d.icon} {d.name} · {d.categories[category]} · {framework} · {pattern}")

today, who, why, terms = d.business[slug]
business, ai = st.columns(2)
with business:
    st.subheader(f"{d.icon} The business problem")
    st.markdown(f"**In the business today:** {today}\n\n**Who does it:** {who}\n\n**Why it's hard:** {why}")
    with st.expander("Key terms explained"):
        st.markdown("\n".join(f"- **{t}**: {d.glossary[t][1]}" for t in terms))
with ai:
    st.subheader("🤖 What the AI does")
    st.markdown(f"{description}\n\n**How:** {how}")
with st.expander("View code"):
    st.code(source, language="python")

question = ""
if re.search(r"sys\.argv\[1", source):  # the app accepts a free-text question
    question = st.text_input("Your question (optional; leave blank to use the built-in example)")


def render(output: str) -> None:
    """Show each '--- Section ---' block: JSON-looking bodies as code, the rest as markdown."""
    parts = re.split(r"^--- (.+) ---$", output, flags=re.M)
    for heading, body in zip(parts[1::2], parts[2::2]):
        body = body.strip()
        st.subheader(heading)
        if body[:1] in "{[":
            st.code(body, language="json")
        else:
            st.markdown(body)


if st.button("▶ Run", type="primary"):
    cmd = [sys.executable, str(app_path)] + ([question] if question.strip() else [])
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUNBUFFERED": "1"}
    live, log = st.empty(), ""
    with st.spinner("Running on your local model - CrewAI crews can take a few minutes..."):
        proc = subprocess.Popen(cmd, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                text=True, encoding="utf-8", errors="replace")
        for line in proc.stdout:
            log += line
            live.code(log[-3000:], language="text")
        proc.wait()
    live.empty()
    if proc.returncode == 0:
        render(log)
    else:
        st.error(f"Exited with code {proc.returncode}")
        st.code(log, language="text")
