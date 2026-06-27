from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(texts):
    """
    Generate vector embeddings for a list of text chunks.
    """
    return model.encode(texts).tolist()

def generate_query_embedding(query):
    """
    Generate embedding for a user's search query.
    """
    embedding = model.encode(query)
    return embedding.tolist()