from pydantic import BaseModel

class ConnectorAuthorizeRequest(BaseModel):
    connector_name: str
    badge_id: int