# import os
from dotenv import load_dotenv

load_dotenv()

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# if OPENAI_API_KEY is None:
#     raise ValueError("OPENAI_API_KEY not set in environment")

# MODEL_NAME = "gpt-4o-mini"
MODEL_NAME = "google/flan-t5-small"

CHUNK_SIZE = 300
CHUNK_OVERLAP = 20

TOP_K = 4

PERSIST_DIR = "vector_db"
