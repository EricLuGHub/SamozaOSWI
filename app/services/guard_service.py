from typing import Dict, List


class GuardService:
    def __init__(self):
        self.sap_matrix: Dict[str, List[str]] = {}
    def load_permissions(self, manifest_path: str):
        # TODO::: load the perms
        pass
    def verify_permission(self, badge_id: str, permission: str) -> bool:
        # todo::: cred_svc credentials
        # return the credentials
        # rename to cred_svc?
        return True
        # TODO ::: todo
        return permission in self.sap_matrix.get(badge_id, [])