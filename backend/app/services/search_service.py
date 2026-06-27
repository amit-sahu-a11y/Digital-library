from app.embeddings.embedding_service import generate_query_embedding
from app.vectorstore.chroma_service import search_chunks


class SearchService:

    def search(self, query):

        embedding = generate_query_embedding(query)

        results = search_chunks(embedding)

        return results