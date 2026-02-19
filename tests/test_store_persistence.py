# tests/test_store_persistence.py

import os
from app.config import PERSIST_DIR


def test_persist_dir_is_configured():
    assert isinstance(PERSIST_DIR, str)
    assert len(PERSIST_DIR) > 0
