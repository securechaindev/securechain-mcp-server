import asyncio

from aiohttp import ClientResponse, ClientSession, ClientTimeout

from app.config import mcp_settings

ACCESS_COOKIE_NAME = "access_token"
REFRESH_COOKIE_NAME = "refresh_token"

class SessionManager:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self._session: ClientSession | None = None
        self._access_token: str | None = None
        self._refresh_token: str | None = None
        self._lock = asyncio.Lock()

    async def _ensure_session(self):
        if self._session is None or self._session.closed:
            timeout = ClientTimeout(total=mcp_settings.REQUEST_TIMEOUT)
            self._session = ClientSession(timeout=timeout)

    def _update_from_cookies(self, resp: ClientResponse):
        if ACCESS_COOKIE_NAME in resp.cookies and resp.cookies[ACCESS_COOKIE_NAME].value:
            self._access_token = resp.cookies[ACCESS_COOKIE_NAME].value
        if REFRESH_COOKIE_NAME in resp.cookies and resp.cookies[REFRESH_COOKIE_NAME].value:
            self._refresh_token = resp.cookies[REFRESH_COOKIE_NAME].value

    async def _login(self):
        await self._ensure_session()
        async with self._session.post(
            f"{mcp_settings.BACKEND_URL}{mcp_settings.AUTH_LOGIN_URL}",
            json={"email": self.email, "password": self.password},
        ) as resp:
            resp.raise_for_status()
            self._update_from_cookies(resp)

    async def _refresh(self):
        await self._ensure_session()
        async with self._session.post(
            f"{mcp_settings.BACKEND_URL}{mcp_settings.AUTH_REFRESH_URL}"
        ) as resp:
            resp.raise_for_status()
            self._update_from_cookies(resp)

    async def ensure_authenticated(self):
        async with self._lock:
            if not self._access_token or not self._refresh_token:
                await self._login()

    async def auth_headers(self) -> dict:
        await self.ensure_authenticated()
        return {"Authorization": f"Bearer {self._access_token}"} if self._access_token else {}

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()


class SessionPool:
    def __init__(self):
        self._by_email: dict[str, SessionManager] = {}
        self._lock = asyncio.Lock()

    async def get(self, email: str, password: str) -> SessionManager:
        async with self._lock:
            sm = self._by_email.get(email)
            if sm is None or sm.password != password:
                sm = SessionManager(email, password)
                self._by_email[email] = sm
            return sm

    async def close_all(self):
        async with self._lock:
            for sm in self._by_email.values():
                await sm.close()
            self._by_email.clear()

session_pool = SessionPool()
