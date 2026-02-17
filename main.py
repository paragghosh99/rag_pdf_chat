from fastapi import FastAPI
from schemas import IngestRequest, QuestionRequest
from ingestion import ingest_pdf
from rag import answer_question

app = FastAPI()


@app.post("/ingest")
def ingest(req: IngestRequest):
    chunks = ingest_pdf(req.pdf_path)
    return {"status": "ingested", "chunks": chunks}


@app.post("/ask")
def ask(req: QuestionRequest):
    answer = answer_question(req.question)
    return {"answer": answer}
