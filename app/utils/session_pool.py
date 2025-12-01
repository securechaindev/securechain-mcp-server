from asyncio import Lock

from .session_manager import SessionManager


class SessionPool:
    def __init__(self):
        self.by_api_key: dict[str, SessionManager] = {}
        self.lock = Lock()

    async def get(self, api_key: str) -> SessionManager:
        async with self.lock:
            sm = self.by_api_key.get(api_key)
            if sm is None:
                sm = SessionManager(api_key)
                self.by_api_key[api_key] = sm
            return sm

    async def close_all(self):
        async with self.lock:
            for sm in self.by_api_key.values():
                await sm.close()
            self.by_api_key.clear()
