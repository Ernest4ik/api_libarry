from sqlalchemy.orm import sessionmaker, Session
from api_library.database import engine
from api_library.models import models
from api_library import schemas

session = sessionmaker(engine)


def open_session(func):
    def wrapper(*args, **kwargs):
        db = None
        with session() as db:
            responce = func(db, *args, **kwargs)
        return responce
    return wrapper


@open_session
def set_user(db: Session, user: schemas.User):
    cur_user = models.User(**schemas.UserInDB)
    db.add(cur_user)
    db.commit()

@open_session
def get_user(db: Session, username: str):
    cur_user = db.query(models.User).filter_by(username=username).first()
    return cur_user

@open_session
def add_book(db: Session, book: schemas.AddBook):
    cur_book = models.Book(
        title=book.title,
        description=book.description,
        author_name=book.author_name,
        edition_count=book.edition_count
    )
    db.add(cur_book)
    db.commit()
    return cur_book
