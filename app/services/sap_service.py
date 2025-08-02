from typing import List, Optional

from app.models.sapORM import SapORM

# TODO::: move this?

_CEIO_MAP = {
    "c":       1 << 0,   # 1
    "e":      1 << 1,   # 2
    "i": 1 << 2,   # 4
    "o":      1 << 3,   # 8
}

def ceio_to_int(permissions: List[str]) -> int:

    mask = 0
    for p in permissions:
        bit = _CEIO_MAP.get(p.lower())
        if bit:
            mask |= bit
    return mask

class SapService:
    def __init__(self, db):
        self.db = db


    def grant_permission(self, badge_id: int, permissions: List[str]):

        mask = ceio_to_int(permissions)

        sap_entry: Optional[SapORM] = (
            self.db.query(SapORM)
            .filter_by(badge_id=badge_id)
            .first()
        )

        if sap_entry:
            sap_entry.permissions = mask
        else:
            sap_entry = SapORM(
                badge_id=badge_id,
                permissions=mask
            )
            self.db.add(sap_entry)

        self.db.commit()
        self.db.refresh(sap_entry)
        return sap_entry
