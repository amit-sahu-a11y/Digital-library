from fastapi import APIRouter, UploadFile, File
import os

from app.services.pdf_service import extract_pdf_pages
# from app.chunking.chunk_service import chunk_text
from app.chunking.chunk_service import create_chunks

router = APIRouter()

UPLOAD_DIR = "app/uploads"

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        return {
            "success": False,
            "message": "Only PDF files are allowed."
        }
    
    """
    Upload a PDF, extract pages, create chunks,
    and return chunk metadata.
    """

    # Save uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Extract page-wise text
    pages = extract_pdf_pages(file_path)

    all_chunks = []
    chunk_id = 1
    total_characters = 0

    # Create chunks for every page
    for page in pages:

        page_number = page["page"]
        page_text = page["text"]

        total_characters += len(page_text)

        chunks = create_chunks(page_text)

        for chunk in chunks:
            all_chunks.append({
                "book_id": 1,

                "book_name": file.filename,

                "page_number": page_number,

                "chunk_id": chunk_id,

                "chunk_index": chunk_id,

                "char_count": len(chunk),
                "word_count": len(chunk.split()),

                "chunk_text": chunk

            })

            chunk_id += 1

    return {
        "success": True,

        "filename": file.filename,

        "total_pages": len(pages),

        "total_characters": total_characters,

        "total_chunks": len(all_chunks),

        "preview_chunks": all_chunks[:5]
    }
    