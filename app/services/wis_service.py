from typing import Dict, Any, Type
from fastapi import BackgroundTasks
from app.connectors.BaseConnector import BaseConnector
from app.connectors.ggl_cal_connect import GoogleCalendarConnector
from app.connectors.requests.Connector.ConnectorAuthorizeRequest import ConnectorAuthorizeRequest
from app.connectors.requests.Connector.ConnectorExecuteRequest import ConnectorExecuteRequest
from app.services.composio_service import ComposioService
from app.services.credential_service import CredentialService
from app.services.guard_service import GuardService
import app.connectors as connectors_pkg
import importlib
import pkgutil
import inspect

class WorldInterfaceService:
    def __init__(self,
                 guard: GuardService,
                 composio_service: ComposioService,
                 credential_service: CredentialService):

        self.guard = guard
        self.composio_service = composio_service
        self.available_connectors: Dict[str, Type[BaseConnector]] = {} # todo ::: make this into a factory
        self.credential_service = credential_service

        self._load_available_connectors()


    def _load_available_connectors(self):
        for finder, module_name, is_pkg in pkgutil.iter_modules(connectors_pkg.__path__):
            module = importlib.import_module(f"{connectors_pkg.__name__}.{module_name}")

            for _, cls in inspect.getmembers(module, inspect.isclass):
                if issubclass(cls, BaseConnector) and cls is not BaseConnector:
                    key = cls.connector_name
                    self.available_connectors[key] = cls

    def auth_connector(self, req : ConnectorAuthorizeRequest):


        # todo ::: check if user has permission to add connector
        if req.connector_name not in self.available_connectors:
            return None

        redir = self.composio_service.begin_add_connector(req.connector_name)

        return {"redirect_url": redir}

    async def handle_connector_callback(
            self,
            user_id: str,
            status: str,
            connected_account_id: str,
            app_name: str,
    ) -> Dict[str, Any]:
        ok = self.composio_service.finish_add_connector(
            user_id=user_id,
            service_name=app_name,
            connected_account_id=connected_account_id,
            status=status,
        )
        return {"ok": ok, "userId": user_id, "service": app_name}


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