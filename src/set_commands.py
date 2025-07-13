from aiogram import Bot, types
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)

async def set_bot_commands():
    commands = [
        types.BotCommand(command="start", description="Приветствие"),
        types.BotCommand(command="help", description="Список команд"),
        types.BotCommand(command="courses", description="Список курсов"),
        types.BotCommand(command="register", description="Запись на курс"),
    ]
    await bot.set_my_commands(commands)
    print("✅ Команды Telegram обновлены")

if __name__ == "__main__":
    asyncio.run(set_bot_commands())
