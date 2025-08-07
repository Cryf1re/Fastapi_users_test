# pyright: reportCallIssue=false
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    """
    Класс настроек проекта.
    Значения автоматически подтягиваются из .env файла.
    """

    # Указываем, откуда грузить переменные
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )
    
    # Обязательные переменные (из .env)
    database_host: str
    database_port: int
    database_name: str
    database_user: str
    database_password: str


    # Настройки Redis
    redis_host: str
    redis_port: int
    redis_db: int = 0


    # Настройки OAuth и fastapi-users
    secret: str

    # Необязательные переменные с дефолтами
    app_host: str = "127.0.0.1"
    app_port: int = 8000
    debug: bool = True

    # Дополнительные настройки
    @property
    def database_url(self) -> str:
        """
        Собираем URL для подключения к PostgreSQL.
        """
        return (
            f"postgresql+asyncpg://{self.database_user}:{self.database_password}"
            f"@{self.database_host}:{self.database_port}/{self.database_name}"
        )
    
    @property
    def redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db}"

# Функция с кэшем — создаёт один экземпляр настроек на всё приложение
@lru_cache
def get_settings() -> Settings:
    return Settings()