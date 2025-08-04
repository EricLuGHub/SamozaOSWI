from pydantic import BaseModel

class AddConnectorRequest(BaseModel):
    connector_name: str