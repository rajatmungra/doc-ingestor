from fastapi.testclient import TestClient

from doc_ingestor.main import app

client = TestClient(app)

def test_health_returns_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_create_document_with_valid_url() -> None:
    response = client.post("/documents", json={"url": "https://example.com/page"})
    assert response.status_code == 201
    body = response.json()
    assert body['url'] == 'https://example.com/page'
    assert body['status'] == 'pending'
    assert "id" in body

def test_create_document_rejects_invalid_url() -> None:
    response = client.post("/documents", json={"url": "not-a-url"})
    assert response.status_code == 422

def test_create_document_rejects_missing_url() -> None:
    response = client.post("/documents", json={})
    assert response.status_code == 422

def test_create_document_rejects_long_url() -> None:
    response = client.post("/documents", json={'url': "https://example.com/" + "".join("a" for _ in range(3000))})
    assert response.status_code == 422
