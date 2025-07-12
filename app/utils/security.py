from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from app.config import settings
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from app import models
from sqlalchemy.orm import Session
from app.database import get_db

pwd_context= CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer=OAuth2PasswordBearer(tokenUrl='/auth/login')

ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINUTES=30

def get_password_hash(password: str) -> str: 
    return pwd_context.hash(password) #transform password into hash

def verify_password(input_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(input_password, hashed_password) #check if input password is the same as hashed password

def create_access_token(data: dict) -> str:
    to_encode=data.copy()
    expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) #time when token expires
    to_encode.update({'exp': expire}) #add time of expiring into info about token
    encoded_jwt=jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM) 
    return encoded_jwt
    
def get_current_user(token: str = Depends(oauth2_bearer), db: Session = Depends(get_db)) -> models.User:
    try:
        payload=jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')

    user=db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
    return user