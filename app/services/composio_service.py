import uuid
from composio_llamaindex import ComposioToolSet, App
from app.DTO.CredentialDTO import Credential
from composio.client.collections import ConnectionRequestModel

from app.services.credential_service import CredentialService


class ComposioService:
    def __init__(self, credential_service: CredentialService):
        self.composio_toolset: ComposioToolSet = ComposioToolSet()
        self.credential_service = credential_service

    def begin_add_connector(self, connector_name : str) -> str:

        new_user_id = str(uuid.uuid4())
        entity = self.composio_toolset.get_entity(id=new_user_id)
        conn_req = entity.initiate_connection(
            app_name=connector_name,
            redirect_url=f"http://localhost:8211/connect/{new_user_id}/callback") # Todo ::: make this dynamic

        return conn_req.redirectUrl

    def finish_add_connector(
            self,
            user_id: str,
            service_name: str,
            connected_account_id: str,
            status: str,
    ) -> bool:

        if status.lower() != "success":
            return False
        creds = Credential(
            connection_id=connected_account_id,
            user_id=user_id,
            service_name=service_name.upper(),
            access_token=None,
            refresh_token=None,
        )
        self.credential_service.add_credential(creds)
        return True
