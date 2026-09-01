<div align="center">

# 🧠 RAG Knowledge Assistant

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat&logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Deployed-Cloudflare%20Pages-F38020?style=flat&logo=cloudflare&logoColor=white)

*Retrieval-Augmented Generation system for intelligent document Q&A*

</div>

---

## ✨ Features

- Document ingestion and chunking
- Vector embeddings with transformer models
- Semantic similarity search
- Context-aware response generation
- RESTful API with OpenAPI docs
- Support for multiple document formats
- Scalable vector storage
- Real-time query processing

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat&logo=fastapi&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.4-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat&logo=postgresql&logoColor=white)

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/Raphasha27/python-rag-knowledge-assistant.git
cd python-rag-knowledge-assistant

# Install dependencies
pip install -e .

# Run API server
uvicorn src.main:app --reload
```

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/ingest` | Upload documents |
| `POST` | `/query` | Query knowledge base |
| `GET` | `/health` | Health check |
| `GET` | `/documents` | List documents |

## 🏗️ Architecture

```
Documents → Chunking → Embeddings → Vector Store
                                         │
User Query → Embedding → Similarity Search │
                                         │
                              Context + Query → LLM → Response
```

## 🌐 Live Demo

| Platform | URL |
|----------|-----|
| GitHub Pages | [raphasha27.github.io/python-rag-knowledge-assistant](https://raphasha27.github.io/python-rag-knowledge-assistant) |
| Docker Hub | [hub.docker.com/r/raphasha27/python-rag-knowledge-assistant](https://hub.docker.com/r/raphasha27/python-rag-knowledge-assistant) |
| Cloudflare Pages | [rag-knowledge-assistant.pages.dev](https://rag-knowledge-assistant.pages.dev) |

## 👤 Author

**raphasha27** — [GitHub](https://github.com/raphasha27)
