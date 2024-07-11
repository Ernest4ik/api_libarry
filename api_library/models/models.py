from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Boolean


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    email = Column(String(30))
    full_name = Column(String(30))
    disabled = Column(Boolean, default=True)
    hashed_password = Column(String)


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String, default=None)
    author_name = Column(String)
    edition_count = Column(Integer)

