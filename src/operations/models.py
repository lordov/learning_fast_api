from sqlalchemy import (
    Integer, String,
    TIMESTAMP,
)

from sqlalchemy.orm import (
    mapped_column, Mapped
)

from src.database import Base
from datetime import datetime


class Operation(Base):
    __tablename__ = 'operation'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantity: Mapped[str] = mapped_column(String, nullable=False, default=0)
    figi: Mapped[str] = mapped_column(String, nullable=True)
    instrument_type: Mapped[str] = mapped_column(String, nullable=True)
    date: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
