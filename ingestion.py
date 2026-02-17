from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from vector_store import get_vector_store
from config import CHUNK_SIZE, CHUNK_OVERLAP


def ingest_pdf(pdf_path: str) -> int:
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    vector_store = get_vector_store()
    vector_store.add_documents(chunks)
    # vector_store.persist() -> only needed for OpenAiEmbeddings. HuggingFaceEmbeddings does it automatically

    return len(chunks)
