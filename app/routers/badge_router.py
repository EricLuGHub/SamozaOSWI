from fastapi import APIRouter, Depends

from app.dependencies import get_auth_service
from app.services import auth_service
from app.services.auth_service import AuthService

components_router = APIRouter(prefix="/components", tags=["components"])

@components_router.get("/badges")
async def get_badges(svc: AuthService = Depends(get_auth_service)):
    return list(svc.badges.values())



