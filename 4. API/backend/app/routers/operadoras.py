from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.operadora import OperadoraResponse
from app.core.database import get_db
from app.services.operadora import buscar_operadoras_fuzzy

router = APIRouter(prefix="/operadoras", tags=["Operadoras"])

@router.get("/buscar", response_model=List[OperadoraResponse])
async def buscar_operadoras(q: str = Query(..., min_length=2), db: AsyncSession = Depends(get_db)):
    return await buscar_operadoras_fuzzy(q, db)
