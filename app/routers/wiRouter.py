from fastapi import APIRouter

wi_router = APIRouter(prefix="/wi", tags=["connector-flow"])

@wi_router.post("/request")
async def connector_request(badge_id: str, connector_name: str, action: str, payload: Dict[str, Any]):
    return wis.perform_action(badge_id, connector_name, action, payload)

