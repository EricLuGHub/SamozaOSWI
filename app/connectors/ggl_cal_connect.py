from typing import Any, Dict

from app.connectors.BaseConnector import BaseConnector
from composio_llamaindex import ComposioToolSet, Action


class GoogleCalendarConnector(BaseConnector):
    connector_name = "GOOGLECALENDAR"

    def __init__(self, api_key: str = None, entity_id: str = None):
        super().__init__(api_key, entity_id)

        if api_key and entity_id:
            self.authenticate(api_key, entity_id)

    def execute(self, action: str, payload: Dict[str, Any]) -> None:


        if self.composio_toolset is None:
            return None

        if action == "GOOGLECALENDAR_CREATE_EVENT":
            self.ggl_cal_create_event(payload)

        elif action == "GOOGLECALENDAR_DUPLICATE_EVENT":
            pass

        else:
            return None

        return None


    def authenticate(self, api_key: str, user_id: str = "default") -> None:
        super().authenticate(api_key,user_id)

    def ggl_cal_create_event(self, payload: Dict[str, Any]) -> None:
        # todo ::: add some kind of verifier for the object
        result = self.composio_toolset.execute_action(
            action=Action(value="GOOGLECALENDAR_CREATE_EVENT"),
            params = payload)

        print(result)

