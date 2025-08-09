
from aiogram import types, Router
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.constants.courses import courses_by_age

router = Router()

def build_courses_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=age_group, callback_data=f"age_{age_group}")]
        for age_group in courses_by_age.keys()
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

@router.message(Command("courses"))
@router.message(lambda msg: msg.text == "📚 Посмотреть курсы")
async def show_courses(message: types.Message):
    await message.answer(
        "📚 <b>Выберите возрастную группу, чтобы посмотреть доступные курсы:</b>",
        reply_markup=build_courses_keyboard(),
        parse_mode="HTML"
    )

@router.callback_query(lambda c: c.data.startswith("age_"))
async def show_courses_by_age(callback: types.CallbackQuery):
    age_group = callback.data.replace("age_", "")
    courses = courses_by_age.get(age_group)

    if not courses:
        await callback.message.answer("❌ Курсы не найдены.")
        return

    courses_text = f"<b>{age_group}</b>:\n" + "\n".join(f"• {course}" for course in courses)
    await callback.message.answer(courses_text, parse_mode="HTML")

