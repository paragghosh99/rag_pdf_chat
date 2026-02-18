from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.vector_store import get_vector_store
from app.config import CHUNK_SIZE, CHUNK_OVERLAP, PERSIST_DIR
import shutil, os


def ingest_pdf(pdf_path: str) -> int:
    # Step 1: Get existing store and delete collection safely
    vector_store = get_vector_store()
    try:
        vector_store.delete_collection()
    except:
        pass  # Ignore if it doesn't exist

    # Step 2: Recreate fresh store
    vector_store = get_vector_store()

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    vector_store.add_documents(chunks)

    return len(chunks)
