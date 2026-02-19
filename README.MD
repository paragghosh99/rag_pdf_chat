# 📚 RAG PDF Chat

Minimal Retrieval-Augmented Generation (RAG) application for querying PDFs using a local LLM and vector search.

---

## 🚀 Features

- PDF ingestion & chunking  
- HuggingFace embeddings (all-MiniLM-L6-v2)  
- Chroma persistent vector database  
- Similarity-based retrieval (Top-K)  
- FLAN-T5 local LLM generation  
- Strict grounded QA prompt (hallucination control)  
- FastAPI backend  
- Simple HTML frontend  
- Pytest-ready  

---

## 🏗 Architecture

Pipeline:

PDF → Chunk → Embed → Store → Retrieve → Prompt → Generate → Answer

Core Modules:

- `main.py` – API layer  
- `ingestion.py` – PDF processing  
- `vector_store.py` – Chroma + embeddings  
- `rag.py` – Retrieval orchestration  
- `llm.py` – FLAN-T5 generation  
- `prompts.py` – QA prompt control  
- `config.py` – Model & chunk configuration  

---

## 📦 Tech Stack

Backend:
- FastAPI  
- LangChain  
- ChromaDB  
- HuggingFace Transformers  
- Sentence Transformers  
- PyTorch  

Frontend:
- HTML + JavaScript  

Testing:
- Pytest  

---

## ⚙ Configuration

Defined in `config.py`:

- `MODEL_NAME`
- `CHUNK_SIZE`
- `CHUNK_OVERLAP`
- `TOP_K`
- `PERSIST_DIR`

Default model:
google/flan-t5-small


---

## 📂 Project Structure

.
├── main.py
├── ingestion.py
├── rag.py
├── vector_store.py
├── llm.py
├── prompts.py
├── schemas.py
├── config.py
├── helper/
│ └── clean_text.py
├── index.html
├── requirements.txt
├── vector_db/
├── uploaded_pdfs/
├── retrieved_chunks.txt
└── tests/


---

## 🧪 Testing

Run:
pytest -v


---

## 🔎 Notes

- Re-ingestion resets vector collection  
- Retrieved chunks logged to `retrieved_chunks.txt`  
- CORS currently open (`*`)  
- Fully local LLM (no external API required)  

---

## 🎯 Purpose

A clean, modular RAG architecture suitable for:

- Local experimentation  
- LLM backend abstraction  
- CI/CD integration  
- Future cloud deployment  