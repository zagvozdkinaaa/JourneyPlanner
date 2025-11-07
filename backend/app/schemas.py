from __future__ import annotations
from pydantic import BaseModel, EmailStr, Field
from datetime import date, time
from typing import List
from app.models import CompanionType


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
    city: str | None = None
    budget_per_person: float | None = None
    companions: CompanionType | None = None
    interests: List[str] | None = None

class TripCreate(TripBase):
    pass 

class TripResponse(TripBase):
    id: int
    owner_id: int
    number_of_days: int
    activities: List[ActivityResponse] = Field(default_factory=list)

    class Config:
        from_attributes = True

class TripUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    city: str | None = None
    budget_per_person: float | None = None
    companions: CompanionType | None = None
    interests: List[str] | None = None

class ActivityBase(BaseModel):
    trip_id: int
    day_number: int
    title: str
    description: str | None = None
    start_time: time | None = None
    duration_hours: float | None = None
    estimated_cost: float | None = None
    location: str | None = None
    order: int | None = None

class ActivityCreate(ActivityBase):
    pass

class ActivityResponse(ActivityBase):
    id: int
    is_ai_generated: bool

    class Config:
        from_attributes = True

class ActivityUpdate(BaseModel):
    day_number: int | None = None
    title: str | None = None
    description: str | None = None
    start_time: time | None = None
    duration_hours: float | None = None 
    estimated_cost: float | None = None
    location: str | None = None
    order: int | None = None