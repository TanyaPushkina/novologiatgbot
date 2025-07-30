from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class MainMenuKeyboard:
    @staticmethod
    def get() -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📚 Посмотреть курсы")],
                [KeyboardButton(text="ℹ Регистрация")],
            ],
            resize_keyboard=True,
            input_field_placeholder="Что вас интересует?"
        )
