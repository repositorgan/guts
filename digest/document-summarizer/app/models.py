"""
models.py

Defines request/response schemas for the API.
FastAPI uses these for validation and docs.
"""

from pydantic import BaseModel, Field


class SummarizeRequest(BaseModel):
    text: str = Field(..., description="Full document text to summarize")
    max_sentences: int = Field(5, ge=1, le=20, description="Number of sentences to return")


class SummarizeResponse(BaseModel):
    summary: str
    sentence_count: int
