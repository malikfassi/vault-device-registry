import sqlalchemy as sa
from psycopg2.errorcodes import UNIQUE_VIOLATION
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.sql.functions import now

from src.common.Database import Database
from src.common.exceptions import ModelAlreadyExistException


class TimestampMixin:
    created_at = sa.Column(sa.DateTime, default=now())


Base = declarative_base()


class BaseModel(TimestampMixin, Base):
    __abstract__ = True
    id = sa.Column(sa.Integer, primary_key=True)


    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def save(self):
        try:

            Database().session.add(self)  # Adds new object record to database
            Database().session.commit()  # Commits all changes
        except IntegrityError as e:
            if hasattr(e.orig, 'pgcode') and e.orig.pgcode == UNIQUE_VIOLATION:
                raise ModelAlreadyExistException(f"Model {self.__class__.__name__} already exists")
            else:
                raise e

    @classmethod
    def get(cls, *args, **kwargs):
        return Database().session.query(cls).filter_by(**kwargs)
