from fastapi import APIRouter, UploadFile, File
from pathlib import Path
from app.services.file_loader import extract_text
from app.services.summarizer import summarize_text

router = APIRouter()

UPLOAD_DIR = Path("app/storage/uploads")
PROCESSED_DIR = Path("app/storage/processed")

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    suffix = Path(file.filename).suffix.lower()
    dest = UPLOAD_DIR / suffix.replace(".", "") / file.filename
    dest.parent.mkdir(parents=True, exist_ok=True)

    content = await file.read()
    dest.write_bytes(content)

    text = extract_text(dest)

    summary = summarize_text(text)

    summary_path = PROCESSED_DIR / "summaries" / f"{file.filename}.summary.txt"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(summary, encoding="utf-8")

    return {
        "filename": file.filename,
        "summary": summary
    }
