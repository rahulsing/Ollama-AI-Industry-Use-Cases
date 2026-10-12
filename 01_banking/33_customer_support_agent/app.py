"""Banking Customer Support Agent — LangChain tool-calling agent + Ollama.

Interactive chat over a mock core-banking API.

Run:  python 01_banking/33_customer_support_agent/app.py            (demo questions)
      python 01_banking/33_customer_support_agent/app.py --chat     (interactive)
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from langchain.agents import create_agent
from langchain_core.tools import tool

from common import banner, get_llm, section

CUSTOMER_ID = "CUST-1001"  # assume the user is already authenticated in the app
ACCOUNTS = {"SAV-221": {"type": "Savings", "balance": 4_215.40}, "CUR-993": {"type": "Current", "balance": 812.10}}
TXNS = [("2026-10-09", "SAV-221", -64.20, "Amazon"), ("2026-10-08", "SAV-221", 2_800.00, "Salary ACME Ltd"),
        ("2026-10-07", "CUR-993", -120.00, "Electric Co Direct Debit"), ("2026-10-06", "SAV-221", -18.75, "Coffee House")]
CARDS = {"4821": {"type": "Debit", "status": "Active"}, "7710": {"type": "Credit", "status": "Active"}}


@tool
def get_balance(account_id: str = "") -> dict:
    """Get balances. Leave account_id empty for all accounts."""
    return {account_id: ACCOUNTS[account_id]} if account_id in ACCOUNTS else ACCOUNTS


@tool
def recent_transactions(limit: int = 5) -> list:
    """Most recent transactions across accounts (date, account, amount, description)."""
    return TXNS[:limit]


@tool
def block_card(last4: str, reason: str) -> str:
    """Block a card immediately by its last 4 digits. reason: lost, stolen or suspected_fraud."""
    if last4 not in CARDS:
        return f"No card ending {last4}."
    CARDS[last4]["status"] = "Blocked"
    return f"Card ending {last4} blocked ({reason}). Replacement dispatched in 5 working days. Ref BLK-{last4}-2026."


@tool
def branch_hours(city: str) -> str:
    """Branch opening hours for a city."""
    return f"{city.title()} branches: Mon-Fri 9:30-16:30, Sat 9:30-13:00. 24/7 phone support: 0800 123 456."


SYSTEM = (
    f"You are a helpful, concise banking support assistant for authenticated customer {CUSTOMER_ID}. "
    "Use tools to answer; never invent balances. Before blocking a card, confirm which card if ambiguous. "
    "Never ask for PINs, passwords or OTPs. For complaints or anything you cannot do, offer to connect a human agent."
)


def main():
    banner("33 - Banking Customer Support Agent (LangChain agent)")
    agent = create_agent(model=get_llm(), tools=[get_balance, recent_transactions, block_card, branch_hours], system_prompt=SYSTEM)
    history = []

    def ask(q: str) -> str:
        history.append({"role": "user", "content": q})
        out = agent.invoke({"messages": history})
        history[:] = out["messages"]
        return out["messages"][-1].content

    if "--chat" in sys.argv:
        print("Type 'exit' to quit.")
        while (q := input("\nYou: ").strip()).lower() not in {"exit", "quit"}:
            print(f"Bot: {ask(q)}")
        return
    for q in ["What's my total balance?", "Show my last 3 transactions",
              "I lost my debit card ending 4821, please block it", "What time does the Leeds branch open on Saturday?"]:
        section(f"You: {q}", f"Bot: {ask(q)}")


if __name__ == "__main__":
    main()
