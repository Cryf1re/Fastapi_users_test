from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import asyncio

from app.config import get_settings
from app.database import Base  # твоя базовая модель
from app.models import user  # импортируй все модели, чтобы Alembic их "увидел"

# Получаем настройки из alembic.ini
config = context.config

# Настройки логгирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Загружаем настройки из .env через pydantic
settings = get_settings()

# ❗ ВАЖНО: Alembic требует синхронный URL (psycopg2)
sync_database_url = settings.database_url.replace("postgresql+asyncpg", "postgresql+psycopg2")
config.set_main_option("sqlalchemy.url", sync_database_url)

# Указываем metadata — откуда Alembic будет брать схемы
target_metadata = Base.metadata


# --- OFFLINE режим (генерация SQL-скриптов без подключения к БД)
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# --- ONLINE режим (с подключением к базе)
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


# Выбор режима в зависимости от запуска Alembic
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()