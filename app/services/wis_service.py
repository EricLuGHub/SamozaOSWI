from typing import Dict, Any, Type
import requests

from app.Constants.ActionPermissionMapper import ActionToPermissionMapper
from app.Constants.Permissions import WisActions
from app.DTO.credentialDTO import CredentialDTO
from app.DTO.sapDTO import SapDTO
from app.connectors.BaseConnector import BaseConnector
from app.connectors.ComposioConnector import ComposioConnector
from app.connectors.requests.Connector.ConnectorAuthorizeRequest import ConnectorAuthorizeRequest
from app.connectors.requests.Connector.ConnectorExecuteRequest import ConnectorExecuteRequest
from app.connectors.requests.Ephemeral.ephConnectorRequest import EphConnectorRequest
from app.services.composio_service import ComposioService
from app.services.credential_service import CredentialService
import app.connectors as connectors_pkg
import importlib
import pkgutil
import inspect

from app.services.sap_service import SapService


class WorldInterfaceService:
    def __init__(self,
                 composio_service: ComposioService,
                 credential_service: CredentialService,
                 sap_service: SapService):

        self.composio_service = composio_service
        self.available_connectors: Dict[str, Type[BaseConnector]] = {}
        self.credential_service = credential_service
        self.sap_service = sap_service

        self.sap_matrix: Dict[int, int] = {} # badge_id -> [permissions]

        self._load_available_connectors()
        self._init_sap_matrix()


    def _has_permission(self, badge_id: int, required_permission: int) -> bool:
        badge_mask = self.sap_matrix.get(badge_id, 0)
        return bool(badge_mask & required_permission)

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

        if not self._has_permission(req.badge_id, WisActions.AUTH_CONNECTOR):
            return {"error": "You do not have permission to add this connector."}

        # if req.connector_name not in self.available_connectors:
        #     return None

        reDir, user_id = self.composio_service.begin_add_connector(req.connector_name)

        return {"redirect_url": reDir, "user_id": user_id }

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

        action_perm = ActionToPermissionMapper.get(req.action)
        if action_perm is None:
            return {"error": f"No CEIO mapping for action '{req.action}'"}

        required = WisActions.CONNECTOR_EXECUTE | action_perm

        if not self._has_permission(req.badge_id, required):
            return {"error": "You do not have permission to execute this action."}


        creds = self.credential_service.get_credentials(req.user_id, req.connector_name)

        if not creds:
            return {"error": "No credentials found for this connector."}

        new_connector = ComposioConnector(
            user_id=creds.user_id,
            connection_id=creds.connection_id
        )

        res = new_connector.execute(req.action, req.payload)
        return res

    def grant_ceio_permissions(self, sap_perm: SapDTO):
        if not self._has_permission(sap_perm.master_badge_id, WisActions.GRANT_CEIO_PERMISSIONS):
            return {"error": "You do not have permission to grant CEIO permissions."}

        if not sap_perm.badge_id or not sap_perm.ceio_permissions:
            return {"error": "Badge ID and permissions are required."}

        if not self.badge_service.validate():
            return {"error": "Invalid badge ID."}

        res = self.sap_service.grant_permission(sap_perm.badge_id, sap_perm.ceio_permissions)

        self.sap_matrix[res.badge_id] = res.permissions

        return {"result": "sap saved"}

    def req_eph_creds(self, eph_req: EphConnectorRequest) -> str:
        resp = requests.post(
            "http://localhost:8222/credentials/claim-creds",
            json={"service_name": eph_req.service_name}
        )
        resp.raise_for_status()
        payload = resp.json()
        user_id = payload["user_id"]
        connection_id = payload["connection_id"]

        new_creds = CredentialDTO(
            service_name=eph_req.service_name,
            user_id=user_id,
            connection_id=connection_id,
            is_bot=True,
        )

        self.credential_service.add_credential(new_creds)

        return user_id

    def discord_eph_creds(self, eph_req: EphConnectorRequest) -> bool:

        self.credential_service.delete_credential(eph_req.user_id)
        resp = requests.post(
            "http://localhost:8222/credentials/release",
            json={"user_id": eph_req.user_id}
        )

        resp.raise_for_status()
        payload = resp.json()
        return payload.get("ok", False) == "ok"