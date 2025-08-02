from typing import Optional

from sqlalchemy.orm import Session
from app.models.credentialORM import CredentialORM
from app.DTO.credentialDTO import CredentialDTO

class CredentialService:
    def __init__(self, db : Session):
        self.db = db

    def get_credentials(self, user_id, service_name) -> Optional[CredentialORM]:
        """
        Retrieves credentials for a given user.
        """
        return (self.db.query(CredentialORM)
                .filter_by(user_id=user_id, service_name=service_name)
                .first())

    def add_credential(self, cred: CredentialDTO) -> CredentialORM:
        cred_orm = CredentialORM(**cred.model_dump()) # TODO ::: mapper maybe?
        self.db.add(cred_orm)
        self.db.commit()
        self.db.refresh(cred_orm)
        return cred_orm

    def delete_credential(self, user_id, service_name) -> bool:
        """
        Deletes a credential for a user.
        """
        cred = (
            self.db
            .query(CredentialORM)
            .filter_by(user_id=user_id, service_name=service_name)
            .first()
        )
        if not cred:
            return False

        self.db.delete(cred)
        self.db.commit()
        return True