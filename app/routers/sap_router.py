from fastapi import APIRouter, Depends

from app.DTO.badgeDTO import BadgeDTO
from app.dependencies import get_badge_service
from app.services.badge_service import BadgeService

sap_router = APIRouter(prefix="", tags=[])

@sap_router.post("/create")
async def grant_permission(new_badge : BadgeDTO, svc: BadgeService = Depends(get_badge_service)):
    badge_id  = svc.create_badge(new_badge)
    return {"badge_id": badge_id}

