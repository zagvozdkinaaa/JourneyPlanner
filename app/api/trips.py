from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.utils.security import get_password_hash, get_current_user
from typing import List

router = APIRouter(prefix='/trips', tags=['Trips'])

@router.post('/create', response_model=schemas.TripResponse)
def trip_create(trip: schemas.TripCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    new_trip = models.Trip(**trip.dict(), owner_id=current_user.id)

    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)

    return new_trip

@router.get('/', response_model=List[schemas.TripResponse])
def get_all_trips(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    trips=db.query(models.Trip).filter(models.Trip.owner_id == current_user.id).all()

    return trips