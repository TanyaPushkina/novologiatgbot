from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from loguru import logger

from app.core.settings import settings
from app.logger.logger_config import setup_logger
from app.keyboards import MainMenuKeyboard
from app.handlers.courses import router as courses_router
from app.handlers.register import router as register_router, start_register
from app.handlers.start import StartHandler


class BotRunner:
    def __init__(self) -> None:
       
        self.bot: Bot = Bot(
            token=settings.bot.bot_token,
            default=DefaultBotProperties(parse_mode="HTML"),
        )

        
        self.dp: Dispatcher = Dispatcher(
            storage=RedisStorage.from_url(settings.redis.url)
        )

    def register_routers(self) -> None:
        
        self.dp.include_router(StartHandler().router)
        self.dp.include_router(courses_router)
        self.dp.include_router(register_router)

        @self.dp.message(Command("help"))
        async def help_handler(message: types.Message) -> None:
            help_text = (
                "📋 <b>Доступные команды:</b>\n\n"
                "/start — Старт\n"
                "/help — Справка\n"
                "/courses — Список курсов\n"
                "/register — Запись на курс"
            )
            await message.answer(help_text)

        @self.dp.message(lambda msg: msg.text == "ℹ Регистрация")
        async def start_registration_from_button(message: types.Message, state: FSMContext) -> None:
            await start_register(message, state)

    async def run(self) -> None:
        setup_logger()
        self.register_routers()
        logger.info("✅ Бот запускается...")
        await self.dp.start_polling(self.bot)
