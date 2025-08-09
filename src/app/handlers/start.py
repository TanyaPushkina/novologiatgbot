from aiogram import Router
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
        )
