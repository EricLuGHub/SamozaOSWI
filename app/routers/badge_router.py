from fastapi import APIRouter, Depends

from app.DTO.badgeDTO import BadgeDTO
from app.dependencies import get_badge_service
from app.services.badge_service import BadgeService

badge_router = APIRouter(prefix="", tags=["components"])

@badge_router.post("/create")
async def create_badge(new_badge : BadgeDTO, svc: BadgeService = Depends(get_badge_service)):
    badge_id  = svc.create_badge(new_badge)
    return {"badge_id": badge_id}





