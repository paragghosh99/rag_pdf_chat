import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_rag_returns_correct_fact(client):
    response = client.post(
        "/ask",
        json={"question": "What is General AI?"}
    )

    assert "does not yet exist" in response.json()["answer"].lower()
