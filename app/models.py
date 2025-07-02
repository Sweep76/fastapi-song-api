from sqlalchemy import Column, Integer, String, DateTime, Numeric, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

# Association table for many-to-many relationship between playlists and songs
playlist_song = Table(
    'playlist_song',
    Base.metadata,
    Column('playlist_id', Integer, ForeignKey('playlists.id')),
    Column('song_id', Integer, ForeignKey('songs.id'))
)

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    length = Column(Integer, nullable=False)  # in seconds
    date_released = Column(DateTime, default=datetime.datetime.utcnow)
    price = Column(Numeric(10, 2), nullable=False)

    playlists = relationship("Playlist", secondary=playlist_song, back_populates="songs")

class Playlist(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    songs = relationship("Song", secondary=playlist_song, back_populates="playlists")
