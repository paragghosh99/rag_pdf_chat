# tests/unit_tests/test_rag_unit.py

from unittest.mock import patch, MagicMock
from app.rag import answer_question


class FakeDoc:
    def __init__(self, content):
        self.page_content = content


@patch("app.rag.get_llm")
@patch("app.rag.get_vector_store")
def test_answer_question_pipeline(mock_get_vector_store, mock_get_llm):
    """
    Full unit isolation of RAG pipeline:
    - No real vector DB
    - No real embeddings
    - No real LLM
    """

    # --- Mock retriever ---
    fake_retriever = MagicMock()
    fake_retriever.invoke.return_value = [
        FakeDoc("AI is artificial intelligence.")
    ]

    fake_store = MagicMock()
    fake_store.as_retriever.return_value = fake_retriever
    mock_get_vector_store.return_value = fake_store

    # --- Mock LLM ---
    fake_llm = MagicMock()
    fake_llm.generate.return_value = "AI is artificial intelligence."
    mock_get_llm.return_value = fake_llm

    # --- Execute ---
    result = answer_question("What is AI?")

    # --- Assertions ---
    assert "artificial intelligence" in result.lower()

    fake_store.as_retriever.assert_called_once()
    fake_retriever.invoke.assert_called_once_with("What is AI?")
    fake_llm.generate.assert_called_once()
