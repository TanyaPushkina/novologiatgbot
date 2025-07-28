from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command
from loguru import logger

from app.core.env_config import settings
from app.logger.logger_config import setup_logger
from app.keyboards.reply import main_menu
from app.handlers.courses import router as courses_router
from app.handlers.register import router as register_router, start_register


class BotRunner:
    def __init__(self, settings):
        self.settings = settings
        self.bot = Bot(
            token=settings.BOT_TOKEN,
            default=DefaultBotProperties(parse_mode="HTML")
        )
        self.dp = Dispatcher(storage=MemoryStorage())

    def register_routers(self):
        self.dp.include_router(courses_router)
        self.dp.include_router(register_router)

        @self.dp.message(CommandStart())
        async def start_handler(message: types.Message):
            await message.answer(
                "Привет, это бот школы Новология!\n"
                "Я помогу вам выбрать курс и записаться.",
                reply_markup=main_menu
            )

        @self.dp.message(Command("help"))
        async def help_handler(message: types.Message):
            help_text = (
                "📋 <b>Доступные команды:</b>\n\n"
                "/start — Старт\n"
                "/help — Справка\n"
                "/courses — Список курсов\n"
                "/register — Запись на курс"
            )
            await message.answer(help_text, parse_mode="HTML")

        @self.dp.message(lambda msg: msg.text == "ℹ Регистрация")
        async def start_registration_from_button(message: types.Message, state: FSMContext):
            await start_register(message, state)

    async def run(self):
        setup_logger()
        self.register_routers()
        logger.info("✅ Бот запускается...")
        await self.dp.start_polling(self.bot)
