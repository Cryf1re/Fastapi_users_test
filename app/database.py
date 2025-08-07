from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.config import get_settings
from contextlib import asynccontextmanager
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


settings = get_settings()


async_engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,
    pool_size=10,
    max_overflow=20,
)

async_session_maker = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session