from fastapi import Depends, APIRouter, HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from app import models, schemas
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.security import verify_password, create_access_token
from app.utils.security import ALGORITHM

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.post('/login', response_model=schemas.Token)
def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail='Incorrect email or password')
    access_token=create_access_token(data = {'sub': user.email})
    return {'access_token': access_token, 'token_type': 'bearer'}
