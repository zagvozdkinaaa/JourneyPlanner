from fastapi import FastAPI
from app.database import engine
from app import models
from app.api import users

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)

