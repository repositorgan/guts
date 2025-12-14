from pydantic import BaseModel

class SummarizeRequest(BaseModel):
    text: str
    max_sentences: int = 3
