
from aiogram import Bot, Dispatcher
from app.core.config import settings
from app.handlers import start

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(start.router)

async def main():
    print("✅ Бот запускается...")
    await dp.start_polling(bot)
