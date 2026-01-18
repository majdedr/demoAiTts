import chromadb
from app.services.vector_store.embeddings import embed_text


class VectorStore:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(
            name="knowledge_base"
        )

    def add_documents(self, docs: list[str]):
        embeddings = [embed_text(doc) for doc in docs]
        ids = [str(i) for i in range(len(docs))]

        self.collection.add(
            documents=docs,
            embeddings=embeddings,
            ids=ids
        )

    def search(self, query: str, k: int = 3) -> str:
        query_embedding = embed_text(query)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )

        documents = results.get("documents", [[]])[0]
        return "\n".join(documents)
