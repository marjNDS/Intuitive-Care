
#to run: uvicorn app.main:app --reload

from fastapi import FastAPI
from app.core.settings import settings
from app.routers import operadoras

app = FastAPI(title=settings.API_V1_STR)

app.include_router(operadoras.router)
