from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class SongCreate(BaseModel):
    title: str
    length: int
    date_released: datetime
    price: Decimal

class Song(SongCreate):
    id: int

    model_config = {
        "from_attributes": True
    }

class PurchaseRequest(BaseModel):
    song_ids: list[int]

class PlaylistCreate(BaseModel):
    name: str
    song_ids: list[int] = []

class Playlist(BaseModel):
    id: int
    name: str
    songs: list[Song] = []

    model_config = {
        "from_attributes": True
    }

