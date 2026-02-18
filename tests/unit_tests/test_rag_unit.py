# tests/test_rag_unit.py

from unittest.mock import patch, MagicMock
from app.rag import answer_question

class FakeDoc:
    def __init__(self, content):
        self.page_content = content

@patch("app.rag.generate_answer")
@patch("app.rag.get_vector_store")
def test_answer_question_pipeline(mock_vector_store, mock_generate):

    # Mock retrieval
    fake_retriever = MagicMock()
    fake_retriever.invoke.return_value = [
        FakeDoc("AI is artificial intelligence.")
    ]

    mock_store_instance = MagicMock()
    mock_store_instance.as_retriever.return_value = fake_retriever
    mock_vector_store.return_value = mock_store_instance

    mock_generate.return_value = "AI is artificial intelligence."

    result = answer_question("What is AI?")

    assert "artificial intelligence" in result
    fake_retriever.invoke.assert_called_once()
    mock_generate.assert_called_once()
