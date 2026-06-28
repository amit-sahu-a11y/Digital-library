import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="ebooks"
)


def store_chunks(chunks, embeddings):

    ids = []

    documents = []

    metadatas = []

    vectors = []

    for chunk, embedding in zip(chunks, embeddings):

        ids.append(str(chunk["chunk_id"]))

        documents.append(chunk["chunk_text"])

        vectors.append(embedding)

        metadatas.append({
            "document_id": chunk["document_id"],

            "book_name": chunk["book_name"],

            "page_number": chunk["page_number"],

            "chunk_id": chunk["chunk_id"],
            
            "chunk_index": chunk["chunk_index"]
        })

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=vectors,
        metadatas=metadatas
    )

def search(query_embedding, top_k=5):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results    

def search_chunks(query_embedding, top_k=5, document_id=None):

    if document_id:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where={"document_id": document_id}
        )
    else:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

    return results