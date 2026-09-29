from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "PocketSmart AI"
    secret_key: str = "change-this-development-secret"
    database_url: str = "sqlite:///./pocketsmart.db"
    gemini_api_key: str | None = None
    gemini_model: str = "gemini-3.8-flash"
    access_token_expire_minutes: int = 120
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

@lru_cache
def get_settings():
    return Settings()
