from abc import ABC, abstractmethod
from typing import Any, Dict


class IConnector(ABC):

    @abstractmethod
    def authenticate(self) -> bool:
        ...

    @abstractmethod
    def execute(self, action: str, payload: object) -> Dict[str, Any]:
        ...


