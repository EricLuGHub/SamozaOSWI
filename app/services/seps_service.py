from typing import List, Dict


class SamozaEphemeralPoolService:
    def __init__(self):
        self.pool: Dict[str, List[Dict[str, str]]] = {}
    def get_pool(self, provider: str) -> List[Dict[str, str]]:
        return self.pool.get(provider, [])
    def allocate(self, provider: str) -> Dict[str, str]:
        return self.pool[provider].pop()
    def release(self, provider: str, creds: Dict[str, str]):
        self.pool[provider].append(creds)