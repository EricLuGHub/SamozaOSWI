import uuid
from composio_llamaindex import ComposioToolSet, App

from seps_app.db import SEPS_ENDPOINT
from seps_app.services.credential_service import CredentialService


class ComposioService:
    def __init__(self, credential_service: CredentialService):
        self.composio_toolset: ComposioToolSet = ComposioToolSet()
        self.credential_service = credential_service

    def begin_add_connector(self, connector_name : str) -> str:

        new_user_id = str(uuid.uuid4())
        entity = self.composio_toolset.get_entity(id=new_user_id)
        conn_req = entity.initiate_connection(
            app_name=connector_name,
            redirect_url=f"{SEPS_ENDPOINT}/credentials/{new_user_id}/callback") # Todo ::: make this dynamic

        return conn_req.redirectUrl
