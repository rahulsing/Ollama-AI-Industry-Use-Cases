"""Shared Ollama-backed LLM helpers for LangChain and CrewAI use cases.

Everything runs locally against an Ollama server. Configure with env vars
(or a .env file in the repo root):

    OLLAMA_BASE_URL     default http://localhost:11434
    OLLAMA_MODEL        default qwen2.5:7b-instruct   (good tool-calling)
    OLLAMA_EMBED_MODEL  default nomic-embed-text      (used by RAG use cases)
    CREW_VERBOSE        default false
    SHOW_STEPS          default false   (also print each agent's work and every tool call)
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):  # avoid mojibake on Windows consoles
    sys.stdout.reconfigure(encoding="utf-8")

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parents[1] / ".env")
except ImportError:  # python-dotenv is optional
    pass

# Keep CrewAI fully local: no telemetry, no trace upload, no "share trace?" prompt
os.environ.setdefault("OTEL_SDK_DISABLED", "true")
os.environ.setdefault("CREWAI_TRACING_ENABLED", "false")

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b-instruct")
OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")
CREW_VERBOSE = os.getenv("CREW_VERBOSE", "false").lower() in {"1", "true", "yes"}
SHOW_STEPS = os.getenv("SHOW_STEPS", "false").lower() in {"1", "true", "yes"}


# --------------------------------------------------------------------------- #
# LangChain
# --------------------------------------------------------------------------- #
def get_llm(temperature: float = 0.1):
    """Return a LangChain ChatOllama model."""
    from langchain_ollama import ChatOllama

    return ChatOllama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL, temperature=temperature)


def run_chain(system: str, human: str, **variables) -> str:
    """Single prompt -> LLM -> text. Use {placeholders} in `human` for variables."""
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate

    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
    return (prompt | get_llm() | StrOutputParser()).invoke(variables)


def run_structured(system: str, text: str, schema):
    """Extract a Pydantic `schema` instance from free text."""
    llm = get_llm(temperature=0).with_structured_output(schema)
    return llm.invoke([("system", system), ("human", text)])


def run_agent(system_prompt: str, tools: list, question: str) -> str:
    """Run a LangChain tool-calling agent (ReAct loop) and return the final answer."""
    from langchain.agents import create_agent

    agent = create_agent(model=get_llm(), tools=tools, system_prompt=system_prompt)
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    if SHOW_STEPS:
        show_tool_calls(result["messages"])
    # The model may write part of its answer before a follow-up tool call, so keep all of its text
    texts = [m.content for m in result["messages"] if m.type == "ai" and isinstance(m.content, str) and m.content.strip()]
    return "\n\n".join(texts)


# --------------------------------------------------------------------------- #
# CrewAI
# --------------------------------------------------------------------------- #
def get_crew_llm(temperature: float = 0.1):
    """Return a CrewAI LLM pointed at the local Ollama server."""
    from crewai import LLM

    return LLM(model=f"ollama/{OLLAMA_MODEL}", base_url=OLLAMA_BASE_URL, temperature=temperature)


def make_agent(role: str, goal: str, backstory: str, tools: list | None = None):
    """Build a CrewAI agent with sane defaults for small local models."""
    from crewai import Agent

    return Agent(
        role=role,
        goal=goal,
        backstory=backstory,
        tools=tools or [],
        llm=get_crew_llm(),
        allow_delegation=False,
        verbose=CREW_VERBOSE,
        max_iter=5,
    )


def make_task(description: str, expected_output: str, agent, context: list | None = None):
    from crewai import Task

    return Task(description=description, expected_output=expected_output, agent=agent, context=context or [])


def run_crew(agents: list, tasks: list, inputs: dict | None = None) -> str:
    """Run a sequential crew and return the final output as text."""
    from crewai import Crew, Process

    crew = Crew(agents=agents, tasks=tasks, process=Process.sequential, verbose=CREW_VERBOSE, tracing=False)
    result = crew.kickoff(inputs=inputs or {})
    if SHOW_STEPS:  # the final task's output is the return value; show the agents' work before it
        for task, out in zip(tasks[:-1], result.tasks_output):
            section(f"Agent: {task.agent.role}", out.raw)
    return str(result)


# --------------------------------------------------------------------------- #
# Output
# --------------------------------------------------------------------------- #
def banner(title: str) -> None:
    line = "=" * max(60, len(title) + 4)
    print(f"\n{line}\n  {title}\n  model: {OLLAMA_MODEL}\n{line}\n")


def section(title: str, body) -> None:
    print(f"\n--- {title} ---\n{body}\n")


def show_tool_calls(messages: list) -> None:
    """Print every tool the agent called, with its arguments and (shortened) result."""
    outputs = {m.tool_call_id: m.content for m in messages if m.type == "tool"}
    calls = [(c["name"], c["args"], outputs.get(c["id"], "")) for m in messages if m.type == "ai"
             for c in getattr(m, "tool_calls", [])]
    lines = [f"{name}({', '.join(f'{k}={v!r}' for k, v in args.items())}) -> {str(out)[:400]}"
             for name, args, out in calls]
    section("Tool calls", "\n".join(lines) or "(no tools called)")
