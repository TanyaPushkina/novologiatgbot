from aiogram import Dispatcher
from app.handlers.help import help_handler

def register_all_handlers(dp: Dispatcher):
    dp.message.register(help_handler, commands=["help"])
   