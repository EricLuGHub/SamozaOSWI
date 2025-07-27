from typing import Dict, Any

from pydantic import BaseModel

class ConnectorExecuteRequest(BaseModel):
    badge_id: str
    connector: str
    action: str
    payload: Dict[str, Any]

