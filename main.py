from fastapi import FastAPI, UploadFile, File
from schemas import QuestionRequest
from ingestion import ingest_pdf
from rag import answer_question
import shutil
import os

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


UPLOAD_DIR = "uploaded_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/ingest")
async def ingest(file: UploadFile = File(...)):
    if not file.filename:
        return {"error": "Invalid file"}
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks = ingest_pdf(file_path)

    return {"status": "ingested", "chunks": chunks}


@app.post("/ask")
def ask(req: QuestionRequest):
    answer = answer_question(req.question)
    return {"answer": answer}
