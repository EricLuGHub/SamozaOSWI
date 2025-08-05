from fastapi import APIRouter, Depends

from app.connectors.requests.Ephemeral.EphConnectorDiscard import EphConnectorDiscard
from app.connectors.requests.Ephemeral.ephConnectorRequest import EphConnectorRequest
from app.dependencies import get_wis_service
from app.services.wis_service import WorldInterfaceService

ephemeral_router = APIRouter(prefix="", tags=[])

@ephemeral_router.post("/request")
async def request_eph_creds(req : EphConnectorRequest, wis: WorldInterfaceService = Depends(get_wis_service)):
    res  = wis.req_eph_creds(req)
    return {"user_id": res}


@ephemeral_router.post("/discard-creds")
async def discard_eph_creds(req : EphConnectorDiscard, wis: WorldInterfaceService = Depends(get_wis_service)):
    res = wis.discord_eph_creds(req)
    return {"response": res}





