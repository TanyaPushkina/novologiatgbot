'''from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base
from app.core.settings import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session
'''
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from app.core.config import settings

# Создание асинхронного движка с использованием драйвера asyncpg
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # Убрать на проде или заменить на False
)

# Асинхронная фабрика сессий
async_session_maker = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

# Базовый класс для всех ORM моделей
Base = declarative_base()

# Генератор сессии — может использоваться как зависимость в FastAPI или вручную
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
