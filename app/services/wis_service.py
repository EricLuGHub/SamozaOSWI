from typing import Dict, Any, Type
from fastapi import Depends
from app.connectors.BaseConnector import BaseConnector
from app.connectors.ggl_cal_connect import GoogleCalendarConnector
from app.connectors.requests.Connector.ConnectorAuthorizeRequest import ConnectorAuthorizeRequest
from app.connectors.requests.Connector.ConnectorExecuteRequest import ConnectorExecuteRequest
from app.services.composio_service import ComposioService
from app.services.credential_service import CredentialService
from app.services.guard_service import GuardService


class WorldInterfaceService:
    def __init__(self,
                 guard: GuardService,
                 composio_service: ComposioService,
                 credential_service: CredentialService):

        self.guard = guard
        self.composio_service = composio_service
        self.available_connectors: Dict[str, Type[BaseConnector]] = {} # todo ::: make this into a factory
        self.credential_service = credential_service


    def _load_connectors(self):
        pass

    def auth_connector(self, req : ConnectorAuthorizeRequest):


        # todo ::: check if user has permission to add connector

        if req.connector_name not in self.available_connectors:
            return None

        creds = self.composio_service.add_connector(req.connector_name)

        if not creds:
            return None

        self.credential_service.add_credential(creds)



        # todo ::: register connector in db
        return None

    def connector_execute(self, req: ConnectorExecuteRequest):

        creds = self.guard.verify_permission(req.badge_id, req.action)

        if not creds:
            return None

        connector = self.connector_registry.get(req.connector_name)

        if not connector:
            return None

        # create connector
        # new_connector = connector(creds)
        # new_connector.execute(creds.api_key, creds.entity_id)

        # todo ::: remove this and replace by logic above
        connector.execute(req.action, req.payload)

        return None