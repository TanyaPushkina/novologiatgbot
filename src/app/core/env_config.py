from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str
    DATABASE_URL: str
    REDIS_HOST: str
    REDIS_PORT: int
    ADMIN_ID: int  
    PARSE_MODE: str = "HTML"  

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()
