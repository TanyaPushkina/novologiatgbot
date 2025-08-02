import asyncio
import redis.asyncio as redis
from app.core.settings import settings


async def main():
    r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

    try:
        await r.set("bot_test_key", "Привет, Redis!")
        value = await r.get("bot_test_key")
        print("✅ Redis доступен. Полученное значение:", value.decode())
    except Exception as e:
        print("❌ Ошибка при подключении к Redis:", e)


if __name__ == "__main__":
    asyncio.run(main())
