from typing import Optional

from pydantic import BaseModel

class CredentialDTO(BaseModel):
    service_name:    Optional[str] = None
    user_id:         Optional[str] = None
    connection_id:   Optional[str] = None
