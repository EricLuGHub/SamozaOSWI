from fastapi import APIRouter, Depends

from app.dependencies import get_badge_service
from app.services.badge_service import BadgeService

badge_router = APIRouter(prefix="/components", tags=["components"])

@badge_router.post("/add")
async def create_badge(creator_badge_id: str, svc: BadgeService = Depends(get_badge_service)):
    badge_id  = svc.add_badge(creator_badge_id)
    return {"message": "Badge created successfully", "badge_id": badge_id}

@badge_router.post("/launch")
# async def create_badge(badge_id: str, svc: AuthService = Depends(get_badge_service)):
async def create_badge(creator_badge_id: str, svc = Depends(get_badge_service)):
    badge_id  = svc.create_badge(creator_badge_id)
    return {"message": "Badge created successfully", "badge_id": badge_id}




