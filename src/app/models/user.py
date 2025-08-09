
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.core.base import Base

class User(Base):
    telegram_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
