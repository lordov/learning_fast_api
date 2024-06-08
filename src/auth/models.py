from sqlalchemy import (
    Column, Integer, String,
    TIMESTAMP, ForeignKey, JSON, Boolean
)

from sqlalchemy.orm import (
    relationship, mapped_column, Mapped
)
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from datetime import datetime
from src.database import Base


# Определение моделей


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)

    user = relationship('User', back_populates='role')


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    registered_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=datetime.now)
    role_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Role.id), nullable=False)
    role = relationship('Role', back_populates='user')
