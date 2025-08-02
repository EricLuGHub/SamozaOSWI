from fastapi import APIRouter, Depends, Query

from app.connectors.requests.Connector.ConnectorAuthorizeRequest import ConnectorAuthorizeRequest
from app.connectors.requests.Connector.ConnectorExecuteRequest import ConnectorExecuteRequest
from app.dependencies import get_wis_service
from app.services.wis_service import WorldInterfaceService
from fastapi import BackgroundTasks
connector_router = APIRouter(prefix="", tags=["connectors"])

@connector_router.post("/execute")
async def connector_execute(
        req : ConnectorExecuteRequest,
        wis : WorldInterfaceService = Depends(get_wis_service)):
    res = wis.connector_execute(req)
    return

@connector_router.post("/authorize")
async def connector_authorize(
        req : ConnectorAuthorizeRequest,
        wis : WorldInterfaceService = Depends(get_wis_service)):
    res = wis.auth_connector(req)
    return res

@connector_router.get("/{user_id}/callback")
async def connector_callback(
    user_id: str,
    status: str = Query(...),
    connectedAccountId: str = Query(...),
    appName: str = Query(...),
    wis: WorldInterfaceService = Depends(get_wis_service),
):
    return await wis.handle_connector_callback(
        user_id=user_id,
        status=status,
        connected_account_id=connectedAccountId,
        app_name=appName,
    )

@connector_router.post("/disconnect")
async def connector_disconnect(req : ConnectorAuthorizeRequest, wis : WorldInterfaceService = Depends(get_wis_service)):
    # TODO: just delete the entry from db
    pass