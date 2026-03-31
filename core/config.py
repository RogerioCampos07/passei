from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DEBUG: bool = True
    SECRET_KEY: str
    ALLOWED_HOSTS: str
    
    # Novos campos para o Banco
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int = 5432

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

config = Settings()