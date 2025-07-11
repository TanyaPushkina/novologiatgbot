from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)
sync_session = sessionmaker(bind=engine)

def get_session() -> Generator[Session, None, None]:
    with sync_session() as session:
        yield session
