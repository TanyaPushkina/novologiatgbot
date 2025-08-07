import pytest
from aiogram import types
from datetime import datetime
from unittest.mock import AsyncMock, patch
from app.handlers.help import help_handler  

@pytest.mark.asyncio
async def test_help_handler_direct_call():
    message = types.Message(
        message_id=1,
        from_user=types.User(id=123, is_bot=False, first_name="Test"),
        chat=types.Chat(id=123, type="private"),
        date=datetime.now(),
        message_thread_id=None,
        text="/help"
    )

    with patch.object(types.Message, "answer", new_callable=AsyncMock) as mock_answer:
        await help_handler(message)

        mock_answer.assert_called_once()
        called_text = mock_answer.call_args.args[0]
        assert "Доступные команды" in called_text
