from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base_model import BaseModel


class User(BaseModel):
    email: Mapped[str] = mapped_column(String(255), unique=True)
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    hashed_password: Mapped[str] = mapped_column(String(255))
