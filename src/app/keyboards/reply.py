"""from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Посмотреть курсы")],
        [KeyboardButton(text="ℹ Регистрация")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интересует?"
)"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Посмотреть курсы")],
        [KeyboardButton(text="ℹ Регистрация")],  # убедись, что тут правильный текст
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интересует?"
)
