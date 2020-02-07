from ledgercommon.json import CustomJSONEncoder
from ledgercommon.logging import setup_logging, get_correlation_id_log_processor
from ledgercommon.flask import Flask, HTTPExceptionsHandler, get_correlation_id
from ledgercommon.flask.config import ConfigService
from ledgercommon.flask.routes import RequestsFilter, FUNCTION_FILTERS

from flask_cors import CORS
from flask import g
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class App(Flask):
    def __init__(self):
        super().__init__(__name__)

        self.json_encoder = CustomJSONEncoder

        self.config.from_yaml('conf.yaml')
        self.config_service = ConfigService()
        self.config_service.initialize(self.config)
        self.logger = self.config_logger()
        self.config_app()

        CORS(
            self,
            supports_credentials=True  # required for cross origin cookie requests
        )
        self.register_routes()

        self.request_filter = RequestsFilter(FUNCTION_FILTERS)

        self.config_service.info()

        @self.errorhandler(Exception)
        def exception(e):
            return HTTPExceptionsHandler().handle(e)

        @self.before_request
        def pre_request():
            return self.execute_before_request()

        @self.teardown_request
        def post_request(exc):
            return self.execute_teardown_request(exc)

    def execute_before_request(self):
        pass

    def execute_teardown_request(self, exc):
        pass

    def filter_request(self):
        user = self.request_filter.filter_request(self)
        if user:
            g.user = user

    def config_app(self):
        self.db = self.init_db()

    def config_logger(self):
        return setup_logging(
            self.config_service.is_dev,
            extra_processors=[get_correlation_id_log_processor(get_correlation_id)]
        )

    def init_db(self):
        self.logger.info("Initialize database", config=self.config["DATABASE"])
        config = self.config_service.get("DATABASE")
        POSTGRES_USER = config['USER']
        POSTGRES_PW = config['PASSWORD']
        POSTGRES_URL = f"{config['HOST']}:{config['PORT']}"
        POSTGRES_DB = config['SCHEMA']

        self.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'
        db.init_app(self)
        # DB initialization
        with self.app_context():
            from src.devices.Device import Device
            db.create_all()

    def register_routes(self):
        # Routes registration
        from src.routes.registrar import RoutesRegistrar
        route_registrar = RoutesRegistrar(self)
        route_registrar.register()