from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(texts):
    """
    Generate vector embeddings for a list of text chunks.
    """
    return model.encode(texts).tolist()