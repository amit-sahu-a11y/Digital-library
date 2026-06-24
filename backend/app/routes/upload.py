from fastapi import APIRouter, UploadFile, File
import os

from app.services.pdf_service import extract_pdf_info

router = APIRouter()

UPLOAD_DIR = "app/uploads"

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(await file.read())

    pdf_info = extract_pdf_info(file_path)

    return {
        "success": True,
        "filename": file.filename,
        "pages": pdf_info["pages"],
        "characters": pdf_info["characters"]
    }