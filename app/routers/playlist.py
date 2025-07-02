from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
import random

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/playlists", response_model=schemas.Playlist)
def create_playlist(playlist: schemas.PlaylistCreate, db: Session = Depends(get_db)):
    songs = db.query(models.Song).filter(models.Song.id.in_(playlist.song_ids)).all()
    new_playlist = models.Playlist(name=playlist.name, songs=songs)
    db.add(new_playlist)
    db.commit()
    db.refresh(new_playlist)
    return new_playlist

@router.get("/playlists", response_model=list[schemas.Playlist])
def list_playlists(db: Session = Depends(get_db)):
    return db.query(models.Playlist).all()

@router.post("/playlists/{playlist_id}/shuffle", response_model=schemas.Playlist)
def shuffle_playlist(playlist_id: int, db: Session = Depends(get_db)):
    playlist = db.get(models.Playlist, playlist_id)
    if not playlist:
        raise HTTPException(status_code=404, detail="Playlist not found")

    songs = playlist.songs
    random.shuffle(songs)
    playlist.songs = songs
    db.commit()
    db.refresh(playlist)
    return playlist
