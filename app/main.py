from fastapi import FastAPI

app = FastAPI(title="SamozaOS Dummy Kernel")
# Pydantic models

guard = GuardService()
auth_service = AuthService()
wis = WorldInterfaceService(guard, auth_service)
seps = SamozaEphemeralPoolService()

@app.get("/")
async def introduction():
    return {"description": "SamozaOS dummy kernel implemented as a FastAPI service. Supports badge-based access control, connector orchestration, and ephemeral account management."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8122)