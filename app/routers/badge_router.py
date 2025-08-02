from fastapi import APIRouter, Depends

from app.dependencies import get_badge_service

badge_router = APIRouter(prefix="/components", tags=["components"])

@badge_router.post("/create")
# async def create_badge(badge_id: str, svc: AuthService = Depends(get_badge_service)):
async def create_badge(creator_badge_id: str, svc = Depends(get_badge_service)):
    badge_id  = svc.create_badge(creator_badge_id)
    return {"message": "Badge created successfully", "badge_id": badge_id}




