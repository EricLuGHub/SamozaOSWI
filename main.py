from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI(title="SamozaOS Dummy Kernel")
# Pydantic models
class Badge(BaseModel):
    badge_id: str
    badge_name: str
    badge_type: str
    validity: bool
    creation_time: str
    is_ephemeral: bool
    validity_time: str

class Credential(BaseModel):
    access_token: str
    refresh_token: str
    provider: str
    badge_id: str
    token_id: str

class SAPEntry(BaseModel):
    id: str
    badge_id: str
    ceio_permissions: List[str]
# Services
class GuardService:
    def __init__(self):
        self.sap_matrix: Dict[str, List[str]] = {}
    def load_permissions(self, manifest_path: str):
        # TODO: load YAML manifest into sap_matrix
        pass
    def verify_permission(self, badge_id: str, permission: str) -> bool:
        return permission in self.sap_matrix.get(badge_id, [])

class AuthService:
    def __init__(self):
        self.badges: Dict[str, Badge] = {}
        self.credentials: Dict[str, Credential] = {}
        self.sap_store: Dict[str, SAPEntry] = {}
    def create_badge(self, badge: Badge) -> Badge:
        self.badges[badge.badge_id] = badge
        return badge
    def refresh_token(self, token_id: str) -> Credential:
        cred = self.credentials.get(token_id)
        if not cred:
            raise HTTPException(status_code=404, detail="Token not found")
        # TODO: implement actual refresh logic
        return cred

class WorldInterfaceService:
    def __init__(self, guard: GuardService, auth_service: AuthService):
        self.guard = guard
        self.auth_service = auth_service
        self.connector_registry: Dict[str, Any] = {}
    def register_connector(self, name: str, connector: Any):
        self.connector_registry[name] = connector
    def perform_action(self, badge_id: str, connector_name: str, action: str, payload: Any):
        if not self.guard.verify_permission(badge_id, action):
            raise HTTPException(status_code=403, detail="Permission denied")
        connector = self.connector_registry.get(connector_name)
        if not connector:
            raise HTTPException(status_code=404, detail="Connector not found")
        return connector.execute(action, payload)

class SamozaEphemeralPoolService:
    def __init__(self):
        self.pool: Dict[str, List[Dict[str, str]]] = {}
    def get_pool(self, provider: str) -> List[Dict[str, str]]:
        return self.pool.get(provider, [])
    def allocate(self, provider: str) -> Dict[str, str]:
        return self.pool[provider].pop()
    def release(self, provider: str, creds: Dict[str, str]):
        self.pool[provider].append(creds)

guard = GuardService()
auth_service = AuthService()
wis = WorldInterfaceService(guard, auth_service)
seps = SamozaEphemeralPoolService()



# Introduction
@app.get("/introduction")
async def introduction():
    return {"description": "SamozaOS dummy kernel implemented as a FastAPI service. Supports badge-based access control, connector orchestration, and ephemeral account management."}

# Components Router
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

# Launch Flow
launch_router = APIRouter(prefix="/launch", tags=["launch"])

@launch_router.post("/initialize")
async def initialize_system():
    guard.load_permissions("permissions.yaml")
    # TODO: load connectors dynamically
    return {"status": "initialized"}

app.include_router(launch_router)

# Storage and Schema Router
storage_router = APIRouter(prefix="/storage", tags=["storage"])

@storage_router.get("/badge-store")
async def badge_store_schema():
    return {"columns": ["badge_id", "badge_name", "badge_type", "validity", "creation_time", "is_ephemeral", "validity_time"]}

@storage_router.get("/credential-vault")
async def credential_vault_schema():
    return {"columns": ["access_token", "refresh_token", "provider", "badge_id", "token_id"]}

@storage_router.get("/sap-store")
async def sap_store_schema():
    return {"columns": ["id", "badge_id", "ceio_permissions"]}

app.include_router(storage_router)

# Connector Request Flow
connector_flow_router = APIRouter(prefix="/connector-flow", tags=["connector-flow"])

@connector_flow_router.post("/request")
async def connector_request(badge_id: str, connector_name: str, action: str, payload: Dict[str, Any]):
    return wis.perform_action(badge_id, connector_name, action, payload)

app.include_router(connector_flow_router)

# Composio Integration Router
composio_router = APIRouter(prefix="/composio", tags=["composio"])

@composio_router.post("/execute")
async def composio_execute(action: Dict[str, Any]):
    # TODO: integrate actual Composio client
    return {"status": "executed", "action": action}

@composio_router.post("/action-mapper")
async def action_mapper(connector: str, action: str):
    mapper = {"gmail.sendEmail": ["O"], "slack.postMessage": ["O", "I"]}
    return {"permissions": mapper.get(f"{connector}.{action}", [])}

app.include_router(composio_router)

# Misc Operations Router
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

@ephemeral_router.get("/pool/{provider}")
async def get_ephemeral_pool(provider: str):
    return seps.get_pool(provider)

@ephemeral_router.post("/lifecycle/setup")
async def setup_ephemeral(badge_id: str, provider: str):
    if not guard.verify_permission(badge_id, "C"):
        raise HTTPException(status_code=403, detail="No permission for ephemeral")
    creds = seps.allocate(provider)
    auth_service.credentials[creds["token_id"]] = Credential(**creds)
    # TODO: update SAP matrix and database
    return creds

@ephemeral_router.delete("/lifecycle/discard/{token_id}")
async def discard_ephemeral(token_id: str):
    cred = auth_service.credentials.pop(token_id, None)
    if not cred:
        raise HTTPException(status_code=404, detail="Credential not found")
    # TODO: notify WIS and SEPS
    return {"status": "discarded"}

app.include_router(ephemeral_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8122)