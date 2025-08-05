from pydantic import BaseModel

class EphConnectorRequest(BaseModel):
    service_name: str