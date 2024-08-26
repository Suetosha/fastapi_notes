from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    id = mapped_column(Integer, primary_key=True)
    email = mapped_column(String, nullable=False, unique=True)
    hashed_password = mapped_column(String, nullable=False)
    is_active = mapped_column(Boolean, nullable=False, default=True)
    is_superuser = mapped_column(Boolean, nullable=False, default=False)
    is_verified = mapped_column(Boolean, nullable=False, default=False)


class Note(Base):
    __tablename__ = 'note'

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String, nullable=False)
    content = mapped_column(String, nullable=False)
    user_id = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
