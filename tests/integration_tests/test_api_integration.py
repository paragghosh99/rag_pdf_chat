# tests/integration_tests/test_api_integration.py

from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)


@patch("main.ingest_pdf")
def test_ingest_endpoint(mock_ingest):
    mock_ingest.return_value = 5

    response = client.post(
        "/ingest",
        files={"file": ("test.pdf", b"dummy content", "application/pdf")}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "ingested"
    assert response.json()["chunks"] == 5

    mock_ingest.assert_called_once()


@patch("main.answer_question")
def test_ask_endpoint(mock_answer):
    mock_answer.return_value = "Artificial Intelligence is..."

    response = client.post(
        "/ask",
        json={"question": "What is AI?"}
    )

    assert response.status_code == 200
    assert response.json()["answer"] == "Artificial Intelligence is..."

    mock_answer.assert_called_once_with("What is AI?")
