from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.utils.security import get_password_hash, verify_password, create_access_token
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

@router.post('/login', response_model=schemas.Token)
def login_user(login_data: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == login_data.email).first()
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail='Incorrect email or password')
    access_token=create_access_token(data = {'sub': user.email})
    return {'access_token': access_token, 'token_type': 'bearer'}

@router.get('/', response_model=List[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users=db.query(models.User).all()
    return users