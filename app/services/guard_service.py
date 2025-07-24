from typing import Dict, List


class GuardService:
    def __init__(self):
        self.sap_matrix: Dict[str, List[str]] = {}
    def load_permissions(self, manifest_path: str):
        # TODO::: load YAML manifest into sap_matrix
        pass
    def verify_permission(self, badge_id: str, permission: str) -> bool:
        return permission in self.sap_matrix.get(badge_id, [])