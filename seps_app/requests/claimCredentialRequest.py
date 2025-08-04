from pydantic import BaseModel

class ClaimCredentialRequest(BaseModel):
    connector_name: str