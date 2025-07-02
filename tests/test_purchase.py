import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def create_song(title, price):
    return client.post("/songs", json={
        "title": title,
        "length": 200,
        "date_released": "2023-01-01T00:00:00",
        "price": price
    }).json()

def test_purchase_under_10():
    song1 = create_song("Cheap Song 1", 3.00)
    song2 = create_song("Cheap Song 2", 4.00)

    response = client.post("/purchase", json={
        "song_ids": [song1["id"], song2["id"]]
    })

    assert response.status_code == 200
    assert "Purchased" in response.json()["message"]

def test_purchase_over_10():
    song1 = create_song("Expensive Song 1", 6.00)
    song2 = create_song("Expensive Song 2", 5.00)

    response = client.post("/purchase", json={
        "song_ids": [song1["id"], song2["id"]]
    })

    assert response.status_code == 200
    assert "Purchased" in response.json()["message"]

def test_purchase_invalid_id():
    response = client.post("/purchase", json={"song_ids": [999]})
    assert response.status_code == 404
