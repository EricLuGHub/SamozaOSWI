from contextlib import asynccontextmanager

from fastapi import FastAPI

from seps_app.services.composio_service import ComposioService
from seps_app.services.credential_service import CredentialService
from seps_app.config import Settings
from seps_app.db import Base, engine, SessionLocal
from seps_app.creds_router import creds_router

settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):


    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    app.state.db = db

    app.state.settings = settings
    app.state.credential_service = CredentialService(db)
    app.state.composio_service = ComposioService(
        app.state.credential_service
    )

    yield

    db.close()

app = FastAPI(
    title="Samoza Ephemeral Pool Service",
    lifespan=lifespan,
)


app.include_router(creds_router, prefix="/credentials", tags=[])

@app.get("/")
async def root():
    return {"message": "Hello from SEPS!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "seps_app.main:app",
        host=settings.host,
        port=settings.port_seps,
        reload=True,
    )
