from typing import Dict, Any

from pydantic import BaseModel

class ConnectorExecuteRequest(BaseModel):
    badge_id: int
    user_id: str
    connector_name: str
    action: str
    payload: Dict[str, Any]

