from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from typing import List
from app.schemas.operadora import OperadoraResponse

async def buscar_operadoras_fuzzy(q: str, db: AsyncSession) -> List[OperadoraResponse]:
    query = text("""
        SELECT * FROM operadoras_ativas
        WHERE unaccent(razao_social) ILIKE unaccent(:q)
           OR unaccent(nome_fantasia) ILIKE unaccent(:q)
           OR cnpj ILIKE :q
           OR CAST(registro_ans AS TEXT) ILIKE :q
        LIMIT 20
    """)

    result = await db.execute(query, {"q": f"%{q}%"})
    rows = result.fetchall()
    return [OperadoraResponse(**dict(row)) for row in rows]