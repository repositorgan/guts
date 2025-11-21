# Summary function. Acts as machine learning, (ML), large language model, (LLM).
# While reading text allow for a counter to determine frequencies of words and reproduce a condensed output for result.
import re
from collections import Counter

# Definition of what is a summary of text.
def summarize_text(text):
    # Andy Block. F| /V [) `/
    # Split text with periods to form sentences. 
    # Integrates keywords into sentences string.
   
    # 1) Make sure text is split into sentences.
    sentences = [s.strip() for s in re.split(r'(?<=[.!?]) +', text) if s.strip()]
    if not sentences:
        return "Give me content with a period."
    
    # 2) Calculate word frequencies.
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)

    # Pass keywords, do not include in product.
    stopwords = {
        "the","and","of","in","to","a","is","for","on","with","as",
        "by","an","at","that","this","it","from","be","are"
    }
    # Find the keywords.
    keywords = [w for w, _ in words_counts.most_common(15) if w not in stopwords]
    # Define the weight of a sentence.
    def sentence_score(sentence):
        s_words = re.findall(r'\b\w+\b', sentence.lower())
        return sum(word_counts.get(w,0) for w in s_words if w in keywords)
    # Rank regarding keyword frequency.
    ranked_sentences = sorted(sentences, key=sentence_score, reverse=True)

    # 4) Identify top two sentences. Consolidate.
    summary_sentences = ranked_sentences[:2]
    summary_text = " ".join(summary_sentences)

    # 5) Cap result output to 20 characters, or near 1% of full text.
    total_chars = len(text)
    max_chars = max(20, int(total_chars * 0.01))
    summary_text = summary_text[:max_chars].rstrip()
    if not summary_text.endswith((".", "!", "?")):
        summary_text += "."

    # 6) Integrate keywords into summary.
    keywords_in_summary = [k for k in keywords if k in summary_text.lower()]
    missing_keywords = [k for k in keywords[:5] if k not in keywords_in_summary]
    if missing_keywords:
        summary_text += " Key concepts include: " + ", ".join(missing_keywords) + "."

    return summary_text
