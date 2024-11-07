from typing import Annotated

from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from src.models.config import settings

# создания движка sqlalchemy для работы с БД
engine = create_engine(url=settings.DATABASE_URL, echo=False)
# создаем сессию
sessions = sessionmaker(bind=engine)

str_50 = Annotated[str, 50]
str_36 = Annotated[str, 36]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_50: String(50),
        str_36: String(36)
    }
