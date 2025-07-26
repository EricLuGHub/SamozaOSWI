from contextlib import asynccontextmanager
from starlette.datastructures import State

from fastapi import FastAPI
from .config import Settings
from .services import auth_service, guard_service, wis_service
from .routers import badge_router



settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.settings = settings
    # app.state.auth = auth_service.AuthService()
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

app.include_router(badge_router.router, prefix="/badge", tags=["auth"])
