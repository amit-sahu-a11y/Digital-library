import time

from app.embeddings.embedding_service import generate_query_embedding
from app.vectorstore.chroma_service import search_chunks
from app.services.generation_service import GenerationService

generator = GenerationService()


class SearchService:

    def search(self, query, top_k=5, document_id=None):

        start_time = time.time()

        # Generate query embedding
        embedding = generate_query_embedding(query)

        # Search ChromaDB
        results = search_chunks(
            embedding,
            top_k=top_k,
            document_id=document_id
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        formatted_results = []

        # Format search results
        for doc, meta, distance in zip(documents, metadatas, distances):

            score = round((1 - distance) * 100, 2)
            score = max(0, min(100, score))

            formatted_results.append({
                "book_name": meta["book_name"],
                "document_id": meta["document_id"],
                "page_number": meta["page_number"],
                "score": score,
                "text": doc
            })

        # Calculate search time
        search_time = round((time.time() - start_time) * 1000, 2)

        # ----------------------------
        # Check similarity score
        # ----------------------------
        best_score = formatted_results[0]["score"] if formatted_results else 0

        print("=" * 50)
        print("Query:", query)
        print("Best Score:", best_score)
        print("=" * 50)

        # Reject poor matches
        if best_score < 40:
            return {
                "query": query,
                "answer": "I couldn't find relevant information in the uploaded documents.",
                "document_id": document_id,
                "total_results": 0,
                "search_time_ms": search_time,
                "generation_time_ms": 0,
                "sources": []
            }

        # ----------------------------
        # Build context using only top 3 chunks
        # ----------------------------
        context = "\n\n".join(
            result["text"]
            for result in formatted_results[:3]
        )

        # ----------------------------
        # Generate answer
        # ----------------------------
        generation_start = time.time()

        answer = generator.generate_answer(
            query=query,
            context=context
        )

        generation_time = round(
            (time.time() - generation_start) * 1000,
            2
        )

        # ----------------------------
        # Prepare source references
        # ----------------------------
        sources = []

        for result in formatted_results:

            sources.append({
                "book_name": result["book_name"],
                "document_id": result["document_id"],
                "page_number": result["page_number"],
                "score": result["score"]
            })

        # ----------------------------
        # Final API Response
        # ----------------------------
        return {
            "query": query,
            "answer": answer,
            "document_id": document_id,
            "total_results": len(sources),
            "search_time_ms": search_time,
            "generation_time_ms": generation_time,
            "sources": sources
        }