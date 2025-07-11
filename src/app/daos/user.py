from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User


async def get_or_create_user(
    tg_id: int,
    username: str | None,
    full_name: str | None,
    session: AsyncSession
) -> User:
    stmt = select(User).where(User.id == tg_id)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        user = User(id=tg_id, username=username, full_name=full_name)
        session.add(user)
        await session.commit()

    return user
