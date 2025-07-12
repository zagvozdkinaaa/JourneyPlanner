from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.utils.security import get_password_hash, get_current_user
from typing import List

router = APIRouter(prefix='/users', tags=['Users'])

@router.post('/register', response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session=Depends(get_db)):
    existing_user=db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail='Email already registered')

    hashed_password=get_password_hash(user.password)
    new_user=models.User(email=user.email, hashed_password=hashed_password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.get('/', response_model=List[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users=db.query(models.User).all()
    return users

@router.get('/me')
def get_profile(current_user: models.User = Depends(get_current_user)):
    return current_user