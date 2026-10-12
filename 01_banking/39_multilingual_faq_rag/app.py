"""Multilingual Banking FAQ (RAG) — LangChain + Ollama.

Run:  python 01_banking/39_multilingual_faq_rag/app.py
      python 01_banking/39_multilingual_faq_rag/app.py "¿Cuál es el límite diario de retiro en cajero?"
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from common import SimpleRetriever, banner, run_chain, section

FAQ = [
    "Daily ATM withdrawal limit: 1,000 on Classic debit cards and 2,500 on Platinum debit cards.",
    "International transfers (SWIFT) cost 15 per transfer and arrive in 1-3 working days. Cut-off time is 3 pm.",
    "To reset your mobile banking PIN: open the app, tap 'Forgot PIN', verify with your debit card and OTP.",
    "Savings account interest is 3.5% per year, calculated daily and paid quarterly.",
    "Minimum average monthly balance for a regular savings account is 1,000; a fee of 10 applies if not maintained.",
    "Fixed deposits can be broken early with a 1% penalty on the applicable interest rate.",
    "Lost or stolen cards can be blocked 24/7 in the app under Cards > Block, or by calling 0800 123 456.",
    "Home loan pre-approval needs ID proof, last 3 payslips, 6 months bank statements and the property details.",
]

SYSTEM = (
    "You are a multilingual bank assistant. Detect the language of the question and answer ONLY in that language, "
    "using ONLY the FAQ context. If the context doesn't contain the answer, say so politely in that language and "
    "suggest calling 0800 123 456. Keep answers under 80 words."
)


def main():
    banner("39 - Multilingual Banking FAQ (LangChain RAG)")
    retriever = SimpleRetriever(FAQ)
    questions = sys.argv[1:] or [
        "ATM se ek din mein kitna paisa nikaal sakte hain?",           # Hinglish
        "¿Cuánto cuesta una transferencia internacional?",            # Spanish
        "Comment réinitialiser mon code PIN de l'application ?",       # French
        "मेरा कार्ड खो गया है, क्या करूं?",                                 # Hindi
    ]
    for q in questions:
        # Translate to English for retrieval: the FAQ is English and the keyword fallback is English-only
        english_q = run_chain("Translate the user's text to English. Output only the translation.", "{q}", q=q)
        ctx = "\n".join(retriever.search(english_q, k=3))
        section(f"Q: {q}", run_chain(SYSTEM, "FAQ context:\n{ctx}\n\nQuestion: {q}", ctx=ctx, q=q))


if __name__ == "__main__":
    main()
