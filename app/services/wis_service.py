from http.client import HTTPException
from typing import Dict, Any


class WorldInterfaceService:
    def __init__(self, guard: GuardService, auth_service: AuthService):
        self.guard = guard
        self.auth_service = auth_service
        self.connector_registry: Dict[str, Any] = {}
    def register_connector(self, name: str, connector: Any):
        self.connector_registry[name] = connector
    def perform_action(self, badge_id: str, connector_name: str, action: str, payload: Any):
        if not self.guard.verify_permission(badge_id, action):
            raise HTTPException(status_code=403, detail="Permission denied")
        connector = self.connector_registry.get(connector_name)
        if not connector:
            raise HTTPException(status_code=404, detail="Connector not found")
        return connector.execute(action, payload)