from pydantic import BaseModel

class SummarizeResponse(BaseModel):
    summary: str
    sentence_count: int
