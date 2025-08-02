from typing import List, Optional, Dict

from app.models.sapORM import SapORM
from app.utils.sap_functions import ceio_to_int


# TODO::: move this?



class SapService:
    def __init__(self, db):
        self.db = db

    def load_all_permissions(self) -> Dict[int, int]:
        rows = self.db.query(SapORM).all()
        return {row.badge_id: row.permissions for row in rows}


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
