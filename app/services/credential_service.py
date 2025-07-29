
class CredentialService:
    def __init__(self, credential_repository):
        self.credential_repository = credential_repository

    def get_credentials(self, user_id):
        """
        Retrieves credentials for a given user.
        """
        return self.credential_repository.get_credentials(user_id)

    def add_credential(self, user_id, credential):
        """
        Adds a new credential for a user.
        """
        return self.credential_repository.add_credential(user_id, credential)

    def update_credential(self, user_id, credential_id, updated_credential):
        """
        Updates an existing credential for a user.
        """
        return self.credential_repository.update_credential(user_id, credential_id, updated_credential)

    def delete_credential(self, user_id, credential_id):
        """
        Deletes a credential for a user.
        """
        return self.credential_repository.delete_credential(user_id, credential_id)