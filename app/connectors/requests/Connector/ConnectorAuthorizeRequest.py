from pydantic import BaseModel

class ConnectorAuthorizeRequest(BaseModel):
    connector_name: str