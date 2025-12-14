"""
summarizer.py

Core of application logic

Business value

Pure Python summarization logic.
No web code. No HTTP. Easy to test and reuse.
"""

import re
from collections import Counter


def summarize_text(text: str, max_sentences: int = 5) -> str:
    """
    Summarize text using sentence scoring.

    Args:
        text: Full document text
        max_sentences: Number of sentences to return

    Returns:
        A summarized string
    """

    # Clean whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Split into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)

    if len(sentences) <= max_sentences:
        return text

    # Tokenize words
    words = re.findall(r'\w+', text.lower())
    word_freq = Counter(words)

    # Score sentences
    def score(sentence):
        return sum(word_freq.get(word.lower(), 0) for word in re.findall(r'\w+', sentence))

    ranked = sorted(sentences, key=score, reverse=True)

    # Select top sentences and preserve original order
    selected = set(ranked[:max_sentences])
    summary = [s for s in sentences if s in selected]

    return " ".join(summary)
