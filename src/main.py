"""import asyncio  
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
import os
from dotenv import load_dotenv
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext

from app.keyboards.reply import main_menu
from app.handlers.courses import router as courses_router
from app.handlers.register import router as register_router
from app.handlers.register import start_register
from aiogram.client.default import DefaultBotProperties
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Подключаем роутеры
dp.include_router(courses_router)
dp.include_router(register_router)

# Общий текст справки
help_text = (
    "📋 <b>Доступные команды:</b>\n\n"
    "/start — Старт\n"
    "/help — Справка\n"
    "/courses — Список курсов\n"
    "/register — Запись на курс"
)

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Привет, это бот школы Новология!\n"
        "Я помогу вам выбрать курс и записаться.",
        reply_markup=main_menu
    )

@dp.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer(help_text)

@dp.message(lambda msg: msg.text == "ℹ Регистрация")
async def start_registration_from_button(message: types.Message, state: FSMContext):
    await start_register(message, state)


async def main():
    print("✅ Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())"""
import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from app.keyboards.reply import main_menu
from app.handlers.courses import router as courses_router
from app.handlers.register import router as register_router, start_register
from app.core.settings import settings  # если уже есть
from aiogram.fsm.context import FSMContext

from loguru import logger

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing in .env")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Роутеры
dp.include_router(courses_router)
dp.include_router(register_router)

# Help text
help_text = (
    "📋 <b>Доступные команды:</b>\n\n"
    "/start — Старт\n"
    "/help — Справка\n"
    "/courses — Список курсов\n"
    "/register — Запись на курс"
)

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Привет, это бот школы Новология!\n"
        "Я помогу вам выбрать курс и записаться.",
        reply_markup=main_menu
    )

@dp.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer(help_text)

@dp.message(lambda msg: msg.text == "ℹ Регистрация")
async def start_registration_from_button(message: types.Message, state: FSMContext):
    await start_register(message, state)

async def main() -> None:
    logger.add("logs/bot.log", rotation="1 MB")
    logger.info("✅ Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

