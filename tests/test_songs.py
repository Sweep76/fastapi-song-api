import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_song():
    response = client.post("/songs", json={
        "title": "Test Song",
        "length": 180,
        "date_released": "2023-01-01T00:00:00",
        "price": 4.99
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Song"
    assert data["length"] == 180

def test_get_songs():
    response = client.get("/songs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
