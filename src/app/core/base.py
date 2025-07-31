from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer

class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
