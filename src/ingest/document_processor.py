"""Document processor for ingesting various file types"""
from pathlib import Path
from typing import Optional
import hashlib


class DocumentProcessor:
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    
    def process_file(self, file_path: str) -> list[dict]:
        path = Path(file_path)
        if path.suffix == ".pdf":
            return self._process_pdf(path)
        elif path.suffix == ".txt":
            return self._process_text(path)
        else:
            raise ValueError(f"Unsupported file type: {path.suffix}")
    
    def _process_pdf(self, path: Path) -> list[dict]:
        from pypdf import PdfReader
        
        reader = PdfReader(str(path))
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        
        return self._chunk_text(text, str(path))
    
    def _process_text(self, path: Path) -> list[dict]:
        text = path.read_text(encoding="utf-8")
        return self._chunk_text(text, str(path))
    
    def _chunk_text(self, text: str, source: str) -> list[dict]:
        chunks = []
        for i in range(0, len(text), self.chunk_size - self.chunk_overlap):
            chunk = text[i:i + self.chunk_size]
            chunk_id = hashlib.md5(chunk.encode()).hexdigest()
            chunks.append({
                "id": chunk_id,
                "content": chunk,
                "source": source,
            })
        return chunks
