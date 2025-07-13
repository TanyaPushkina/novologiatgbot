import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from datetime import datetime, time
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Установим дневной интервал: 08:00 - 20:00
START_TIME = time(8, 0, 0)
END_TIME = time(20, 0, 0)

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    now = datetime.now().time()

    if START_TIME <= now <= END_TIME:
        await message.answer("Привет, это бот школы Новология.")
    else:
        await message.answer("⛔ Бот работает только с 08:00 до 20:00. Попробуй позже.")

async def main():
    print("✅ Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
