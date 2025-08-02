from sqlalchemy.orm import Session

from app.DTO.badgeDTO import BadgeDTO
from app.models.badgeORM import BadgeORM


class BadgeService:

    def __init__(self, db: Session):
        self.db = db

    def get_badge(self, user_id: str, service_name: str):

        return None

    def create_badge(self, badge: BadgeDTO)-> int:
        badge_orm = BadgeORM(
            badge_name=badge.badge_name,
            badge_type=badge.badge_type,
            is_valid=badge.validity,
            validity_period=badge.validity_time,
            is_ephemeral=badge.is_ephemeral,
        )

        self.db.add(badge_orm)
        self.db.commit()
        self.db.refresh(badge_orm)

        return badge_orm.badge_id
