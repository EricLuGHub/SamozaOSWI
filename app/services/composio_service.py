import uuid
from composio_llamaindex import ComposioToolSet, App
from app.DTO.CredentialDTO import Credential


class ComposioService:
    def __init__(self):
        self.composio_toolset: ComposioToolSet = ComposioToolSet()

    def add_connector(self, connector_name : str) -> Credential:

        new_user_id = str(uuid.uuid4())
        entity = self.composio_toolset.get_entity(id=new_user_id)

        connection_request = entity.initiate_connection(app_name=connector_name)

        if connection_request.redirectUrl:
            try:
                active_connection = connection_request.wait_until_active(
                    client=self.composio_toolset.client,
                    timeout=120
                )

                return Credential(
                    connection_id=active_connection.id,
                    user_id=new_user_id,
                    service_name=connector_name,

                    access_token=active_connection.access_token,
                    refresh_token=active_connection.refresh_token
                )
            
            except Exception as e:
                print(f"Error waiting for connection: {e}")

        return None
