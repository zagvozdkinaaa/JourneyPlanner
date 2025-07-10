from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from app.config import settings

pwd_context= CryptContext(schemes=['bcrypt'], deprecated='auto')

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
    