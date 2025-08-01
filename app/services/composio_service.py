import uuid
from composio_llamaindex import ComposioToolSet, App
from app.DTO.CredentialDTO import Credential
from composio.client.collections import ConnectionRequestModel


class ComposioService:
    def __init__(self):
        self.composio_toolset: ComposioToolSet = ComposioToolSet()

    def begin_add_connector(self, connector_name : str) -> (ConnectionRequestModel, str):

        new_user_id = str(uuid.uuid4())
        entity = self.composio_toolset.get_entity(id=new_user_id)
        conn_req = entity.initiate_connection(app_name=connector_name)
        return conn_req, new_user_id


    def finish_connector(self, conn_req, user_id: str, service_name: str)->Credential:
        try:
            active = conn_req.wait_until_active(client=self.composio_toolset.client,
                                                timeout=120)
            return Credential(
                connection_id=active.id,
                user_id=user_id,
                service_name=service_name,
                access_token=active.access_token,
                refresh_token=active.refresh_token
            )

        except Exception as e:
            print(e)
            return None
