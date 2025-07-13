from aiogram import types

async def help_handler(message: types.Message):
    await message.answer(
        "📋 <b>Доступные команды:</b>\n\n"
        "/start — Приветствие\n"
        "/help — Справка\n"
        "/courses — Список курсов\n"
        "/register — Запись на курс",
        parse_mode="HTML"
    )
