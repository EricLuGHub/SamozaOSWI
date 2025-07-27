from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.config import Settings
from app.services.wis_service import WorldInterfaceService

settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.settings = settings
    app.state.wis = WorldInterfaceService
    # app.state.guard = guard_service.GuardService()


    #startup flow
    # initialize db connection here

    yield
    # shut down logic here
    # close db

app = FastAPI(
    title="SamozaOS World Interface",
    lifespan=lifespan,
)

from .routers import badge_router

app.include_router(badge_router.badge_router, prefix="/badge", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Hello"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=True,
    )
