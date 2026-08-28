"""Embedding generation module"""
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import Optional


class EmbeddingGenerator:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
    
    def generate(self, texts: list[str]) -> np.ndarray:
        return self.model.encode(texts, show_progress_bar=True)
    
    def generate_single(self, text: str) -> np.ndarray:
        return self.model.encode([text])[0]
