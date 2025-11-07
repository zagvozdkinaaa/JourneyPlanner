from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from app import models, schemas
from app.database import get_db
from app.utils.security import get_current_user
from typing import List

router = APIRouter(prefix='/trips', tags=['Trips'])

@router.post('/create', response_model=schemas.TripResponse)
def trip_create(trip: schemas.TripCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    new_trip = models.Trip(**trip.model_dump(exclude_unset=True), owner_id=current_user.id)
    if new_trip.start_date > new_trip.end_date:
        raise HTTPException(status_code=400, detail='Start date cannot be after end date')
    new_trip.number_of_days = (new_trip.end_date - new_trip.start_date).days + 1

    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)

    return new_trip


@router.get('/', response_model=List[schemas.TripResponse])
def get_all_trips(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    trips = db.query(models.Trip).options(
        joinedload(models.Trip.activities)
    ).filter(models.Trip.owner_id == current_user.id).all()

    return trips


@router.get('/{trip_id}', response_model=schemas.TripResponse)
def get_trip(trip_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    trip = db.query(models.Trip).options(
        joinedload(models.Trip.activities)
    ).filter(models.Trip.id == trip_id, models.Trip.owner_id == current_user.id).first()
    if not trip:
        raise HTTPException(status_code=404, detail='Trip not found')
    
    return trip


@router.put('/{trip_id}', response_model=schemas.TripResponse)
def update_trip(trip_id: int, trip_data: schemas.TripUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    trip = db.query(models.Trip).options(
        joinedload(models.Trip.activities)
    ).filter(models.Trip.id == trip_id, models.Trip.owner_id == current_user.id).first()
    if not trip:
        raise HTTPException(status_code=404, detail='Trip not found')
    trip_data_dict = trip_data.model_dump(exclude_unset=True)

    effective_start = trip_data_dict.get('start_date', trip.start_date)
    effective_end = trip_data_dict.get('end_date', trip.end_date)

    if effective_start and effective_end and effective_start > effective_end:
        raise HTTPException(status_code=400, detail='Start date cannot be after end date')

    for key, value in trip_data_dict.items():
        setattr(trip, key, value)

    if trip.start_date and trip.end_date:
        trip.number_of_days = (trip.end_date - trip.start_date).days + 1

    db.commit()
    db.refresh(trip)

    return trip


@router.delete('/{trip_id}', status_code=204)
def delete_trip(trip_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    trip=db.query(models.Trip).filter(models.Trip.id == trip_id, models.Trip.owner_id == current_user.id).first()
    if not trip:
        raise HTTPException(status_code=404, detail='Trip not found')
    
    db.delete(trip)
    db.commit()