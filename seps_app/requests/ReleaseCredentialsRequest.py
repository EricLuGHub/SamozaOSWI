from pydantic import BaseModel

class ReleaseCredentialsRequest(BaseModel):
    user_id: str