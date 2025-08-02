from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.settings import settings  # обновлённый settings.py
from app.core.base import Base  # declarative_base() со всеми моделями

# Создаём асинхронный движок с MySQL
engine = create_async_engine(
    settings.db.url,
    echo=True,  # лог SQL-запросов, отключить на проде
)

# Асинхронная фабрика сессий
async_session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

# Генератор сессий
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
