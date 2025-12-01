from typing import Any

from app.exceptions import PackageNotFoundException
from app.settings import settings
from app.utils import SessionManager


class VEXTIXLogic:
    async def generate_vex_tix(self, session_manager: SessionManager, owner: str, name: str) -> dict[str, Any]:
        await session_manager.ensure_session()
        headers = session_manager.auth_headers()
        url = f"{settings.BACKEND_URL}/vexgen/vex_tix/generate"
        body = {"owner": owner, "name": name}

        async with session_manager.session.post(url, json=body, headers=headers) as resp:
            if resp.status == 422:
                text = await resp.text()
                raise RuntimeError(f"422 validation error: {text}")
            if resp.status == 404:
                raise PackageNotFoundException()
            resp.raise_for_status()
