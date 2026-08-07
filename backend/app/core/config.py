from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App
    app_name: str
    app_version: str
    debug: bool

    # Server
    host: str
    port: int

    # Database
    database_url: str

    # Security
    secret_key: str

    # Logging
    log_level: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()