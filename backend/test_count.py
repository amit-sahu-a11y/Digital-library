from app.vectorstore.chroma_service import collection

print(collection.count())
from app.vectorstore.chroma_service import collection

print("Total Chunks:", collection.count())

from app.embeddings.embedding_service import generate_query_embedding
from app.vectorstore.chroma_service import search_raw

query = "Linear Regression"

embedding = generate_query_embedding(query)

results = search_raw(embedding)

for i, (doc, distance) in enumerate(
    zip(results["documents"][0], results["distances"][0])
):
    print("=" * 60)
    print(f"Result {i+1}")
    print(f"Distance : {distance}")
    print(doc[:500])