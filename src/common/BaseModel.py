from psycopg2.errorcodes import UNIQUE_VIOLATION
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declared_attr
import sqlalchemy as sa
from sqlalchemy.sql.functions import now

from App import db
from src.common.exceptions import ModelAlreadyExistException


class TimestampMixin(object):
    created_at = sa.Column(sa.DateTime, default=now())


class BaseModelMixin(TimestampMixin, object):

    id = sa.Column(sa.Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def save(self):
        try:
            db.session.add(self)  # Adds new object record to database
            db.session.commit()  # Commits all changes
        except IntegrityError as e:
            if hasattr(e.orig, 'pgcode') and e.orig.pgcode == UNIQUE_VIOLATION:
                raise ModelAlreadyExistException(f"Model {self.__class__.__name__} already exists")
            else:
                raise e

    @classmethod
    def get(cls, *args, **kwargs):
        return db.session.query(cls).filter_by(**kwargs)
