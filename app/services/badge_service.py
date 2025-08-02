from sqlalchemy.orm import Session

from app.DTO.badgeDTO import BadgeDTO


class BadgeService:

    def __init__(self, db: Session):
        self.db = db

    def get_badge(self, user_id: str, service_name: str):

        return None

    def add_badge(self, badge: BadgeDTO):
        badge_orm = BadgeDTO(**badge.model_dump())
        self.db.add(badge_orm)
        self.db.commit()
        self.db.refresh(badge_orm)
        return badge_orm
