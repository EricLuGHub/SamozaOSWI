from pydantic import BaseSettings

class Settings(BaseSettings):
    db_url: str
    host: str = "127.0.0.1"
    port: int = 8122

    class Config:
        env_file = ".env"