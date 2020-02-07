import structlog  # type: ignore
from ledgercommon.flask.routes import Blueprint, FilterTypes

logger = structlog.get_logger(__name__)


class StatusController:

    status_routes = Blueprint("status", __name__, filter_type=FilterTypes.NONE)

    @staticmethod
    @status_routes.route("/_health", methods=["GET"])
    def get_health():
        pass
