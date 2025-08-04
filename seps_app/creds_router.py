from fastapi import APIRouter, Depends, Query

from seps_app.CredentialDTO import CredentialDTO
from seps_app.dependencies import get_composio_service, get_credential_service
from seps_app.requests.addConnectorRequest import AddConnectorRequest
from seps_app.requests.claimCredentialRequest import ClaimCredentialRequest
from seps_app.services.composio_service import ComposioService
from seps_app.services.credential_service import CredentialService

creds_router = APIRouter(prefix="", tags=[])

@creds_router.post("/add")
async def add_credential(new_connector : AddConnectorRequest, svc: ComposioService = Depends(get_composio_service)):
    # todo::: check if connector name exists
    res  = svc.begin_add_connector(new_connector.connector_name)
    return res


@creds_router.get("/{user_id}/callback")
async def connector_callback(
    user_id: str,
    status: str = Query(...),
    connectedAccountId: str = Query(...),
    appName: str = Query(...),
    svc: CredentialService = Depends(get_credential_service),
):
    cred = CredentialDTO(
        connection_id=connectedAccountId,
        user_id=user_id,
        service_name=appName.upper(),
        access_token=None,
        refresh_token=None,
    )

    return {"response": "success"}


@creds_router.post("/claim-creds")
async def claim_cred(new_badge : ClaimCredentialRequest, svc: CredentialService = Depends(get_credential_service)):
    badge_id  = svc.claim_credentials(new_badge)
    return {"badge_id": badge_id}


@creds_router.get("/release")
async def release_cred(
    user_id: str,
    svc: CredentialService = Depends(get_credential_service),
):
    res = svc.release_credentials(user_id)
    return {"response": "success" if res else "failure"}



