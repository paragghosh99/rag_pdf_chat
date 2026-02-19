# tests/unit_tests/test_clean_text.py

from app.helper.clean_text import clean_text

def test_removes_extra_spaces():
    text = "Hello    world"
    assert clean_text(text) == "Hello world"

def test_removes_line_breaks():
    text = "Hello\n\nworld"
    assert clean_text(text) == "Hello world"

def test_strips_edges():
    text = "   Hello world   "
    assert clean_text(text) == "Hello world"
