from ledgercommon.flask.routes import RoutesRegistrar as BaseRoutesRegistrar

from src.devices.DevicesController import DevicesController
from src.status.StatusController import StatusController


class RoutesRegistrar(BaseRoutesRegistrar):

    BLUEPRINTS: list = [StatusController.status_routes, DevicesController.devices_routes]
