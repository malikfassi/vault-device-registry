from ledgercommon.flask.routes import RoutesRegistrar as BaseRoutesRegistrar

from src.devices.devices_controller import DevicesController
from src.status.status_controller import StatusController


class RoutesRegistrar(BaseRoutesRegistrar):

    BLUEPRINTS: list = [
        StatusController.status_routes,
        DevicesController.devices_routes,
    ]
