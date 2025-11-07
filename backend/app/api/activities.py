from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.utils.security import get_current_user
from typing import List

router = APIRouter(prefix='/activities', tags=['Activities'])

@router.post('/create', response_model=schemas.ActivityResponse)
def create_activity(activity: schemas.ActivityCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    trip = db.query(models.Trip).filter(models.Trip.id == activity.trip_id, models.Trip.owner_id == current_user.id).first()
    if not trip:
        raise HTTPException(status_code=404, detail='Trip not found')

    new_activity = models.Activity(**activity.model_dump(exclude_unset=True))
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)

    return new_activity


@router.get('/trip/{trip_id}', response_model=List[schemas.ActivityResponse])
def get_trip_activities(trip_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    trip = db.query(models.Trip).filter(models.Trip.id == trip_id, models.Trip.owner_id == current_user.id).first()
    if not trip:
        raise HTTPException(status_code=404, detail='Trip not found')

    activities = db.query(models.Activity).filter(models.Activity.trip_id == trip_id).all()

    return activities


@router.get('/{activity_id}', response_model=schemas.ActivityResponse)
def get_activity(activity_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    activity = db.query(models.Activity).filter(models.Activity.id == activity_id).first()
    if not activity or not activity.trip or activity.trip.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail='Activity not found')
    return activity


@router.put('/{activity_id}', response_model=schemas.ActivityResponse)
def update_activity(activity_id: int, activity_data: schemas.ActivityUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    activity = db.query(models.Activity).filter(models.Activity.id == activity_id).first()
    if not activity or not activity.trip or activity.trip.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail='Activity not found')
    activity_data_dict = activity_data.model_dump(exclude_unset=True)
    for key, value in activity_data_dict.items():
        setattr(activity, key, value)
    db.commit()
    db.refresh(activity)
    return activity


@router.delete('/{activity_id}', status_code=204)
def delete_activity(activity_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    activity = db.query(models.Activity).filter(models.Activity.id == activity_id).first()
    if not activity or not activity.trip or activity.trip.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail='Activity not found')
    db.delete(activity)
    db.commit()
