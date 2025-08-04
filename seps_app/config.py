from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    seps_db_url: str
    host: str
    port: int
    port_seps: int
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
