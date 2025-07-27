from http.client import HTTPException
from typing import Dict, Any, Type

from app.connectors.Connectable import BaseConnector
from app.connectors.ggl_cal_connect import GoogleCalendarConnector
from app.connectors.requests.Connector.ConnectorAuthorizeRequest import ConnectorAuthorizeRequest
from app.connectors.requests.Connector.ConnectorExecuteRequest import ConnectorExecuteRequest
from app.services.guard_service import GuardService


class WorldInterfaceService:
    def __init__(self, guard: GuardService):
        self.guard = guard
        self.available_connectors: Dict[str, Type[BaseConnector]] = {} # todo ::: make this into a factory
        self.connector_registry: Dict[str, BaseConnector] = {}

        # todo ::: load available connectors and remove below
        self.connector_registry["google_calendar"] = GoogleCalendarConnector()



    def auth_connector(self, req : ConnectorAuthorizeRequest):

        if req.connector_name not in self.available_connectors:
            return None

        connector = self.available_connectors[req.connector_name]
        self.connector_registry[req.connector_name] = connector(req.api_key, req.user_id)
        # todo ::: register connector in db
        return None

    def connector_execute(self, req: ConnectorExecuteRequest):

        if not self.guard.verify_permission(req.badge_id, req.action):
            return None

        connector = self.connector_registry.get(req.connector)

        if not connector:
            return None

        return connector.execute(req.action, req.payload)