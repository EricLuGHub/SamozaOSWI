import uuid

from composio_llamaindex import ComposioToolSet, App

from app.models.credential import Credential


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

                credential = Credential()

                credential.service_name = connector_name
                credential.user_id = new_user_id
                credential.connector_id = active_connection.id
                credential.access_token = active_connection.access_token
                credential.refresh_token = active_connection.refresh_token

                return credential
            except Exception as e:
                print(f"Error waiting for connection: {e}")

        return None
