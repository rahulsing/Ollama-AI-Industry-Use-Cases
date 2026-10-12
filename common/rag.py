"""Tiny dependency-free retriever for RAG use cases.

Uses Ollama embeddings (OLLAMA_EMBED_MODEL) with pure-Python cosine similarity.
If the embedding model isn't pulled, it falls back to keyword overlap so the
demo still runs. Run `ollama pull nomic-embed-text` for proper semantic search.
"""

from __future__ import annotations

import math
import re

from .llm import OLLAMA_BASE_URL, OLLAMA_EMBED_MODEL


def _tokens(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", text.lower()) if len(t) > 2}


def _cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


class SimpleRetriever:
    def __init__(self, docs: list[str]):
        self.docs = docs
        self.vectors = None
        try:
            from langchain_ollama import OllamaEmbeddings

            self.embedder = OllamaEmbeddings(model=OLLAMA_EMBED_MODEL, base_url=OLLAMA_BASE_URL)
            self.vectors = self.embedder.embed_documents(docs)
        except Exception as exc:  # model not pulled, server down, etc.
            print(f"[rag] embeddings unavailable ({exc.__class__.__name__}); using keyword retrieval")

    def search(self, query: str, k: int = 3) -> list[str]:
        if self.vectors is not None:
            qv = self.embedder.embed_query(query)
            scores = [_cosine(qv, v) for v in self.vectors]
        else:
            q = _tokens(query)
            scores = [len(q & _tokens(d)) for d in self.docs]
        ranked = sorted(range(len(self.docs)), key=lambda i: scores[i], reverse=True)
        return [self.docs[i] for i in ranked[:k]]
