from http.client import HTTPException
from typing import Dict, Any

from app.connectors.Connectable import BaseConnector
from app.connectors.requests.Connector.ConnectorExecuteRequest import ConnectorExecuteRequest
from app.services.guard_service import GuardService


class WorldInterfaceService:
    def __init__(self, guard: GuardService):
        self.guard = guard
        self.connector_registry: Dict[str, BaseConnector] = {}

    def register_connector(self, name: str, connector: Any):
        self.connector_registry[name] = connector

    def connector_execute(self, payload: ConnectorExecuteRequest):

        if not self.guard.verify_permission(payload.badge_id, payload.action):
            raise HTTPException(status_code=403, detail="Permission denied")

        connector = self.connector_registry.get(connector_name)
        if not connector:
            raise HTTPException(status_code=404, detail="Connector not found")
        return connector.execute(action, payload)