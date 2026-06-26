from app.services.pdf_service import extract_pdf_pages
from app.chunking.chunk_service import create_chunks
from app.embeddings.embedding_service import generate_embeddings
from app.vectorstore.chroma_service import store_chunks


class DocumentProcessor:

    def process_document(self, file_path, file_name):

        pages = extract_pdf_pages(file_path)

        all_chunks = []
        chunk_id = 1
        total_characters = 0

        for page in pages:

            page_number = page["page"]
            page_text = page["text"]

            total_characters += len(page_text)

            chunks = create_chunks(page_text)

            for chunk in chunks:

                all_chunks.append({

                    "book_id": 1,

                    "book_name": file_name,

                    "page_number": page_number,

                    "chunk_id": chunk_id,

                    "chunk_index": chunk_id,

                    "char_count": len(chunk),

                    "word_count": len(chunk.split()),

                    "chunk_text": chunk

                })

                chunk_id += 1

        texts = [chunk["chunk_text"] for chunk in all_chunks]

        embeddings = generate_embeddings(texts)

        store_chunks(all_chunks, embeddings)

        return {

            "success": True,

            "filename": file_name,

            "total_pages": len(pages),

            "total_characters": total_characters,

            "total_chunks": len(all_chunks),

            "preview_chunks": all_chunks[:5],

            "status": "Stored successfully in ChromaDB"
        }