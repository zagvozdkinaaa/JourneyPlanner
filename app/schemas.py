from pydantic import BaseModel, EmailStr
from datetime import date

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config():
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TripBase(BaseModel):
    title: str
    description: str | None = None
    start_date: date
    end_date: date

class TripCreate(TripBase):
    pass 

class TripResponse(TripBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class TripUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    start_date: date | None = None
    end_date: date | None = None