from sqlalchemy import BigInteger, Text
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    balance: Mapped[int] = mapped_column(nullable=False)
    wallet: Mapped[str] = mapped_column(nullable=False)
    invited: Mapped[int] = mapped_column(nullable=False)
    inviter_id: Mapped[int] =  mapped_column(nullable=False)