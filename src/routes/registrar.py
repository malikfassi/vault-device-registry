from ledgercommon.flask.routes import RoutesRegistrar as BaseRoutesRegistrar

from src.status_controller import StatusController


class RoutesRegistrar(BaseRoutesRegistrar):

    BLUEPRINTS: list = [StatusController.status_routes]
