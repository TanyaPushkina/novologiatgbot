
from aiogram import Router, F, types
from aiogram.types import CallbackQuery

router = Router()

HELP_TEXT = (
    "📋 <b>Доступные команды:</b>\n\n"
    "/start — Приветствие\n"
    "/help — Справка\n"
    "/courses — Список курсов\n"
    "/register — Запись на курс"
)

@router.message(F.text.in_({"ℹ Справка", "Справка", "/help"}))
async def help_message(message: types.Message):
    await message.answer(HELP_TEXT, parse_mode="HTML")

@router.callback_query(F.data == "help")
async def help_callback(cb: CallbackQuery):
    await cb.answer()
    await cb.message.answer(HELP_TEXT, parse_mode="HTML")
