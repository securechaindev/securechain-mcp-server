from aiohttp import ClientSession, ClientTimeout

from app.settings import settings


class SessionManager:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session: ClientSession | None = None

    async def ensure_session(self):
        if self.session is None or self.session.closed:
            timeout = ClientTimeout(total=settings.REQUEST_TIMEOUT)
            self.session = ClientSession(timeout=timeout)

    def auth_headers(self) -> dict:
        return {"X-API-Key": self.api_key}

    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()
