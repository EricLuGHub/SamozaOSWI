import uuid

from composio_llamaindex import ComposioToolSet, App

class ComposioService:
    def __init__(self):
        self.composio_toolset: ComposioToolSet = ComposioToolSet()

    def add_connector(self, connector_name) -> (str, str):



        app_to_connect = App[connector_name]
        if not app_to_connect:
            return None

        new_user_id = str(uuid.uuid4())

        entity = self.composio_toolset.get_entity(id=new_user_id)
        



        return None
