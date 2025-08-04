from pydantic import BaseModel

class ClaimCredentialRequest(BaseModel):
    service_name: str