---
layout: default
title: RAG PDF Chat — A Journey From Document to Answer
hero_title: RAG PDF Chat
hero_subtitle: From PDF Upload to Grounded LLM Responses
hero_meta: Built with FastAPI · Chroma · HuggingFace · Docker
hero_image: "/rag_pdf_chat/assets/hero.png"
---

# RAG PDF Chat — A Journey From Document to Answer

This page walks you through  
**what it is**, **why it matters**, and **how it actually works** — end to end.

---

## What Problem Are We Solving?

Most LLM demos stop at “here’s a chatbot.”

Real AI systems must also:

1. Ground answers in real documents  
2. Prevent hallucination  
3. Reset state safely between uploads  
4. Retrieve only relevant context  
5. Run consistently inside containers  

That’s what this project focuses on.

---

## Table of Contents

1. [High-Level Architecture](#high-level-architecture)
2. [PDF Ingestion Flow](#pdf-ingestion-flow)
3. [Retrieval & Prompt Construction](#retrieval--prompt-construction)
4. [APIs You Can Call](#apis-you-can-call)
5. [Building & Running Locally](#building--running-locally)
6. [Docker: One Image, Many Environments](#docker-one-image-many-environments)
7. [Model & Vector Store Design](#model--vector-store-design)
8. [Lessons Learned & Next Steps](#lessons-learned--next-steps)

---

## High-Level Architecture

At its core, the RAG PDF Chat system has three pillars:

- **HTTP API** — FastAPI handles ingestion and question requests  
- **Retrieval Layer** — Chroma vector database stores and searches embeddings  
- **Generation Layer** — Flan-T5 produces answers grounded in retrieved context  

**Request lifecycle:**

User → `/ask` → Vector Search → Context Injection → LLM → JSON response

## PDF Ingestion Flow

Ingestion prepares the document for semantic search.

### Upload

- Client uploads a PDF via `POST /ingest`
- The file is stored temporarily on the server

### Chunking

- The PDF is loaded using `PyPDFLoader`
- Text is split using `RecursiveCharacterTextSplitter`
- Chunk size and overlap are configurable

### Embedding

- Each chunk is converted into a vector representation
- Model used: `sentence-transformers/all-MiniLM-L6-v2`

### Storage

- Chunks and embeddings are stored in Chroma
- The collection is reset before each new upload to prevent memory bleed

## Retrieval & Prompt Construction

Answer generation is strictly grounded in retrieved document context.

### Retrieval

- Client sends a question to `POST /ask`
- A similarity search is performed in Chroma
- Top K relevant chunks are retrieved (`TOP_K = 3`)

Only the most semantically similar chunks are selected.

### Context Injection

- Retrieved chunks are cleaned and concatenated
- They are injected into a structured prompt template
- The model is instructed to use ONLY the provided context

If the answer is not explicitly present, it must respond:

"Answer not found in the document."

### Generation

- Prompt is passed to `google/flan-t5-small`
- The model generates a 2–4 sentence grounded response
- The answer is returned as JSON

## APIs You Can Call

### Ingestion

- `POST /ingest` — Upload and process a new PDF  

  - Deletes existing vector collection  
  - Splits document into chunks  
  - Generates embeddings  
  - Stores them in Chroma  

### Question Answering

- `POST /ask` — Ask a question about the uploaded document  

  - Performs similarity search  
  - Injects retrieved chunks into prompt  
  - Generates grounded response  
  - Returns JSON answer  

## Building & Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```
Start the server:

uvicorn app.main:app --reload
Visit:

API Docs → http://localhost:8000/docs

Main UI → http://localhost:8000

## Docker: One Image, Many Environments

Docker guarantees identical behavior across environments.

Build the image:

```bash
docker build -t rag-pdf .
```
Run the container:

```bash
docker run -p 8000:8000 rag-pdf
```

Same image locally.
Same image in production.
No “works on my machine” surprises.

## Model & Vector Store Design

This system is intentionally designed to run without paid APIs.

### Embedding Model

- `sentence-transformers/all-MiniLM-L6-v2`
- Lightweight and fast
- Produces 384-dimensional embeddings
- Optimized for semantic similarity search

### Language Model

- `google/flan-t5-small`
- Runs locally via HuggingFace Transformers
- Deterministic and Docker-friendly
- Generates concise, grounded responses

### Vector Store

- Chroma with local persistence
- Collection reset on each new ingestion
- Prevents cross-document contamination

This architecture keeps the system:

- Fully local  
- Cost-free  
- Reproducible  
- Easy to containerize

## Lessons Learned & Next Steps

### What This Project Teaches

- Retrieval is more important than model size  
- LLMs must be constrained to prevent hallucination  
- Vector stores require careful state management  
- Local models simplify deployment and cost control  
- Deterministic Docker builds reduce environment drift  

### Next Improvements

- Add streaming responses for real-time answer generation  
- Introduce larger open-source LLM (GPU-backed)  
- Add metadata filtering per document  
- Support multiple document collections  
- Add authentication layer for multi-user support

---

_Made with ❤️ by Parag · Hosted on GitHub Pages_