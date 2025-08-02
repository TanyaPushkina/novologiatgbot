# NovologiatgBot

Telegram-бот позволяет пользователям записаться на курсы по возрастной группе. Использует MySQL для хранения данных, Redis для FSM (Finite State Machine), и написан на базе `aiogram`.

---

## Возможности

- Команды `/start`, `/help`, `/courses`, `/register`
- FSM-регистрация: имя, возраст, курс, контакт
- Кнопки: "Посмотреть курсы", "Записаться"
- Inline-клавиатура для выбора курса
- Отправка заявок админу
- Парсинг и валидация email/телефона

---

## Стек

- Python 3.12+
- [Aiogram 3.x]
- MySQL (через `aiomysql`)
- Redis (для хранения состояний FSM)
- Pydantic / Pydantic Settings
- Poetry

---

## Установка

### 1. Клонируй репозиторий

```bash
git clone https://github.com/TanyaPushkina/novologiatgbot.git
cd novologiatgbot
