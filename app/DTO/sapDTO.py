from typing import List

from pydantic import BaseModel


class SapDTO(BaseModel):
    badge_id: int
    ceio_permissions: List[str]