"""Document retrieval module"""
from .embeddings import EmbeddingGenerator
from .vectorstore import VectorStore


class Retriever:
    def __init__(self):
        self.embedding_generator = EmbeddingGenerator()
        self.vector_store = VectorStore()
    
    def retrieve(self, query: str, top_k: int = 5) -> list[dict]:
        query_embedding = self.embedding_generator.generate_single(query)
        results = self.vector_store.query(query_embedding.tolist(), top_k)
        
        retrieved = []
        for i, doc in enumerate(results["documents"][0]):
            retrieved.append({
                "content": doc,
                "score": results["distances"][0][i] if "distances" in results else 0.0,
            })
        
        return retrieved
