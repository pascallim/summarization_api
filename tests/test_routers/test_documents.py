import json

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from main import app
from core import crud, models
from core.utils import summarize

client = TestClient(app)

def test_read_documents(monkeypatch):
    test_data = [{"id": 1, "text": "some text"}, {"id": 2, "text": "some other text"}]

    def mock_get_documents(db, skip, limit):
        return test_data

    monkeypatch.setattr(crud, "get_documents", mock_get_documents)

    response = client.get("/documents")
    assert response.status_code == 200
    assert response.json() == test_data

def test_read_document(monkeypatch):
    test_data = {"id": 1, "text": "some text"}

    def mock_get_document(db, document_id):
        return test_data

    monkeypatch.setattr(crud, "get_document", mock_get_document)

    response = client.get("/documents/1")
    assert response.status_code == 200
    assert response.json() == test_data

def test_read_document_incorrect_id():
    response = client.get("/documents/42")
    assert response.status_code == 404
    assert response.json() == {"detail": "Document not found"}

def test_create_document(monkeypatch):
    test_payload = {"text": "some text"}
    test_response = {"id": 1, "text": "some text"}

    def mock_create_document(db, document):
        return test_response

    monkeypatch.setattr(crud, "create_document", mock_create_document)

    response = client.post("/documents", data=json.dumps(test_payload))
    assert response.status_code == 200
    assert response.json() == test_response

def test_summarize_document(monkeypatch):
    test_data = models.Document(text="some text")

    def mock_get_document(db, document_id):
        return test_data
    def mock_summarize_text(document_text):
        return "summarized text"

    monkeypatch.setattr(crud, "get_document", mock_get_document)
    monkeypatch.setattr(summarize, "summarize_text", mock_summarize_text)

    response = client.get("/documents/summarize/1")
    assert response.status_code == 200
    assert response.json() == {"document_id": 1, "summary": "summarized text"}

def test_summarize_document_incorrect_id():
    response = client.get("/documents/summarize/42")
    assert response.status_code == 404
    assert response.json() == {"detail": "Document not found"}
