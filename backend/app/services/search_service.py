import time

from app.embeddings.embedding_service import generate_query_embedding
from app.vectorstore.chroma_service import search_chunks

import time

# from app.embeddings.embedding_service import generate_query_embedding
# from app.vectorstore.chroma_service import search_chunks
from app.services.generation_service import GenerationService


generator = GenerationService()


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
        context = "\n\n".join(documents)
        generation_start = time.time()

        answer = generator.generate_answer(
        query=query,
        context=context
        )

        generation_time = round(
            (time.time() - generation_start) * 1000,
            2
            )

        for doc, meta, distance in zip(documents, metadatas, distances):

            # Convert distance to similarity score
            score = round((1 - distance) * 100, 2)
            score = max(0, min(100, score))

            formatted_results.append({

                "book_name": meta["book_name"],

                "document_id": meta["document_id"],

                "page_number": meta["page_number"],

                "score": score

            })

        search_time = round((time.time() - start_time) * 1000, 2)

        if len(formatted_results) == 0:
            return {
                "query": query,
                "answer": "I couldn't find relevant information in the uploaded documents.",
                "document_id": document_id,
                "total_results": 0,
                "search_time_ms": search_time,
                "generation_time_ms": 0,
                "sources": []
            }
        else:
            return {

                "query": query,

                "answer": answer,

                "document_id": document_id,

                "total_results": len(formatted_results),

                "search_time_ms": search_time,

                "generation_time_ms": generation_time,

                "sources": formatted_results

        }