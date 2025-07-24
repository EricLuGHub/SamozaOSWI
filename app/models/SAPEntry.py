from typing import List

from pydantic import BaseModel


class SAPEntry(BaseModel):
    id: str
    badge_id: str
    ceio_permissions: List[str]