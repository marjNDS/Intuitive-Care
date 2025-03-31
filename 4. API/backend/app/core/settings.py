from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:6669@localhost:5432/IntuitiveCare"

    class Config:
        env_file = ".env"

settings:Settings = Settings()
