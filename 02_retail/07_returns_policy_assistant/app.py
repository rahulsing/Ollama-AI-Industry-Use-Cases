"""Returns & Refund Policy Assistant (RAG) — LangChain + Ollama.

Retrieval finds the relevant policy sections, the LLM turns the customer's message into a returns checklist,
Python applies the policy rules (windows, fees, proof of purchase) and the LLM explains the decision.

Tip: `ollama pull nomic-embed-text` for semantic retrieval (falls back to keywords).

Run:  python 02_retail/07_returns_policy_assistant/app.py
      python 02_retail/07_returns_policy_assistant/app.py "Can I return headphones I opened 20 days ago?"
"""

import sys
from pathlib import Path
from typing import Literal

sys.path.append(str(Path(__file__).resolve().parents[2]))
from pydantic import BaseModel, Field

from common import SimpleRetriever, banner, run_chain, run_structured, section

# Sample returns policy (fictional) - replace with chunks of your own policy pages
POLICY = [
    ("Section 1 Standard returns", "Most items can be returned within 30 days of purchase in their original "
     "condition for a full refund to the original payment method."),
    ("Section 2 Electronics", "Electronics (laptops, phones, headphones, cameras) can be returned within 15 days of "
     "purchase. Opened electronics carry a 15% restocking fee unless they are faulty."),
    ("Section 3 Final sale", "Items marked final sale, including all clearance items, cannot be returned or "
     "exchanged unless they are faulty."),
    ("Section 4 Faulty items", "If an item develops a fault within 1 year of purchase we will repair, replace or "
     "refund it, with no restocking fee."),
    ("Section 5 Proof of purchase", "We accept a receipt, an order confirmation email, or the payment card used, "
     "which we can look up for purchases in the last 90 days. Without proof of purchase we can only offer store "
     "credit at the item's lowest selling price in the last 30 days."),
    ("Section 6 Hygiene items", "For hygiene reasons, swimwear, earrings and underwear can only be returned unopened "
     "with the hygiene seal intact."),
    ("Section 7 Gift cards", "Gift cards cannot be returned or exchanged for cash."),
]
STANDARD_DAYS, ELECTRONICS_DAYS, FAULTY_DAYS, CARD_LOOKUP_DAYS = 30, 15, 365, 90
RESTOCKING_FEE = 0.15
# The policy's own product lists (Sections 2 and 6), applied by Python rather than guessed by the model
ELECTRONICS = {"laptop", "phone", "smartphone", "headphones", "earbuds", "camera", "tablet", "tv"}
HYGIENE = {"swimsuit", "swimwear", "bikini", "earrings", "underwear"}


class ReturnRequest(BaseModel):
    item: str = Field(description="The product, in one or two words, e.g. 'laptop', 'swimsuit', 'jacket'")
    final_sale: bool = Field(description="True ONLY if the customer says it was bought on clearance or as final sale")
    faulty: bool = Field(description="True only if the item is broken or stopped working, not if they just dislike it")
    opened_or_used: bool = Field(description="True if opened, tried on, worn or used")
    days_since_purchase: int = Field(description="Approximate days since purchase (1 month = 30 days)")
    proof: Literal["receipt", "card", "none"] = Field(
        description="receipt = receipt or order confirmation email; card = only the payment card; none = no proof")


def category(item: str) -> str:
    words = set(item.lower().replace("-", " ").split())
    return "electronics" if words & ELECTRONICS else "hygiene" if words & HYGIENE else "other"


def decide(r: ReturnRequest) -> dict:
    """Apply the returns policy. Returns the decision and the sections it relied on."""
    fee, kind = 0.0, category(r.item)
    if r.faulty:  # faults override final sale and hygiene rules
        rule, window, outcome = "Section 4 Faulty items", FAULTY_DAYS, "repair, replacement or refund"
    elif r.final_sale:
        rule, window, outcome = "Section 3 Final sale", None, "final sale: not returnable"
    elif kind == "hygiene" and r.opened_or_used:
        rule, window, outcome = "Section 6 Hygiene items", None, "opened hygiene item: not returnable"
    elif kind == "electronics":
        rule, window, outcome = "Section 2 Electronics", ELECTRONICS_DAYS, "refund"
        fee = RESTOCKING_FEE if r.opened_or_used else 0.0
    else:
        rule, window, outcome = "Section 1 Standard returns", STANDARD_DAYS, "refund"
    ok = window is not None and r.days_since_purchase <= window
    if window and not ok:
        outcome = f"outside the {window}-day return window"
    sections, refund_to, proof = [rule], None, None
    if ok:
        sections.append("Section 5 Proof of purchase")
        card_found = r.proof == "card" and r.days_since_purchase <= CARD_LOOKUP_DAYS
        proof = ("receipt or order confirmation" if r.proof == "receipt" else
                 f"payment card lookup (accepted for purchases in the last {CARD_LOOKUP_DAYS} days)" if card_found
                 else "none")
        refund_to = ("original payment method" if r.proof == "receipt" or card_found
                     else "store credit at the lowest selling price in the last 30 days")
    return {"item": r.item, "category": kind, "decision": "RETURN ACCEPTED" if ok else "RETURN DECLINED", "outcome": outcome,
            "days_since_purchase": r.days_since_purchase, "return_window_days": window,
            "restocking_fee": f"{fee:.0%}" if ok and fee else "none", "proof_of_purchase": proof,
            "refund_to": refund_to, "policy_sections": sections}


EXTRACT = (
    "Fill in the returns checklist from the customer's message. Read each field's description carefully. "
    "final_sale is false unless the message mentions clearance or final sale. faulty is false if the customer "
    "simply doesn't like the item. Do not guess facts they didn't give."
)
EXPLAIN = (
    "You are a friendly customer service assistant for a retailer. The returns decision below is FINAL. Explain it "
    "to the customer in 3-4 sentences, citing the policy section in square brackets, and say how they will be "
    "refunded and any fee. If declined, offer a helpful alternative from the policy. Do not change the decision."
)


def main():
    banner("Retail 07 - Returns & Refund Policy Assistant (LangChain RAG)")
    retriever = SimpleRetriever([f"[{s}] {t}" for s, t in POLICY])
    questions = sys.argv[1:] or [
        "I bought a laptop 10 days ago and opened it, but I don't like it. Can I return it? I have the receipt.",
        "Can I return a swimsuit I bought on clearance 5 days ago? I tried it on.",
        "My blender stopped working after 3 months. I have the order confirmation email.",
        "I lost the receipt for a jacket I bought 20 days ago, but I paid with my debit card. It still has the tags.",
    ]
    for q in questions:
        request = run_structured(EXTRACT, q, ReturnRequest)
        decision = decide(request)
        passages = retriever.search(q, k=3)
        passages += [f"[{s}] {t}" for s, t in POLICY if s in decision["policy_sections"] and f"[{s}] {t}" not in passages]
        answer = run_chain(EXPLAIN, "Decision: {d}\n\nPolicy extracts:\n{ctx}\n\nCustomer message: {q}",
                           d=decision, ctx="\n".join(passages), q=q)
        section(f"Q: {q}", f"**{decision['decision']}** ({', '.join(decision['policy_sections'])})\n\n{answer}")


if __name__ == "__main__":
    main()
