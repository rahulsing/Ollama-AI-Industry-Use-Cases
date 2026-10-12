"""Bank Policy & Procedure Q&A (RAG) — LangChain + Ollama embeddings.

Tip: `ollama pull nomic-embed-text` for semantic retrieval (falls back to keywords).

Run:  python 01_banking/24_policy_qa_rag/app.py
      python 01_banking/24_policy_qa_rag/app.py "Do I need senior approval to onboard a PEP?"
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import SimpleRetriever, banner, run_chain, section

POLICIES = [  # (source, text) - replace with chunks from your own policy PDFs
    ("Credit Policy 4.2", "Unsecured personal loans are capped at 20x net monthly income and a maximum tenure of 60 months. "
                          "DTI including the new loan must not exceed 50%."),
    ("Credit Policy 7.1", "Any credit exception beyond policy requires approval one level above the normal sanctioning "
                          "authority and must be reported to the Credit Risk Committee monthly."),
    ("KYC Policy 3.4", "Politically Exposed Persons (PEPs) require Enhanced Due Diligence, source of wealth verification "
                       "and approval by senior management (Head of Compliance) before onboarding."),
    ("KYC Policy 5.1", "Periodic KYC review frequency: high-risk customers every 1 year, medium every 2 years, low every 3 years."),
    ("Ops Manual 2.8", "Cash transactions of 10,000 or more must be reported in the Currency Transaction Report by T+1. "
                       "Splitting transactions to avoid reporting is structuring and must be escalated to the MLRO."),
    ("Ops Manual 6.3", "Lost debit cards must be hot-listed immediately on customer request through any channel; "
                       "replacement cards are dispatched within 5 working days."),
    ("Complaints Policy 1.2", "Complaints must be acknowledged within 2 working days and resolved within 30 days. "
                              "Unresolved complaints are escalated to the Principal Nodal Officer."),
]

SYSTEM = (
    "You answer bank staff questions using ONLY the policy extracts provided. Cite the source in square brackets "
    "after each statement, e.g. [KYC Policy 3.4]. If the extracts do not contain the answer, say so and suggest "
    "who to contact. Be concise."
)


def main():
    banner("24 - Bank Policy Q&A (LangChain RAG)")
    retriever = SimpleRetriever([f"[{s}] {t}" for s, t in POLICIES])
    questions = sys.argv[1:] or [
        "Do I need senior approval to onboard a PEP, and how often must we review them?",
        "A customer deposited 9,900 cash three days in a row. What should I do?",
        "What is the maximum personal loan for someone earning 4,000 net per month?",
    ]
    for q in questions:
        context = "\n".join(retriever.search(q, k=4))
        section(f"Q: {q}", run_chain(SYSTEM, "Policy extracts:\n{context}\n\nQuestion: {q}", context=context, q=q))


if __name__ == "__main__":
    main()
