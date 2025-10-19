from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

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

    owner = relationship('User', back_populates='trips')