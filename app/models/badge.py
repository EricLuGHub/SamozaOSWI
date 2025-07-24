from pydantic import BaseModel


class Badge(BaseModel):
    badge_id: str
    badge_name: str
    badge_type: str
    validity: bool
    creation_time: str
    is_ephemeral: bool
    validity_time: str