from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_")

    app_name: str = "doc-ingestor"
    environment: str = "local"

settings = Settings()
