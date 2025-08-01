from fastapi import APIRouter, Depends

from app.connectors.requests.Connector.ConnectorAuthorizeRequest import ConnectorAuthorizeRequest
from app.connectors.requests.Connector.ConnectorExecuteRequest import ConnectorExecuteRequest
from app.dependencies import get_wis_service
from app.services.wis_service import WorldInterfaceService
from fastapi import BackgroundTasks
connector_router = APIRouter(prefix="", tags=["connectors"])

@connector_router.post("/execute")
async def connector_execute(req : ConnectorExecuteRequest, wis : WorldInterfaceService = Depends(get_wis_service)):
    res = wis.connector_execute(req)
    return

@connector_router.post("/authorize")
async def connector_authorize(
        req : ConnectorAuthorizeRequest,
        background_tasks: BackgroundTasks,
        wis : WorldInterfaceService = Depends(get_wis_service)):
    res = wis.auth_connector(req, background_tasks)
    return res

@connector_router.post("/disconnect")
async def connector_disconnect(req : ConnectorAuthorizeRequest, wis : WorldInterfaceService = Depends(get_wis_service)):
    # TODO: just delete the entry from db
    pass