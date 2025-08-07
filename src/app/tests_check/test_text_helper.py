'''response_text = "📋 <b>Доступные команды:</b>\n\n/start — Старт\n/help — Справка\n/courses — Список курсов\n/register — Запись на курс"
def test_help_text_contains_command_list():
    response_text = (
        "📋 <b>Доступные команды:</b>\n\n"
        "/start — Старт\n"
        "/help — Справка\n"
        "/courses — Список курсов\n"
        "/register — Запись на курс"
    )

    assert "Доступные команды" in response_text

'''
stroka = "Этот бот помогает учиться"
podstroka = "бот"
def test_check():
    assert podstroka in stroka, f"Подстрока '{podstroka}' входит в '{stroka}'"