"""Policy Coverage Q&A (RAG) — LangChain + Ollama.

Retrieval finds the relevant clauses, the LLM fills a structured coverage checklist, Python decides
COVERED / NOT COVERED from the schedule, and the LLM explains the decision to the customer.

Tip: `ollama pull nomic-embed-text` for semantic retrieval (falls back to keywords).

Run:  python 03_insurance/02_policy_coverage_qa/app.py
      python 03_insurance/02_policy_coverage_qa/app.py "Is accidental damage to my TV covered?"
"""

import re
import sys
from pathlib import Path
from typing import Literal

sys.path.append(str(Path(__file__).resolve().parents[2]))
from pydantic import BaseModel, Field

from common import SimpleRetriever, banner, run_chain, run_structured, section

# Sample home insurance policy wording (fictional) - replace with chunks of your own policy documents
POLICY = [
    ("Section 1.1 Escape of water", "We cover damage to your buildings and contents caused by water escaping from a "
     "fixed water installation, washing machine or dishwasher. We do not cover the cost of repairing the appliance "
     "or pipe itself, or damage from gradual leaks over time."),
    ("Section 1.2 Storm and flood", "We cover damage caused by storm or flood. We do not cover damage to gates, "
     "fences, hedges or garden sheds caused by storm or flood."),
    ("Section 1.3 Theft", "We cover theft from your home involving forcible and violent entry or exit. Theft from "
     "outside the home is only covered if you selected the Personal Possessions add-on."),
    ("Section 1.4 Accidental damage", "Accidental damage to contents (e.g. spilling paint, dropping a TV) is only "
     "covered if Accidental Damage cover is shown in your schedule."),
    ("Section 2 Personal Possessions add-on", "Covers theft of or damage to personal possessions while away from "
     "your home, including phones, jewellery and bicycles, anywhere in the UK and up to 60 days abroad. Bicycles over "
     "1,000 must be named in your schedule. A bicycle stolen while left unattended is covered only if it was locked "
     "to a fixed object such as a bike rack or railing."),
    ("Section 3 Excess", "You pay the first 250 of every claim, or 500 for escape of water claims."),
    ("Your schedule", "Policyholder: J. Patel. Buildings cover: INCLUDED. Contents cover: INCLUDED. "
     "Personal Possessions add-on (Section 2): INCLUDED. Accidental Damage cover (Section 1.4): NOT INCLUDED. "
     "Named items: Trek bicycle, value 1,450."),
    ("General exclusions", "We do not cover wear and tear, damage caused by pets, or loss while the home is "
     "unoccupied for more than 60 consecutive days."),
]

# Which covers this customer bought (normally read from the policy system)
INCLUDED = {"Section 1.1 Escape of water": True, "Section 1.2 Storm and flood": True, "Section 1.3 Theft": True,
            "Section 1.4 Accidental damage": False, "Section 2 Personal Possessions add-on": True}
EXCESS = {"Section 1.1 Escape of water": 500}  # every other claim: 250

Section = Literal["Section 1.1 Escape of water", "Section 1.2 Storm and flood", "Section 1.3 Theft",
                  "Section 1.4 Accidental damage", "Section 2 Personal Possessions add-on", "None of these"]


class Checklist(BaseModel):
    matching_section: Section = Field(
        description="The ONE section whose cover describes this event. Theft or damage away from home = Section 2.")
    conditions_met: bool = Field(description="Does the event meet that section's conditions (e.g. bike locked to a fixed object)?")
    detail: str = Field(description="The condition that decided it, quoted briefly")


class ExclusionCheck(BaseModel):
    applies: bool = Field(description="True only if this exclusion sentence clearly describes the customer's event")


EXTRACT = "Fill in the coverage checklist for the customer's event, using only the policy extracts."
EXPLAIN = (
    "You are a friendly home insurance helpline assistant. The coverage decision below is FINAL. Explain it to the "
    "customer in 3-4 sentences, citing the section in square brackets, and state the excess if covered. Do not "
    "change the decision or invent amounts."
)


def exclusions_for(section_name: str) -> list[str]:
    """The 'We do not cover...' sentences of a section, plus the general exclusions."""
    text = dict(POLICY).get(section_name, "")
    own = [s for s in re.split(r"(?<=\.)\s+", text) if s.startswith("We do not cover")]
    return own + [dict(POLICY)["General exclusions"]]


def decide(c: Checklist, event: str) -> dict:
    """Coverage decision: the matched cover must be in the schedule, its conditions met, and no exclusion applied."""
    included = INCLUDED.get(c.matching_section, False)
    hit = None
    if included and c.conditions_met:
        for exclusion in exclusions_for(c.matching_section):
            check = run_structured("Decide whether this insurance exclusion applies to the customer's event.",
                                   f"Exclusion: {exclusion}\nCustomer event: {event}", ExclusionCheck)
            if check.applies:
                hit = exclusion
                break
    covered = included and c.conditions_met and hit is None
    if c.matching_section == "None of these":
        reason = "no section of the policy covers this event"
    elif not included:
        reason = f"{c.matching_section} is not included in the customer's schedule"
    elif hit:
        reason = f"excluded: {hit}"
    else:
        reason = c.detail
    return {"verdict": "COVERED" if covered else "NOT COVERED", "section": c.matching_section, "reason": reason,
            "excess": EXCESS.get(c.matching_section, 250) if covered else None}


def main():
    banner("Insurance 02 - Policy Coverage Q&A (LangChain RAG)")
    # The schedule and excess apply to every question, so they are always included alongside the retrieved clauses
    always = ("Your schedule", "Section 3 Excess")
    pinned = "\n".join(f"[{s}] {t}" for s, t in POLICY if s in always)
    retriever = SimpleRetriever([f"[{s}] {t}" for s, t in POLICY if s not in always])
    questions = sys.argv[1:] or [
        "My washing machine hose burst and flooded the kitchen. Am I covered?",
        "I dropped my TV while moving it. Can I claim?",
        "My named Trek bike was stolen outside a cafe; I had locked it to a railing.",
        "A storm blew down my garden shed.",
    ]
    for q in questions:
        ctx = "\n".join([pinned] + retriever.search(q, k=3))
        checklist = run_structured(EXTRACT, f"Policy extracts:\n{ctx}\n\nCustomer event: {q}", Checklist)
        decision = decide(checklist, q)
        answer = run_chain(EXPLAIN, "Decision: {d}\n\nPolicy extracts:\n{ctx}\n\nCustomer question: {q}",
                           d=decision, ctx=ctx, q=q)
        section(f"Q: {q}", f"**{decision['verdict']}** ({decision['section']})\n\n{answer}")


if __name__ == "__main__":
    main()
