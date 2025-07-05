from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship
from database import Base

class User(Base):
    __tablename__='users'

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, index=True)
    age=Column(Integer)