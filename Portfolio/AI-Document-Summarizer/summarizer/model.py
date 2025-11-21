# Summary function. Acts as machine learning, (ML), large language model, (LLM).
# Definition.
def summarize_text(text):
    # Andy Block. F| /V [) `/
    # Split text with periods to form sentences.
    sentences = text.split('.')
    # Ready to read format. 
    sentences = [s.strip() for s in sentences if s.strip()]
  
    if not sentences:
      return "Give me content with a period."
      
    return '. '.join(sentences) + "."
  
