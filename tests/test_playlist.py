import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def create_song(title, price=2.0):
    return client.post("/songs", json={
        "title": title,
        "length": 180,
        "date_released": "2023-01-01T00:00:00",
        "price": price
    }).json()

def test_create_playlist():
    song1 = create_song("P1")
    song2 = create_song("P2")

    response = client.post("/playlists", json={
        "name": "My Playlist",
        "song_ids": [song1["id"], song2["id"]]
    })

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "My Playlist"
    assert len(data["songs"]) == 2

def test_shuffle_playlist():
    # Create songs
    song1 = create_song("Shuffle A")
    song2 = create_song("Shuffle B")
    song3 = create_song("Shuffle C")

    # Create playlist
    playlist = client.post("/playlists", json={
        "name": "Shuffler",
        "song_ids": [song1["id"], song2["id"], song3["id"]]
    }).json()

    # Shuffle
    response = client.post(f"/playlists/{playlist['id']}/shuffle")
    assert response.status_code == 200
    assert response.json()["name"] == "Shuffler"
