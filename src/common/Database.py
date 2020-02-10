import logging

from flask_sqlalchemy import SQLAlchemy
from ledgercommon.flask.config import ConfigService
from ledgercommon.utils import singleton


@singleton
class Database(SQLAlchemy):
    def __init__(self):
        self.config = ConfigService().get("DATABASE")
        self.logger = logging.getLogger(__name__)
        super().__init__()

    def initialize(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = self.get_uri()
        self.init_app(app)
        with app.app_context():
            self.create_all()

    def get_uri(self):
        POSTGRES_USER = self.config['USER']
        POSTGRES_PW = self.config['PASSWORD']
        POSTGRES_URL = f"{self.config['HOST']}:{self.config['PORT']}"
        POSTGRES_DB = self.config['SCHEMA']
        SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'
        return SQLALCHEMY_DATABASE_URI
