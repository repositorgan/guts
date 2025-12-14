"""
main.py

FastAPI HTTP service for document summarization.
"""

from fastapi import FastAPI
from app.models import SummarizeRequest, SummarizeResponse
from app.summarizer import summarize_text

app = FastAPI(
    title="AI Document Summarizer",
    description="Legal & Educational document summarization service",
    version="1.0.0"
)


@app.get("/")
def health_check():
    """
    Health endpoint for monitoring and demos.
    """
    return {"status": "running"}


@app.post("/summarize", response_model=SummarizeResponse)
def summarize(req: SummarizeRequest):
    """
    Summarize a document.

    Use cases:
    - Legal document review
    - Contract analysis
    - Educational reading comprehension
    """

    summary = summarize_text(
        text=req.text,
        max_sentences=req.max_sentences
    )

    return SummarizeResponse(
        summary=summary,
        sentence_count=summary.count(".")
    )
