from abc import ABC, abstractmethod
from typing import Any, Dict
from composio_llamaindex import ComposioToolSet


class BaseConnector:
    connector_name: str
    user_id: str
    connection_id: str
    composio_toolset: ComposioToolSet

    # todo ::: base_composio

    def __init__(self, user_id: str, connection_id: str):
        self.user_id = user_id
        self.connection_id = connection_id

    @abstractmethod
    def execute(self, action: str, payload: dict[str, Any]) -> Dict[str, Any]:
        ...

