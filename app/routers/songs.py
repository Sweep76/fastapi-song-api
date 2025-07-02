from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/songs", response_model=schemas.Song)
def create_song(song: schemas.SongCreate, db: Session = Depends(get_db)):
    db_song = models.Song(**song.model_dump())
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song

@router.get("/songs", response_model=list[schemas.Song])
def list_songs(db: Session = Depends(get_db)):
    return db.query(models.Song).all()

@router.get("/songs/{song_id}", response_model=schemas.Song)
def get_song(song_id: int, db: Session = Depends(get_db)):
    song = db.query(models.Song).get(song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return song

@router.delete("/songs/{song_id}")
def delete_song(song_id: int, db: Session = Depends(get_db)):
    song = db.query(models.Song).get(song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    db.delete(song)
    db.commit()
    return {"message": "Deleted successfully"}
