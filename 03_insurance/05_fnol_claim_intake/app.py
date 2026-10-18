"""FNOL Claim Intake — LangChain structured output + Ollama.

The LLM classifies each first-notice-of-loss email, then extracts the details for that kind of claim; Python
checks the policy (in force on the loss date, cover bought, excess), missing information and urgency, and
routes each claim; the LLM writes the claims team's work queue.

Run:  python 03_insurance/05_fnol_claim_intake/app.py
"""

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Literal

sys.path.append(str(Path(__file__).resolve().parents[2]))
from pydantic import BaseModel, Field

from common import banner, run_chain, run_structured, section

TODAY = date(2026, 10, 13)
EMAILS = [
    ("Maria Lopez", "Hello, my policy is POL-1001. On 12 Oct 2026 at about 8am another car drove into the back of "
     "mine at the junction of High St and Mill Lane. The other driver, Tom Reed (registration KX19 ABC, insured with "
     "Swift Insurance), said it was his fault. My neck has been sore since. The car is driveable but the boot won't close."),
    ("Edith Harper", "Policy POL-2002. Since this morning, 13 Oct 2026, water has been pouring through the kitchen "
     "ceiling from the upstairs bathroom. I've turned the water off at the stopcock but the ceiling is sagging and the "
     "light fitting is dripping. I'm 82 and live on my own and I don't know who to call."),
    ("Sam Okafor", "Hi, policy POL-3003. Someone broke into my garden shed on 5 Oct 2026 and took two bikes and a "
     "lawnmower, worth about 2,300 in total. The padlock was cut. I haven't reported it to the police yet."),
    ("Priya Shah", "Policy POL-2002. On 30 Sep 2026 my son knocked a tin of paint over our new living room carpet. "
     "The carpet cost 1,400 and I'd like to claim for a replacement."),
]
# What the policy system knows (normally the policy admin system)
POLICIES = {
    "POL-1001": {"product": "motor comprehensive", "start": "2026-02-01", "end": "2027-01-31", "status": "active",
                 "covers": {"accident", "theft", "windscreen"}, "excess": 300},
    "POL-2002": {"product": "home buildings & contents", "start": "2025-11-15", "end": "2026-11-14", "status": "active",
                 "covers": {"escape_of_water", "storm", "fire", "theft"}, "excess": 250,
                 "excess_by_cause": {"escape_of_water": 500}},
    "POL-3003": {"product": "home contents", "start": "2025-10-01", "end": "2026-09-30", "status": "lapsed (not renewed)",
                 "covers": {"escape_of_water", "storm", "fire", "theft"}, "excess": 250},
}
LATE_REPORT_DAYS = 7


# Step 1: what kind of claim is it?
class ClaimType(BaseModel):
    claim_type: Literal["motor_accident", "home_damage", "theft", "other"] = Field(
        description="motor_accident = a vehicle collision; home_damage = damage to a home or its contents (water, "
                    "storm, fire, spills or accidents); theft = something was stolen")
    policy_number: str = Field(description="Policy number, e.g. POL-1001")


# Step 2: a small schema per claim type (small models fill short, specific schemas far more reliably)
class MotorAccident(BaseModel):
    loss_date: str = Field(description="Date of the accident, e.g. 12 Oct 2026")
    third_party_registration: str = Field(description="The other vehicle's registration, or '' if not given")
    third_party_insurer: str = Field(description="The other driver's insurer, or '' if not given")
    third_party_admitted_fault: bool = Field(description="True only if the other driver said it was their fault")
    mentions_pain_or_injury: bool = Field(description="True if the email mentions any pain, soreness or injury to "
                                                      "anyone, even a minor one such as a sore neck")
    vehicle_driveable: bool


class HomeDamage(BaseModel):
    loss_date: str = Field(description="Date the damage happened, e.g. 13 Oct 2026")
    cause: Literal["water_leak", "storm", "fire", "spill_or_drop", "other"] = Field(
        description="water_leak = water leaking or pouring from a pipe, tank, bath, shower or appliance; "
                    "spill_or_drop = a person spilled, dropped or knocked something over")
    emergency: bool = Field(description="True if there is immediate danger, e.g. water near electrics or a collapsing ceiling")
    customer_needs_extra_support: bool = Field(
        description="True if the customer mentions age, living alone, ill health or not knowing what to do")


class Theft(BaseModel):
    loss_date: str = Field(description="Date of the theft, e.g. 5 Oct 2026")
    items_stolen: str = Field(description="What was stolen, briefly")
    estimated_value: float = Field(description="Total value of the stolen items")
    police_crime_reference: str = Field(
        description="The police crime reference (letters and digits), or '' if they haven't reported it yet")


DETAILS = {"motor_accident": MotorAccident, "home_damage": HomeDamage, "theft": Theft}
# Plain-English causes the model picks from -> the policy's cover names
COVER_NAME = {"motor_accident": "accident", "theft": "theft", "water_leak": "escape_of_water",
              "spill_or_drop": "accidental_damage"}


def parse_date(text: str) -> date | None:
    """Date from the model's text ('2026-10-12...', '12 Oct 2026', '12 October 2026')."""
    if m := re.search(r"\d{4}-\d{2}-\d{2}", text or ""):
        return date.fromisoformat(m.group())
    if m := re.search(r"(\d{1,2}) ([A-Za-z]{3})[a-z]* (\d{4})", text or ""):
        return datetime.strptime(" ".join(m.groups()), "%d %b %Y").date()
    return None


def check(customer: str, kind: str, policy_no: str, d: dict) -> dict:
    """Policy, cover, missing information and routing for one claim."""
    p = POLICIES.get(policy_no.strip().upper())
    out = {"customer": customer, "policy": policy_no, "claim_type": kind}
    if not p:
        return out | {"route": "Call the customer: policy number not found", "priority": "normal"}
    loss = parse_date(d.get("loss_date", ""))
    in_force = loss is not None and p["status"] == "active" and \
        date.fromisoformat(p["start"]) <= loss <= date.fromisoformat(p["end"])
    cause = COVER_NAME.get(kind) or COVER_NAME.get(d.get("cause"), d.get("cause"))
    covered = in_force and cause in p["covers"]
    missing, urgent = [], []
    if kind == "theft" and not re.search(r"\d", d.get("police_crime_reference", "")):  # a real reference has digits
        missing.append("police crime reference (required for every theft claim)")
    if kind == "motor_accident" and not d.get("third_party_registration"):
        missing.append("other vehicle's registration")
    if d.get("emergency"):
        urgent.append("emergency: send an emergency plumber and electrician today")
    if d.get("customer_needs_extra_support"):
        urgent.append("customer needs extra support: phone them, don't email")
    if d.get("mentions_pain_or_injury"):
        urgent.append("injury reported: pass to the bodily injury team")
    excess = p.get("excess_by_cause", {}).get(cause, p["excess"]) if covered else None
    recovery = d["third_party_insurer"] if d.get("third_party_admitted_fault") and d.get("third_party_insurer") else None
    late = loss is not None and (TODAY - loss).days > LATE_REPORT_DAYS
    if not in_force:
        route = f"Coverage check: policy {p['status']}, ended {p['end']}, before the loss date"
    elif not covered:
        route = f"Coverage check: '{cause}' is not covered by this {p['product']} policy"
    else:
        route = "Claims handler"
    # Everything the handler must do, in order, so the work queue only has to copy it
    actions = urgent + [f"ask the customer for the {m}" for m in missing]
    if excess:
        actions.append(f"excess to deduct: {excess}")
    if recovery:
        actions.append(f"recover our costs from {recovery} (their driver admitted fault)")
    if not covered:
        actions.append(f"{route[0].lower()}{route[1:]}: handler to confirm before writing to the customer")
    if late:
        actions.append(f"reported {(TODAY - loss).days} days after the loss: note why on the file")
    return out | {
        "loss_date": loss.isoformat() if loss else None, "reported_after_days": (TODAY - loss).days if loss else None,
        "policy_in_force_on_loss_date": in_force, "cause": cause, "covered": covered, "excess": excess,
        "route": route, "priority": "URGENT" if urgent else "normal", "missing_information": missing or None,
        "recovery_from_third_party": recovery, "late_report": late, "actions": actions,
    }


CLASSIFY = ("Classify this first notice of loss and find the policy number. A spill, a dropped item or water "
            "damage at home is home_damage.")
SYSTEM = (
    "You are a claims team leader writing today's work queue from the checked claims, which are already in "
    "priority order. Write EVERY claim, in the order given, in exactly this format:\n"
    "**<priority> · <customer> (<policy>)**: <what happened, under 15 words, in your own words>\n"
    "- <action 1>\n- <action 2>\n"
    "with one bullet for EVERY item of its actions list, copied exactly and in order. Never change the facts, and "
    "add no currency symbols."
)


def main():
    banner("Insurance 05 - FNOL Claim Intake (LangChain structured output)")
    checks = []
    for customer, text in EMAILS:
        email = f"From: {customer}\n\n{text}"
        head = run_structured(CLASSIFY, email, ClaimType)
        details = {}
        if head.claim_type in DETAILS:
            details = run_structured("Extract these claim details from the email.", email,
                                     DETAILS[head.claim_type]).model_dump()
        section(customer, json.dumps({**head.model_dump(), **details}, indent=2))
        checks.append(check(customer, head.claim_type, head.policy_number, details))
    section("Validation", json.dumps(checks, indent=2))
    emails = "\n\n".join(f"From {customer}: {text}" for customer, text in EMAILS)
    queue = sorted(checks, key=lambda c: c["priority"] != "URGENT")  # urgent first, otherwise in arrival order
    section("Action list", run_chain(SYSTEM, "Claim emails:\n{e}\n\nChecked claims ({n}, in priority order):\n{c}",
                                     e=emails, n=len(queue), c=json.dumps(queue, indent=2)))


if __name__ == "__main__":
    main()
