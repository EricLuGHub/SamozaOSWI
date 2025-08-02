from typing import Dict, Any, Type
from fastapi import BackgroundTasks

from app.DTO.sapDTO import SapDTO
from app.connectors.BaseConnector import BaseConnector
from app.connectors.requests.Connector.ConnectorAuthorizeRequest import ConnectorAuthorizeRequest
from app.connectors.requests.Connector.ConnectorExecuteRequest import ConnectorExecuteRequest
from app.services.composio_service import ComposioService
from app.services.credential_service import CredentialService
from app.services.guard_service import GuardService
import app.connectors as connectors_pkg
import importlib
import pkgutil
import inspect

from app.services.sap_service import SapService


class WorldInterfaceService:
    def __init__(self,
                 guard: GuardService,
                 composio_service: ComposioService,
                 credential_service: CredentialService,
                 sap_service: SapService):

        self.guard = guard
        self.composio_service = composio_service
        self.available_connectors: Dict[str, Type[BaseConnector]] = {} # todo ::: make this into a factory
        self.credential_service = credential_service
        self.sap_service = sap_service

        self.sap_matrix: Dict[str, int] = {} # badge_id -> [permissions]

        self._load_available_connectors()
        self._init_sap_matrix()

    def _init_sap_matrix(self):
        self.sap_matrix = self.sap_service.load_all_permissions()

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

        hasAccess = self.guard.verify_permission(req.badge_id, req.action)

        if not hasAccess:
            return {"error": "You do not have permission to execute this action."}

        creds = self.credential_service.get_credentials(req.user_id, req.connector_name)

        if not creds:
            return {"error": "No credentials found for this connector."}



        connector = self.available_connectors.get(req.connector_name)

        if not connector:
            return None

        new_connector = connector(
            user_id=creds.user_id,
            connection_id=creds.connection_id
        )
        # todo ::: remove this and replace by logic above
        new_connector.execute(req.action, req.payload)

        return None

    def grant_ceio_permissions(self, sap_perm: SapDTO):

        if not sap_perm.badge_id or not sap_perm.ceio_permissions:
            return {"error": "Badge ID and permissions are required."}

        # todo ::: check if badge_id is valid
        res = self.sap_service.grant_permission(sap_perm.badge_id, sap_perm.ceio_permissions)

        self.sap_matrix[res.badge_id] = res.permissions

        return {"result": "sap saved"}