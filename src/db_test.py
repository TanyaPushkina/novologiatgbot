import asyncio
from sqlalchemy import text

from app.core.session import get_async_session

async def test_connection():
    async for session in get_async_session():
        result = await session.execute(text("SELECT DATABASE();"))
        db_name = result.scalar()
        print(f"✅ Connected to database: {db_name}")

if __name__ == "__main__":
    asyncio.run(test_connection())
