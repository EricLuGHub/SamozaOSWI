from abc import ABC, abstractmethod
from typing import Any, Dict
from composio_llamaindex import ComposioToolSet


class BaseConnector:
    connector_name: str
    api_key: str
    entity_id: str
    composio_toolset: ComposioToolSet

    def __init__(self, api_key: str, entity_id: str):
        self.api_key = api_key
        self.entity_id = entity_id




    @abstractmethod
    def authenticate(self, api_key: str, user_id: str="default") -> None:
        # todo ::: find way to check/validate creds
        self.composio_toolset = ComposioToolSet(api_key, user_id)

    @abstractmethod
    def execute(self, action: str, payload: dict[str, Any]) -> Dict[str, Any]:
        ...

