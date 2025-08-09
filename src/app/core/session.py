'''from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.settings import settings  # обновлённый settings.py
from app.core.base import Base  # declarative_base() со всеми моделями

# Создаём асинхронный движок с MySQL
engine = create_async_engine(
    #settings.DATABASE_URL, 
    settings.database.url,  # <-- Исправлено
    echo=True,
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
        yield session'''
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from app.core.settings import settings
from app.core.base import Base

engine = create_async_engine(
    settings.db.database_url,   # <-- важно: через .db.database_url
    echo=True,
)

async_session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
