# Summary function. Acts as large language model, (LLM) statistical sentence produce.
# While reading text allow for a counter to determine frequencies of words and reproduce a condensed output of two sentences for result.
import re
from collections import Counter

# Definition of what is a summary of text.
def summarize_text(text):
    # Andy Block. F| /V [) `/
    # Split text with periods to form sentences. 
    # Integrates keywords into sentences string.
   
    # Make sure text is split into sentences.
    sentences = [s.strip() for s in re.split(r'(?<=[.!?]) +', text) if s.strip()]
    if not sentences:
        return "Give me content with a period."
    
    # Calculate word frequencies.
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)

    # Pass keywords, do not include in product.
    stopwords = {
        "the","and","of","in","to","a","is","for","on","with","as",
        "by","an","at","that","this","it","from","be","are"
    }
    # Find the keywords.
    keywords = [w for w, _ in word_counts.most_common(50) if w not in stopwords]

    if not keywords:
        keywords = list(word_counts.keys())[:10]
        
    # Define the weight of a sentence.
    def sentence_score(sentence):
        s_words = re.findall(r'\b\w+\b', sentence.lower())
        return sum(word_counts.get(w,0) for w in s_words if w in keywords)
    # Rank regarding keyword frequency.
    ranked_sentences = sorted(sentences, key=sentence_score, reverse=True)

    # Identify top two sentences regarding statistics. Consolidate.
    top_sentences = ranked_sentences[:2]
    summary_text = " ".join(top_sentences).strip()

    # Make sure sentences end with a period.

    if not summary_text.endswith((".", "!", "?")):
        summary_text += "."
    # Make sure code can process spacing with paragraph structure.
    summary_text = re.sub(r'\s+', ' ', summary_text)


    # Produce summary for at most two sentences with full words.
    ##summary_sentences = summary_text.split(".")
    ##summary_sentences = [s.strip() for s in summary_sentences if s.strip()]
    ##summary_text = ". ".join(summary_sentences[:2]) + "."
    
    # Account for paragraphs in spacing.
    summary_text = summary_text.replace("  ", " ")
   
    # Integrate missing keyword concepts in readable English.
    first_five_keywords = keywords[:5]
    missing = [k for k in first_five_keywords if k not in summary_text.lower()]

    if missing:
        summary_text += " Key concepts include: " + ", ".join(missing) + "."
        # Create natural-language list.
        if len(missing) == 1:
            summary_text = f" Key concept emphasized: {missing[0]}."
        else:
            summary_text += (
                " Key concepts emphasized: " +
                ", ".join(missing[:-1]) +
                f", and {missing[-1]}."
            )
            
    return summary_text
