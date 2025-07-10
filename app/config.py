from pydantic_settings import BaseSettings

#safe way of taking vulnerable data or constants from .env file

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str

    class Config():
        env_file = '.env'

settings = Settings()