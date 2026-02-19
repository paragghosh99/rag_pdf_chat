from fastapi import FastAPI, UploadFile, File
from app.schemas import QuestionRequest
from app.ingestion import ingest_pdf
from app.rag import answer_question
import shutil
import os
from fastapi.responses import FileResponse
from app.config import BASE_DIR

INDEX_FILE = BASE_DIR / "frontend" / "index.html"

app = FastAPI()

@app.get("/")
def serve_ui():
    return FileResponse(INDEX_FILE)

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
