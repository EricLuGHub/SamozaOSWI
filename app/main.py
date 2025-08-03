from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm.session import sessionmaker

from app.config import Settings
from app.db import SQLALCHEMY_DATABASE_URL, SessionLocal, Base, engine
from app.routers.connect_router import connector_router
from app.routers.sap_router import sap_router
from app.services.badge_service import BadgeService
from app.services.composio_service import ComposioService
from app.services.credential_service import CredentialService
from app.services.guard_service import GuardService
from app.services.sap_service import SapService
from app.services.wis_service import WorldInterfaceService
from app.routers.badge_router import badge_router

settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):


    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    app.state.db = db

    app.state.settings = settings
    app.state.guard = GuardService()
    app.state.credential_service = CredentialService(db)
    app.state.composio_service = ComposioService(
        app.state.credential_service
    )
    app.state.badge_service = BadgeService(db)
    app.state.sap_service = SapService(db)

    app.state.wis = WorldInterfaceService(app.state.guard,
                                          app.state.composio_service,
                                          app.state.credential_service,
                                          app.state.sap_service)

    yield

    db.close()

app = FastAPI(
    title="SamozaOS World Interface",
    lifespan=lifespan,
)


app.include_router(badge_router, prefix="/badge", tags=[])
app.include_router(connector_router, prefix="/connect", tags=[])
app.include_router(sap_router, prefix="/sap", tags=[])

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
