from assistant.config import load_faq


def answer_faq(question: str) -> dict:
    """Match a caller's question against the FAQ by keyword."""
    text = question.lower()
    best, best_hits = None, 0
    for entry in load_faq():
        hits = sum(1 for kw in entry["keywords"] if kw in text)
        if hits > best_hits:
            best, best_hits = entry, hits
    if best is None:
        return {"found": False, "answer": None, "source": "faq"}
    return {
        "found": True,
        "answer": best["answer"],
        "matched_question": best["question"],
        "source": "faq",
    }
