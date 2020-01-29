import structlog  # type: ignore
from flask import request
from ledgercommon.flask import HttpResource
from ledgercommon.flask.routes import FilteredBlueprint, FilterTypes

logger = structlog.get_logger(__name__)


class DeviceController:

    # /!\ We probably don't want FilterTypes.NONE here, but instead VALID_API_KEY
    #     Anyway, as it was not working I put NONE, lol.
    device_routes = FilteredBlueprint("device", __name__, filter_type=FilterTypes.NONE)

    @staticmethod
    @device_routes.route("/register", methods=["POST"])
    def register():
        data = request.json
        print("---")
        print("-> Registering a device")
        print(data['pub_key'])
        print("---")
        return HttpResource.success()
