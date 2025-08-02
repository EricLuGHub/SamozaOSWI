from typing import Dict, Any

from pydantic import BaseModel

class ConnectorExecuteRequest(BaseModel):
    badge_id: str
    user_id: str
    connector_name: str
    action: str
    payload: Dict[str, Any]

