from fastapi import APIRouter, Depends

from app.connectors.requests.Connector.ConnectorAuthorizeRequest import ConnectorAuthorizeRequest
from app.connectors.requests.Connector.ConnectorExecuteRequest import ConnectorExecuteRequest
from app.dependencies import get_wis_service
from app.services.wis_service import WorldInterfaceService

connector_router = APIRouter(prefix="/connect", tags=["connectors"])

@connector_router.get("/status")
async def connector_status():
    pass

@connector_router.post("/execute")
async def connector_execute(req : ConnectorExecuteRequest, wis : WorldInterfaceService = Depends(get_wis_service)):
    res = wis.connector_execute(req)
    return

@connector_router.post("/authorize")
async def connector_authorize(req : ConnectorAuthorizeRequest, wis : WorldInterfaceService = Depends(get_wis_service)):
    # todo ::: should not be this, should only pass the connector name
    res = wis.auth_connector(req)

    pass