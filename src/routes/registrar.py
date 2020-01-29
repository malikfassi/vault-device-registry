from ledgercommon.flask.routes import RoutesRegistrar as BaseRoutesRegistrar

from src.status_controller import StatusController
from src.device_controller import DeviceController


class RoutesRegistrar(BaseRoutesRegistrar):

    BLUEPRINTS: list = [StatusController.status_routes, DeviceController.device_routes]
