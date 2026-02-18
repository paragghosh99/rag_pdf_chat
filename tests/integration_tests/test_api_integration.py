# tests/test_api_integration.py

from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)

def test_ingest_endpoint():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    test_pdf_path = os.path.join(BASE_DIR, "documents", "Simple_RAG_Test_Document.pdf")

    with open(test_pdf_path, "rb") as f:
        response = client.post(
            "/ingest",
            files={"file": ("test.pdf", f, "application/pdf")}
        )

    assert response.status_code == 200
    assert response.json()["status"] == "ingested"
    assert response.json()["chunks"] > 0


def test_ask_endpoint():
    response = client.post(
        "/ask",
        json={"question": "What is Artificial Intelligence?"}
    )

    assert response.status_code == 200
    assert "answer" in response.json()
