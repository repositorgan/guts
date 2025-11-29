"""
Extractive summarizer for producing 1–2 sentence executive summaries.
"""

import re
from collections import Counter

def summarize_text(text: str) -> str:
    # 1. Break into sentences.
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    if not sentences:
        return "No valid sentences found."

    # 2. Count word frequencies for scoring.
    words = re.findall(r'\b\w+\b', text.lower())
    counts = Counter(words)

    # Common stopwords that should not count as keywords.
    stopwords = {
        "the", "and", "of", "in", "to", "a", "is", "for", "on", "with", "as",
        "by", "an", "at", "that", "this", "it", "from", "be", "are", "was",
        "were", "but", "or", "has", "have", "so", "its", "been", "over", "about", 
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "I",
    }

    # 3. Extract high-frequency keywords.
    keywords = [w for w, _ in counts.most_common(20) if w not in stopwords][:15]
    if not keywords:
        keywords = list(counts.keys())[:10]

    # 4. Score sentences by keyword density, not length.
    def score(sentence):
        s_words = re.findall(r'\b\w+\b', sentence.lower())
        if not s_words:
            return 0
        raw_score = sum(counts.get(w, 0) for w in s_words if w in keywords)
        return raw_score / len(s_words)

    # 5. Rank sentences using the score function.
    ranked = sorted(sentences, key=score, reverse=True)

    # 6. Pick the top 2 meaningful sentences.
    best = ranked[:2]
    summary = " ".join(best).strip()

    # Clean spacing.
    summary = re.sub(r'\s+', " ", summary)
    if not summary.endswith((".", "!", "?")):
        summary += "."

    # 7. Add missing key concepts (optional).
    top5 = keywords[:5]
    missing = [k for k in top5 if k not in summary.lower()]

    if missing:
        if len(missing) == 1:
            summary += f" Most commonly used text: {missing[0]}."
        else:
            summary += (
                " Key concepts emphasized: "
                + ", ".join(missing[:-1])
                + f", and {missing[-1]}."
            )

    return summary
