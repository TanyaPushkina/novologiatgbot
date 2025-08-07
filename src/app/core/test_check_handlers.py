from bot_runner import BotRunner
import pytest
class MockMessage:
    def __init__(self):
        self.text = "/help"
        self.replied_text = None

    async def answer(self, text, parse_mode=None):
        self.replied_text = text

@pytest.mark.asyncio
async def test_help_command():
    runner = BotRunner()
    runner.register_routers()

    message = MockMessage()

    # Найдём и выполним нужный хендлер
    for handler in runner.dp.message.handlers:
        if handler.filters and any(f.key == "command" and f.value == "help" for f in handler.filters):
            await handler.callback(message)
            break

    assert message.replied_text is not None
    assert "Доступные команды" in message.replied_text