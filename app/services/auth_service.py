from http.client import HTTPException
from typing import Dict

from app.models.Credential import Credential
from app.models.SAPEntry import SAPEntry
from app.models.badge import Badge


class AuthService:
    def __init__(self):
        self.badges: Dict[str, Badge] = {}

    def create_badge(self, badge: Badge) -> Badge:
        self.badges[badge.badge_id] = badge
        return badge

