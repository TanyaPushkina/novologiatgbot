
from aiogram import Router, types
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.types import Message
from app.keyboards.reply import main_menu

from app.repositories.user_repository import UserRepository
from app.core.session import get_async_session

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    # Получаем сессию
    async for session in get_async_session():
        repo = UserRepository(session)
        user = await repo.get_by_telegram_id(message.from_user.id)

        if user:
            await message.answer(
                f"С возвращением, {user.name} 👋",
                reply_markup=main_menu
            )
        else:
            await message.answer(
                "Привет, это бот школы Новология!\n"
                "Я помогу вам выбрать курс и записаться.",
                reply_markup=main_menu
            )
