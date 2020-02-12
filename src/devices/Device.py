import sqlalchemy as sa
from sqlalchemy import UniqueConstraint

from src.common.BaseModel import BaseModel


class Device(BaseModel):

    pub_key = sa.Column(sa.String)
    workspace = sa.Column(sa.String)

    __table_args__ = (UniqueConstraint('pub_key', 'workspace', name='_pub_key_workspace_uc'),
                      )

    def __repr__(self):
        return f"<Device(name={self.pub_key})>"
