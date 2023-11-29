from fastapi import FastAPI
from router import client_router
from models.base import Base
from models.client import Client
from models.ouvrage import Ouvrage
from config.connexion import engine
from .models import Commentaire

app = FastAPI()

app.include_router(client_router.router)

Base.metadata.create_all(engine)