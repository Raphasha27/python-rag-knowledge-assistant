"""Vector store module using ChromaDB"""
import chromadb
from typing import Optional


class VectorStore:
    def __init__(self, collection_name: str = "documents"):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(collection_name)
    
    def add_documents(self, ids: list[str], documents: list[str], embeddings: list[list[float]]):
        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
        )
    
    def query(self, query_embedding: list[float], n_results: int = 5) -> dict:
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
        )
    
    def count(self) -> int:
        return self.collection.count()
