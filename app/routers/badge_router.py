from fastapi import APIRouter, Depends

from app.dependencies import get_auth_service, get_badge_service
from app.services import auth_service
from app.services.auth_service import AuthService

badge_router = APIRouter(prefix="/components", tags=["components"])

@badge_router.post("/create-badge")
async def create_badge(badge_id: str, svc: AuthService = Depends(get_badge_service)):
    if badge_id in svc.badges:
        return {"error": "Badge already exists"}
    svc.create_badge(badge_id)
    return {"message": "Badge created successfully", "badge_id": badge_id}




