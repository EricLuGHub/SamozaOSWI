from fastapi import APIRouter, Depends

from seps_app.dependencies import get_composio_service
from seps_app.requests.addConnectorRequest import AddConnectorRequest
from seps_app.services.composio_service import ComposioService

creds_router = APIRouter(prefix="", tags=[])

@creds_router.post("/add")
async def add_credential(new_connector : AddConnectorRequest, svc: ComposioService = Depends(get_composio_service)):
    res  = svc.begin_add_connector(new_connector.connector_name)
    return res


@creds_router.post("/claim-creds")
async def create_badge(new_badge : BadgeDTO, svc: BadgeService = Depends(get_badge_service)):
    badge_id  = svc.create_badge(new_badge)
    return {"badge_id": badge_id}




