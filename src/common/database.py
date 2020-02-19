import logging

from flask_sqlalchemy import SQLAlchemy
from ledgercommon.flask.config import ConfigService
from ledgercommon.utils import singleton
from sqlalchemy import engine_from_config


@singleton
class Database(SQLAlchemy):
    def __init__(self, config=None):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self.config = config or ConfigService().get("DATABASE")
        self.uri = self._get_uri()
        self.logger.info(f"Initialize database {self.config}")

    def initialize_app(self, app):
        app.config["SQLALCHEMY_DATABASE_URI"] = self.uri
        self.init_app(app)

    def get_engine_from_conf(self):
        return engine_from_config({"url": self.uri}, prefix="")

    def create_all_tables(self):
        engine = self.get_engine_from_conf()
        from src.common.base_model import Base
        Base.metadata.create_all(bind=engine)

    def drop_all_tables(self):
        engine = self.get_engine_from_conf()
        from src.common.base_model import Base
        Base.metadata.drop_all(bind=engine)

    def _get_uri(self):
        POSTGRES_USER = self.config["USER"]
        POSTGRES_PW = self.config["PASSWORD"]
        POSTGRES_URL = f"{self.config['HOST']}:{self.config['PORT']}"
        POSTGRES_DB = self.config["SCHEMA"]
        SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}"
        return SQLALCHEMY_DATABASE_URI
