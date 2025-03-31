from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from app.core.settings import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL, echo=True)

Session: sessionmaker = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)

# Dependência para injetar a sessão assíncrona no FastAPI
async def get_db():
    async with Session() as session:
        yield session


