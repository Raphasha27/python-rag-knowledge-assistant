"""Response generation module"""
from typing import Optional


class Generator:
    def __init__(self, model_name: str = "gpt2"):
        self.model_name = model_name
    
    def generate(self, query: str, context: list[str]) -> str:
        context_text = "\n\n".join(context)
        return f"Based on the provided context, here is the answer to your question about: {query[:50]}..."
