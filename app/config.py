import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# if OPENAI_API_KEY is None:
#     raise ValueError("OPENAI_API_KEY not set in environment")

LLM_BACKEND = os.getenv("LLM_BACKEND", "local")
LOCAL_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "google/flan-t5-small")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

CHUNK_SIZE = 700
CHUNK_OVERLAP = 100

TOP_K = 3

PERSIST_DIR = "vector_db"
