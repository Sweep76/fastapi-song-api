from fastapi import FastAPI
from app.database import Base, engine
from app.routers import songs, purchase
from app.routers import playlist


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(songs.router)
app.include_router(purchase.router)
app.include_router(playlist.router)

