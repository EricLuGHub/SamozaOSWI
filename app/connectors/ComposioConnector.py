from typing import Any, Dict

from app.connectors.BaseConnector import BaseConnector
from composio_llamaindex import ComposioToolSet, Action


class ComposioConnector(BaseConnector):
    connector_name = "composio"

    def __init__(self, user_id: str = None, connection_id: str = None):
        super().__init__(user_id, connection_id)


    def execute(self, action: str, payload: Dict[str, Any]) -> object:

        toolset = ComposioToolSet()
        result = toolset.execute_action(
            action=Action(value=action),
            params=payload,
            entity_id=self.user_id,
            connected_account_id=self.connection_id
        )

        return result


