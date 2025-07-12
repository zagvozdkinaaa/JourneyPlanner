from fastapi import FastAPI
from app.database import engine
from app import models
from app.api import users, auth

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(auth.router)

