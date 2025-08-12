from pydantic import BaseModel, validator
import re

class ContactValidator(BaseModel):
    contact: str

    @validator("contact")
    def validate_contact(cls, v):
        v = v.strip()

        # Email
        if re.fullmatch(r"[a-zA-Z0-9._%+-]+@(gmail\.com|mail\.ru|yandex\.ru)", v, re.IGNORECASE):
            return v

        # Телефон +79XXXXXXXXX
        if re.fullmatch(r"\+79\d{9}", v):
            return v

        # Телефон 89XXXXXXXXX → преобразуем в +79XXXXXXXXX
        if re.fullmatch(r"89\d{9}", v):
            return "+7" + v[1:]

        # Если ничего не подошло
        raise ValueError(
            "Неверный формат. Введите email (gmail.com, mail.ru, yandex.ru) "
            "или телефон в формате +79XXXXXXXXX или 89XXXXXXXXX (вторая цифра — 9)"
        )
