# Novologia Telegram Bot

Telegram-бот, разработанный на основе фреймворка `aiogram 3.x`, с использованием асинхронного PostgreSQL (`asyncpg`) и Redis.

## Возможности

- Обработка пользовательских команд
- Подключение к базе данных PostgreSQL
- Интеграция с Redis
- Гибкая конфигурация через `.env`
- Асинхронная архитектура

## Стек технологий

- Python 3.12+
- aiogram 3.x
- PostgreSQL (asyncpg)
- SQLAlchemy 2.0 (async)
- Redis
- Docker + Poetry

## Установка

```bash
git clone https://github.com/yourname/novologiatgbot.git
cd novologiatgbot
poetry install
