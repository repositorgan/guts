# Summary function. Acts as large language model, (LLM) statistical sentence produce.
# While reading text allow for a counter to determine frequencies of words and reproduce a condensed output of two sentences for result.
import re
from collections import Counter

def summarize_text(text):
    """
    Lightweight extractive summarizer:
    - Extracts sentences
    - Computes keyword frequency
    - Selects best 1–2 sentences
    - Produces a clean, grammatical summary
    """

    # --- 1. Split text into sentences ---
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]

    if not sentences:
        return "No usable sentences found in the text."

    # --- 2. Count word frequencies ---
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)

    stopwords = {
        "the", "and", "of", "in", "to", "a", "is", "for", "on", "with",
        "as", "by", "an", "at", "that", "this", "it", "from", "be", "are"
    }

    keywords = [w for w, _ in word_counts.most_common(20) if w not in stopwords]

    if not keywords:
        keywords = list(word_counts.keys())[:10]

    # --- 3. Score each sentence ---
    def sentence_score(sentence):
        s_words = re.findall(r'\b\w+\b', sentence.lower())
        return sum(word_counts.get(w, 0) for w in s_words if w in keywords)

    ranked = sorted(sentences, key=sentence_score, reverse=True)

    # --- 4. Take top 1–2 sentences ---
    best_sentences = ranked[:2]
    summary = " ".join(best_sentences)

    # --- 5. Fix spacing, ensure full sentences ---
    summary = summary.replace("  ", " ").strip()
    if not summary.endswith((".", "!", "?")):
        summary += "."

    # --- 6. Include missing core keywords in English form ---
    top_keywords = keywords[:5]
    missing = [k for k in top_keywords if k not in summary.lower()]

    if missing:
        if len(missing) == 1:
            summary += f" Key concept emphasized: {missing[0]}."
        else:
            summary += (
                " Key concepts emphasized: "
                + ", ".join(missing[:-1])
                + f", and {missing[-1]}."
            )

    return summary

