from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

from app.core.config import settings  # путь должен соответствовать твоей структуре

# Создание асинхронного SQLAlchemy движка с использованием asyncpg драйвера
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # 🔧 На проде лучше отключить или логировать через логгер
)

# Асинхронная фабрика для создания сессий
async_session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

# Базовый класс для всех моделей
Base = declarative_base()

# Генератор сессий — может использоваться как Depends(...) в FastAPI или вручную
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
