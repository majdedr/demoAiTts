from pathlib import Path
from app.services.vector_store.store import VectorStore

vector_store = VectorStore()


def load_knowledge():
    base_path = Path("app/data/knowledge_base")

    documents = []
    for file in base_path.glob("*.txt"):
        documents.append(file.read_text(encoding="utf-8"))

    if documents:
        vector_store.add_documents(documents)
    print(f"Loaded {len(documents)} documents into vector store")
