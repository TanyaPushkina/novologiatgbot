import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

BOT_TOKEN = "8022670442:AAHmdrx-04blUJlHlCMAahBx7MWuuvp1P6M"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Привет, это бот школы Новология.")

async def main():
    print("✅ Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
