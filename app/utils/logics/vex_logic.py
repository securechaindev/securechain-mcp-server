from typing import Any

from aiohttp import ClientResponseError

from app.settings import settings
from app.exceptions import PackageNotFoundException
from app.utils.auth import SessionManager


async def create_vex(session_manager: SessionManager, owner: str, name: str) -> dict[str, Any]:
    await session_manager._ensure_session()
    headers = await session_manager.auth_headers()
    url = f"{settings.BACKEND_URL}/vexgen/vex_tix/generate"
    body = {"owner": owner, "name": name, "user_id": session_manager._user_id}

    async def _do_request():
        async with session_manager._session.post(url, json=body, headers=headers) as resp:
            if resp.status == 422:
                text = await resp.text()
                raise RuntimeError(f"422 validation error: {text}")
            if resp.status == 404:
                raise PackageNotFoundException()
            if resp.status == 401:
                raise ClientResponseError(request_info=resp.request_info, history=resp.history, status=401, message="unauthorized")
            resp.raise_for_status()

    try:
        return await _do_request()
    except ClientResponseError as e:
        if e.status == 401:
            if hasattr(session_manager, "_refresh"):
                await session_manager._refresh()
            return await _do_request()
        raise
