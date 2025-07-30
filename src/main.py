import asyncio
from app.core import BotRunner
from app.core.env_config import settings

async def main():
    runner = BotRunner(settings)
    await runner.run()

if __name__ == "__main__":
    asyncio.run(main())


