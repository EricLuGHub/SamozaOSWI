import random
from typing import Optional

from sqlalchemy.orm import Session

from seps_app.DTO.credentialDTO import CredentialDTO
from seps_app.credentialORM import CredentialORM


class CredentialService:
    def __init__(self, db : Session):
        self.db = db

    def claim_credentials(self, service_name: str) -> Optional[CredentialORM]:
        creds = (
            self.db
            .query(CredentialORM)
            .filter_by(service_name=service_name, is_used=False)
            .all()
        )
        if not creds:
            return None
        cred = random.choice(creds)
        cred.is_used = True
        self.db.commit()
        self.db.refresh(cred)
        return cred

    def release_credentials(self, user_id) -> bool:
        cred = (
            self.db
            .query(CredentialORM)
            .filter_by(user_id=user_id)
            .first()
        )
        if not cred:
            return False
        cred.is_used = False
        self.db.commit()
        return True

    def add_credential(self, cred: CredentialDTO) -> CredentialORM:
        existing = (
            self.db.query(CredentialORM)
            .filter_by(user_id=cred.user_id)
            .first()
        )
        if existing:
            return None

        cred_orm = CredentialORM(**cred.model_dump())
        self.db.add(cred_orm)
        self.db.commit()
        self.db.refresh(cred_orm)
        return cred_orm

