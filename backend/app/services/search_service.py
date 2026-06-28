import time

from app.embeddings.embedding_service import generate_query_embedding
from app.vectorstore.chroma_service import search_chunks


class SearchService:

    def search(self, query, top_k=5, document_id=None):

        start_time = time.time()

        embedding = generate_query_embedding(query)

        results = search_chunks(
            embedding,
            top_k=top_k,
            document_id=document_id
        )

        formatted_results = []

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        for doc, meta, distance in zip(documents, metadatas, distances):

            # Convert distance to similarity score
            score = round((1 - distance) * 100, 2)
            score = max(0, min(100, score))

            formatted_results.append({

                "book_name": meta.get("book_name"),

                "document_id": meta.get("document_id"),

                "page_number": meta.get("page_number"),

                "chunk_id": meta.get("chunk_id"),

                "score": score,

                # Return only a preview instead of the entire chunk
                "text": doc[:350] + "..." if len(doc) > 350 else doc

            })

        search_time = round((time.time() - start_time) * 1000, 2)

        return {

            "query": query,

            "document_id": document_id,

            "total_results": len(formatted_results),

            "search_time_ms": search_time,

            "results": formatted_results

        }