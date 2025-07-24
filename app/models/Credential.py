from pydantic import BaseModel


class Credential(BaseModel):
    access_token: str
    refresh_token: str
    provider: str
    badge_id: str
    token_id: str