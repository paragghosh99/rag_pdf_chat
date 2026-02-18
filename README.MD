# 📚 RAG PDF Chat Application

A full-stack Retrieval-Augmented Generation (RAG) application that allows users to:

1. Upload a PDF
2. Convert it into embeddings
3. Store embeddings in a persistent vector database
4. Ask questions about the document
5. Get AI-generated answers grounded strictly in the document context

---

# 🚀 Features

- PDF ingestion and chunking
- Embedding generation using Sentence Transformers
- Persistent vector storage with ChromaDB
- Context retrieval using similarity search
- LLM answer generation using FLAN-T5
- FastAPI backend
- Simple HTML frontend
- Unit tests with Pytest
- CI-ready structure

---

# 🏗 Architecture Overview

This project follows a clean modular RAG pipeline:

PDF → Chunking → Embeddings → Vector Store → Retrieval → Prompt → LLM → Answer

Core components:

- **Ingestion Layer** → `ingestion.py`
- **Vector Store** → `vector_store.py`
- **LLM Generation** → `llm.py`
- **RAG Pipeline** → `rag.py`
- **API Layer** → `main.py`
- **Frontend UI** → `index.html`

---

# 📦 Tech Stack

Backend:
- FastAPI
- LangChain
- ChromaDB
- HuggingFace Transformers
- Sentence Transformers
- PyTorch

Frontend:
- Simple HTML + JS

Testing:
- Pytest

Dependencies are listed in:
requirements.txt


---

# 🛠 Local Setup Guide

## 1️⃣ Clone the Repository


git clone <your-repo-url>
cd <repo-name>
Create Virtual Environment
Windows:
python -m venv venv
venv\Scripts\activate
Mac/Linux:
python3 -m venv venv
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Dependencies defined in:

requirements.txt
Environment Variables (Optional)
The project loads environment variables via:

config.py
Currently using local FLAN-T5 model:

MODEL_NAME = "google/flan-t5-base"
No OpenAI key required.

▶️ Running the Application
Start FastAPI Server
uvicorn main:app --reload
You should see:

Uvicorn running on http://127.0.0.1:8000
Open Frontend
Open:

index.html
in your browser.

📄 How to Use the App
Step 1: Upload PDF
Select a PDF file

Click "Ingest PDF"

System:

Splits document into chunks

Creates embeddings

Stores in persistent Chroma DB (vector_db/)

Ingestion logic:

ingestion.py
Step 2: Ask Question
Type a question

Click Ask

System:

Retrieves top-K chunks

Formats prompt

Sends to FLAN-T5

Returns grounded answer

Retrieval logic:

rag.py
Prompt template:

prompts.py
LLM generation:

llm.py
🧠 How the RAG Pipeline Works
Vector Store
vector_store.py
Uses:

HuggingFace embeddings (all-MiniLM-L6-v2)

Chroma persistent storage

Directory: vector_db/

Retrieval
In rag.py:

Uses similarity search

TOP_K = 3

Writes retrieved chunks to:

retrieved_chunks.txt
(useful for debugging)

Prompt Control
Defined in:

prompts.py
Strictly instructs model to:

Use only provided context

Refuse if answer not found

Prevents hallucination.

📂 Project Structure
.
├── main.py                 # FastAPI app
├── ingestion.py            # PDF ingestion logic
├── rag.py                  # RAG pipeline
├── vector_store.py         # ChromaDB setup
├── llm.py                  # FLAN-T5 generation
├── prompts.py              # Prompt template
├── schemas.py              # Pydantic models
├── config.py               # Config constants
├── helper/
│   └── clean_text.py
├── index.html              # Frontend UI
├── requirements.txt
├── vector_db/              # Persistent embeddings
├── uploaded_pdfs/          # Stored PDFs
├── retrieved_chunks.txt    # Debug retrieval
└── test_basic.py           # Unit tests
🧪 Running Tests
Run:

pytest -v
Tests located in:

test_basic.py
🔁 Re-Ingesting a New PDF
Each ingestion:

Deletes existing collection

Recreates vector store

Indexes new PDF

Handled inside:

ingestion.py
⚙ Configuration Options
Modify in config.py:

Setting	Description
MODEL_NAME	LLM model
CHUNK_SIZE	Text split size
CHUNK_OVERLAP	Overlap size
TOP_K	Number of retrieved chunks
PERSIST_DIR	Vector DB directory
🚧 Performance Notes
First model load may take ~30–60 seconds

Embeddings are computed once per ingestion

Retrieval is fast after indexing

Uses CPU (faiss-cpu + torch)

🧯 Troubleshooting
1️⃣ Slow first response?
Model warm-up. Normal.

2️⃣ Hallucination?
Check:

retrieved_chunks.txt
Confirm relevant chunks are retrieved.

3️⃣ Chroma errors?
Delete:

vector_db/
and re-ingest.

🧪 Example Test PDF
You can test using:

Simple_RAG_Test_Document.pdf
🔐 Security Notes
CORS is currently set to allow all origins.

Not production hardened.

No authentication.

📈 Future Improvements
Streaming responses

MMR retrieval

Better chunking strategies

UI improvements

Dockerization

Deployment pipeline

GPU inference

📜 License
For learning and experimentation purposes.

👨‍💻 Author
Built as a modular, production-style RAG system.

🧠 Learning Objective
This project demonstrates:

End-to-end RAG architecture

Embedding + Retrieval systems

Prompt engineering

FastAPI backend design

CI + testing structure

Local LLM deployment

⭐ If You Found This Useful
Consider starring the repo.