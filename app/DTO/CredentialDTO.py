from typing import Optional

from pydantic import BaseModel

class Credential(BaseModel):
    service_name:    Optional[str] = None
    is_bot:          bool           = False
    user_id:         Optional[str] = None
    connection_id:   Optional[str] = None
    access_token:    Optional[str] = None
    refresh_token:   Optional[str] = None