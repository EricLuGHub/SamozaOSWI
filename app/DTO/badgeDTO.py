from typing import Optional
from pydantic import BaseModel

class BadgeDTO(BaseModel):
    badge_id: Optional[str] = None
    badge_name: Optional[str] = None
    badge_type: Optional[str] = None
    validity: Optional[bool] = None
    creation_time: Optional[str] = None
    is_ephemeral: Optional[bool] = None
    validity_time: Optional[str] = None