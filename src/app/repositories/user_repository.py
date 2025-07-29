'''from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_telegram_id(self, telegram_id: int) -> Optional[User]:
        result = await self.session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()

    async def create(self, telegram_id: int, name: str) -> User:
        user = User(telegram_id=telegram_id, name=name)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
'''
# app/repositories/user_repository.py
from app.models.user import User
from crud.base import BaseRepository
from sqlalchemy import select


class UserRepository(BaseRepository[User]):
    def __init__(self, session):
        super().__init__(User, session)

    async def get_by_telegram_id(self, telegram_id: int):
        result = await self.session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()

    async def create(self, telegram_id: int, name: str) -> User:
        user = User(telegram_id=telegram_id, name=name)
        return await self.add(user)
