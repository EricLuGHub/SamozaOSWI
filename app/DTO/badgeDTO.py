from typing import Optional
from pydantic import BaseModel
from datetime import timedelta

class BadgeDTO(BaseModel):
    badge_name: Optional[str] = None
    badge_type: Optional[str] = None
    validity: Optional[bool] = None
    is_ephemeral: Optional[bool] = None
    validity_time: Optional[timedelta] = None