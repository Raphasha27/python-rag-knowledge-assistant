# RAG Knowledge Assistant

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat&logo=fastapi&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.4-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat&logo=postgresql&logoColor=white)

> Retrieval-Augmented Generation system for intelligent document Q&A

## Architecture

```
Documents → Chunking → Embeddings → Vector Store
                                         │
User Query → Embedding → Similarity Search │
                                         │
                              Context + Query → LLM → Response
```

## Quick Start

```bash
git clone https://github.com/Raphasha27/python-rag-knowledge-assistant.git
cd python-rag-knowledge-assistant
pip install -e .
uvicorn src.main:app --reload
```

## License

MIT License

## Live Demo

| Platform | URL |
|----------|-----|
| GitHub Pages | [https://raphasha27.github.io/python-rag-knowledge-assistant](https://raphasha27.github.io/python-rag-knowledge-assistant) |
| Docker Hub | [docker pull raphasha27/python-rag-knowledge-assistant](https://hub.docker.com/r/raphasha27/python-rag-knowledge-assistant) |
| Cloudflare Pages | [https://rag-knowledge-assistant.pages.dev](https://rag-knowledge-assistant.pages.dev) |

