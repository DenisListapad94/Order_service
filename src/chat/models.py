from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column
from src.models import Base


class Message(Base):
    __tablename__ = "message"

    id = mapped_column(Integer, primary_key=True)
    message = mapped_column(String(50))

