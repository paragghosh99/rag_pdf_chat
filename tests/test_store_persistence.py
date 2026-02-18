import os
from app.config import PERSIST_DIR

def test_vector_store_created():
    assert os.path.exists(PERSIST_DIR)
