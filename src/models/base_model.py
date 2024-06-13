import uuid
from datetime import datetime

from sqlalchemy import TIMESTAMP, String, func
from sqlalchemy.orm import Mapped, declared_attr, mapped_column

from src.commons.database.session import db


class BaseModel(db.Model):
    __abstract__ = True

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=str(uuid.uuid4())
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now(), server_onupdate=func.now()
    )

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
