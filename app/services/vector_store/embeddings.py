from sentence_transformers import SentenceTransformer

# Small & fast embedding model
_model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_text(text: str) -> list[float]:
    embedding = _model.encode(text)
    return embedding.tolist()
