import sqlalchemy as sa

from sqlalchemy import UniqueConstraint

from App import db
from src.common.BaseModel import BaseModelMixin


class Device(BaseModelMixin, db.Model):

    pub_key = sa.Column(sa.String)
    workspace = sa.Column(sa.String)

    __table_args__ = (UniqueConstraint('pub_key', 'workspace', name='_pub_key_workspace_uc'),
                      )

    def __repr__(self):
        return "<Device(name={self.pub_key!r})>".format(self=self)
