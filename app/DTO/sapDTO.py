from typing import List

from pydantic import BaseModel


class SapDTO(BaseModel):
    master_badge_id: int
    badge_id: int
    ceio_permissions: List[str]