"""from aiogram import types, Router
from app.models.data import courses_by_age

router = Router()


@router.message(lambda msg: msg.text == "📚 Посмотреть курсы")
async def courses_handler(message: types.Message):
    text = "📚 <b>Курсы по возрастным группам:</b>\n\n"

    for age, topics in courses_by_age.items():
        text += f"<b>{age}</b>:\n"
        for course in topics:
            text += f"• {course}\n"
        text += "\n"

    await message.answer(text, parse_mode="HTML")"""
from aiogram import types, Router
from aiogram.filters.command import Command
from app.models.data import courses_by_age

router = Router()

# Общий текст курсов
def get_courses_text():
    text = "📚 <b>Курсы по возрастным группам:</b>\n\n"
    for age, topics in courses_by_age.items():
        text += f"<b>{age}</b>:\n"
        for course in topics:
            text += f"• {course}\n"
        text += "\n"
    return text

# Обработка команды /courses
@router.message(Command("courses"))
async def courses_command(message: types.Message):
    await message.answer(get_courses_text(), parse_mode="HTML")

# Обработка кнопки 📚 Посмотреть курсы
@router.message(lambda msg: msg.text == "📚 Посмотреть курсы")
async def courses_button(message: types.Message):
    await message.answer(get_courses_text(), parse_mode="HTML")
