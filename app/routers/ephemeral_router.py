from fastapi import APIRouter, Depends
from app.connectors.requests.Ephemeral.ephConnectorRequest import EphConnectorRequest
from app.dependencies import get_wis_service
from app.services.wis_service import WorldInterfaceService

ephemeral_router = APIRouter(prefix="", tags=[])

@ephemeral_router.post("/request")
async def create_badge(new_badge : EphConnectorRequest, svc: WorldInterfaceService = Depends(get_wis_service)):
    badge_id  = svc.create_badge(new_badge)
    return {"badge_id": badge_id}





