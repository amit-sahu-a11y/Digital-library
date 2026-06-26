from fastapi import APIRouter, UploadFile, File
import os

from app.services.document_processor import DocumentProcessor

router = APIRouter()

UPLOAD_DIR = "app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    # Validate file
    if not file.filename.lower().endswith(".pdf"):
        return {
            "success": False,
            "message": "Only PDF files are allowed."
        }

    # Save uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Process document
    processor = DocumentProcessor()

    result = processor.process_document(
        file_path=file_path,
        file_name=file.filename
    )

    return result