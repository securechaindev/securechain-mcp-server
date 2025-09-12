from typing import Any

from aiohttp import ClientResponseError

from app.config import mcp_settings
from app.exceptions import PackageNotFoundException
from app.utils.auth import SessionManager


async def get_package_status(session_manager: SessionManager, node_type: str, package_name: str) -> dict[str, Any]:
    await session_manager._ensure_session()
    headers = await session_manager.auth_headers()
    url = f"{mcp_settings.BACKEND_URL}/depex/graph/package/status"
    params = {"node_type": node_type, "package_name": package_name}

    async def _do_request():
        async with session_manager._session.get(url, params=params, headers=headers) as resp:
            if resp.status == 422:
                text = await resp.text()
                raise RuntimeError(f"422 validation error: {text}")
            if resp.status == 404:
                raise PackageNotFoundException()
            if resp.status == 401:
                raise ClientResponseError(request_info=resp.request_info, history=resp.history, status=401, message="unauthorized")
            resp.raise_for_status()
            return await resp.json()

    try:
        return await _do_request()
    except ClientResponseError as e:
        if e.status == 401:
            if hasattr(session_manager, "_refresh"):
                await session_manager._refresh()
            return await _do_request()
        raise


async def get_package_ssc(session_manager: SessionManager, node_type: str, package_name: str) -> dict[str, Any]:
    await session_manager._ensure_session()
    headers = await session_manager.auth_headers()
    url = f"{mcp_settings.BACKEND_URL}/depex/operation/package/package_info"
    body = {"node_type": node_type, "package_name": package_name, "max_depth": 2}

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
            return await resp.json()

    try:
        return await _do_request()
    except ClientResponseError as e:
        if e.status == 401:
            if hasattr(session_manager, "_refresh"):
                await session_manager._refresh()
            return await _do_request()
        raise


async def get_version_status(session_manager: SessionManager, node_type: str, package_name: str, version_name: str) -> dict[str, Any]:
    await session_manager._ensure_session()
    headers = await session_manager.auth_headers()
    url = f"{mcp_settings.BACKEND_URL}/depex/graph/version/status"
    params = {"node_type": node_type, "package_name": package_name, "version_name": version_name}

    async def _do_request():
        async with session_manager._session.get(url, params=params, headers=headers) as resp:
            if resp.status == 422:
                text = await resp.text()
                raise RuntimeError(f"422 validation error: {text}")
            if resp.status == 404:
                raise PackageNotFoundException()
            if resp.status == 401:
                raise ClientResponseError(request_info=resp.request_info, history=resp.history, status=401, message="unauthorized")
            resp.raise_for_status()
            return await resp.json()

    try:
        return await _do_request()
    except ClientResponseError as e:
        if e.status == 401:
            if hasattr(session_manager, "_refresh"):
                await session_manager._refresh()
            return await _do_request()
        raise
