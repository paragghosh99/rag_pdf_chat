# tests/test_config.py

from app.config import CHUNK_SIZE, CHUNK_OVERLAP, TOP_K

def test_chunk_values_valid():
    assert CHUNK_SIZE > CHUNK_OVERLAP
    assert CHUNK_SIZE > 0
    assert TOP_K > 0
