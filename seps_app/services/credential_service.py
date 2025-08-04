from typing import Optional

from sqlalchemy.orm import Session

from seps_app.CredentialDTO import CredentialDTO
from seps_app.credentialORM import CredentialORM


class CredentialService:
    def __init__(self, db : Session):
        self.db = db

    def claim_credentials(self, user_id, service_name) -> Optional[CredentialORM]:
        """
        Retrieves credentials for a given user.
        """
        pass

    def release_credentials(self, user_id) -> bool:
        return True

    def add_credential(self, cred: CredentialDTO) -> CredentialORM:
        # todo ::: make sure unique_id
        cred_orm = CredentialORM(**cred.model_dump()) # TODO ::: mapper maybe?
        self.db.add(cred_orm)
        self.db.commit()
        self.db.refresh(cred_orm)
        return cred_orm

