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

            score = round((1 - distance) * 100, 2)

            formatted_results.append({

                "book_name": meta["book_name"],

                "document_id": meta["document_id"],

                "page_number": meta["page_number"],

                "chunk_id": meta["chunk_id"],

                "score": score,

                "text": doc

            })

        search_time = round((time.time() - start_time) * 1000, 2)

        return {

            "query": query,

            "total_results": len(formatted_results),

            "search_time_ms": search_time,

            "results": formatted_results

        }