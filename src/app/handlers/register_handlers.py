from aiogram import Dispatcher
from .help import help_handler
#from .courses import courses_handler
#from .register import register_handler


def register_all_handlers(dp: Dispatcher):
    dp.message.register(help_handler, commands=["help"])
    #dp.message.register(courses_handler, commands=["courses"])
    #dp.message.register(register_handler, commands=["register"])
