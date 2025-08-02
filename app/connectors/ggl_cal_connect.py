from typing import Any, Dict

from app.connectors.BaseConnector import BaseConnector
from composio_llamaindex import ComposioToolSet, Action


class GoogleCalendarConnector(BaseConnector):
    connector_name = "GOOGLECALENDAR"

    def __init__(self, user_id: str = None, connection_id: str = None):
        super().__init__(user_id, connection_id)


    def execute(self, action: str, payload: Dict[str, Any]) -> None:

        if not action or not payload or not self.user_id or not self.connection_id:
            return None

        if action == "GOOGLECALENDAR_CREATE_EVENT":
            self.ggl_cal_create_event(payload)

        elif action == "GOOGLECALENDAR_DUPLICATE_EVENT":
            pass

        else:
            return None

        return None

    def ggl_cal_create_event(self, payload: Dict[str, Any]) -> None:
        # todo ::: add some kind of verifier for the object
        toolset = ComposioToolSet()
        result = toolset.execute_action(
            action=Action(value="GOOGLECALENDAR_CREATE_EVENT"),
            params = payload,
            entity_id=self.user_id,
            connected_account_id=self.connection_id
        )

        print(result)

