
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy import Integer

class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
       
        return cls.__name__.lower() + "s"

    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
