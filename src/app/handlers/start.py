'''from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext  

from app.keyboards import MainMenuKeyboard

class StartHandler:
    def __init__(self):
        self.router = Router()
        self.router.message(CommandStart())(self.start)

    async def start(self, message: Message, state: FSMContext) -> None:  
        await state.clear()  
        await message.answer(
            "Привет, это бот школы Новология!\n"
            "Я помогу вам выбрать курс и записаться.",
            reply_markup=MainMenuKeyboard.get()
        )'''
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext

router = Router()

class StartHandler:
    def __init__(self):
        self.router = router
        self.router.message(CommandStart())(self.start)

    async def start(self, message: Message, state: FSMContext) -> None:
        await state.clear()

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="ℹ Справка", callback_data="help")],
                [InlineKeyboardButton(text="📋 Курсы", callback_data="courses")],
                [InlineKeyboardButton(text="✍️ Регистрация", callback_data="register")],
            ]
        )

        await message.answer(
            "👋 Привет! Это бот школы Новология.\nВыберите действие ниже:",
            reply_markup=keyboard
        )
