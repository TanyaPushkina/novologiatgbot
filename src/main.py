from app.core import BotRunner
import asyncio

async def main():
    runner = BotRunner()
    await runner.run()

if __name__ == "__main__":
    asyncio.run(main())
