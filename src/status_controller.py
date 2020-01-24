import structlog  # type: ignore
from ledgercommon.flask import HttpResource
from ledgercommon.flask.routes import FilteredBlueprint, FilterTypes

logger = structlog.get_logger(__name__)


class StatusController:

    status_routes = FilteredBlueprint("status", __name__, filter_type=FilterTypes.NONE)

    @staticmethod
    @status_routes.route("/_health", methods=["GET"])
    def get_health():
        return HttpResource.success()
