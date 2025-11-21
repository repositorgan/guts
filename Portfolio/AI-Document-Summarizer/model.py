# Summary function. Acts as machine learning, (ML), large language model, (LLM).
# Definition.
def summarize_text(text: str) -> str:
  # Andy Block
  sentences = text.split('.')
  return '. '.join(sentences[:2]) + '.'
  
    # Member access operator to grammar.
    sentences = text.split(".")
    return sentences[0].strip() + "."
