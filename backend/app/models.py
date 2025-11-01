from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, Float, Time, ARRAY, Enum, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class CompanionType(str, enum.Enum):
    SOLO = "solo"
    COUPLE = "couple"
    FAMILY = "family"
    FRIENDS = "friends"
    BUSINESS = "business"

class User(Base):
    __tablename__='users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password= Column(String, nullable=False)

    trips = relationship('Trip', back_populates='owner')

class Trip(Base):
    __tablename__='trips'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    owner_id =  Column(Integer, ForeignKey('users.id'))
    city = Column(String, nullable=True)
    budget_per_person = Column(Float, nullable=True)
    number_of_days = Column(Integer, nullable=True)
    companions = Column(Enum(CompanionType), nullable=True)
    interests = Column(ARRAY(String), nullable=True)

    owner = relationship('User', back_populates='trips')
    activities = relationship('Activity', back_populates='trip', cascade='all, delete-orphan')

class Activity(Base):
    __tablename__='activities'

    id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey('trips.id'), nullable=False)
    day_number = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    start_time = Column(Time, nullable=True)
    duration_hours = Column(Float, nullable=True)
    estimated_cost = Column(Float, nullable=True)
    location = Column(String, nullable=True)
    is_ai_generated = Column(Boolean, default=False)
    order = Column(Integer, nullable=True)
    
    trip = relationship('Trip', back_populates='activities')

