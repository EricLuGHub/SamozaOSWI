from fastapi import APIRouter, Depends
from app.DTO.sapDTO import SapDTO
from app.dependencies import get_wis_service
from app.services.wis_service import WorldInterfaceService

sap_router = APIRouter(prefix="", tags=[])

@sap_router.post("/grant")
async def grant_permission(sap_perm : SapDTO, svc: WorldInterfaceService = Depends(get_wis_service)):
    badge_id  = svc.grant_ceio_permissions(sap_perm)
    return {"badge_id": badge_id}

