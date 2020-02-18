import structlog  # type: ignore
from ledgercommon.flask.routes import Blueprint, FilterTypes

from src.devices.DevicesParemeters import (
    DeviceRegisterParameters,
    DeviceSearchParameters,
)
from src.devices.DevicesService import DevicesService

logger = structlog.get_logger(__name__)


class DevicesController:

    devices_routes = Blueprint("devices", __name__, filter_type=FilterTypes.NONE)
    devices_service = DevicesService()

    @staticmethod
    @devices_routes.route(
        "/register", methods=["POST"], request_model=DeviceRegisterParameters
    )
    def register_device(request_args: DeviceRegisterParameters):
        DevicesController.devices_service.register(request_args)

    @staticmethod
    @devices_routes.route(
        "/device", methods=["GET"], request_model=DeviceSearchParameters
    )
    def get_workspaces(request_args: DeviceSearchParameters):
        return DevicesController.devices_service.get_workspaces(request_args)
