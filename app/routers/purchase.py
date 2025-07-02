from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, models, schemas
from app.services.payment_gateway import CheapPaymentGateway, ExpensivePaymentGateway

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/purchase")
def purchase_songs(purchase: schemas.PurchaseRequest, db: Session = Depends(get_db)):
    songs = db.query(models.Song).filter(models.Song.id.in_(purchase.song_ids)).all()
    if not songs:
        raise HTTPException(status_code=404, detail="No songs found")

    total = sum([float(song.price) for song in songs])

    if total < 10:
        gateway = CheapPaymentGateway()
    else:
        gateway = ExpensivePaymentGateway()

    success = gateway.process_payment(total)
    if not success:
        raise HTTPException(status_code=500, detail="Payment failed")

    return {"message": f"Purchased {len(songs)} songs for ${total}"}
