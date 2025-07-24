from fastapi import APIRouter

from app.services import auth_service

components_router = APIRouter(prefix="/components", tags=["components"])

@components_router.get("/badges")
async def get_badges():
    return list(auth_service.badges.values())

@components_router.get("/guard")
async def get_guard_status():
    return {"sap_matrix": guard.sap_matrix}

@components_router.get("/connectors")
async def list_connectors():
    return list(wis.connector_registry.keys())

@components_router.get("/world-interface-service")
async def get_wis_status():
    return {"connectors": list(wis.connector_registry.keys())}

@components_router.get("/auth-service")
async def get_auth_status():
    return {"badges": len(auth_service.badges), "credentials": len(auth_service.credentials)}

app.include_router(components_router)

app.include_router(wi_router)

ops_router = APIRouter(tags=["operations"])

@ops_router.post("/connectors/add")
async def add_connector(name: str):
    wis.register_connector(name, object())
    return {"status": f"connector {name} added"}

@ops_router.post("/badges/create", response_model=Badge)
async def create_badge(badge: Badge):
    return auth_service.create_badge(badge)

@ops_router.post("/tokens/refresh")
async def refresh_token(token_id: str):
    return auth_service.refresh_token(token_id)

app.include_router(ops_router)

# Ephemeral Accounts Router
ephemeral_router = APIRouter(prefix="/ephemeral", tags=["ephemeral"])

@ephemeral_router.delete("/lifecycle/discard/{token_id}")
async def discard_ephemeral(token_id: str):
    cred = auth_service.credentials.pop(token_id, None)
    if not cred:
        raise HTTPException(status_code=404, detail="Credential not found")
    # TODO: notify WIS and SEPS
    return {"status": "discarded"}

app.include_router(ephemeral_router)
