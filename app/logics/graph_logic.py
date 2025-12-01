from typing import Any

from app.exceptions import PackageNotFoundException
from app.settings import settings
from app.utils import SessionManager


class GraphLogic:
    async def get_package_status(self, session_manager: SessionManager, node_type: str, package_name: str) -> dict[str, Any]:
        await session_manager.ensure_session()
        headers = session_manager.auth_headers()
        url = f"{settings.BACKEND_URL}/depex/graph/package/status"
        params = {"node_type": node_type, "package_name": package_name}

        async with session_manager.session.get(url, params=params, headers=headers) as resp:
            if resp.status == 422:
                text = await resp.text()
                raise RuntimeError(f"422 validation error: {text}")
            if resp.status == 404:
                raise PackageNotFoundException()
            resp.raise_for_status()
            return await resp.json()

    async def get_package_ssc(self, session_manager: SessionManager, node_type: str, package_name: str) -> dict[str, Any]:
        await session_manager.ensure_session()
        headers = session_manager.auth_headers()
        url = f"{settings.BACKEND_URL}/depex/operation/ssc/package_ssc_info"
        body = {"node_type": node_type, "package_name": package_name, "max_depth": 2}

        async with session_manager.session.post(url, json=body, headers=headers) as resp:
            if resp.status == 422:
                text = await resp.text()
                raise RuntimeError(f"422 validation error: {text}")
            if resp.status == 404:
                raise PackageNotFoundException()
            resp.raise_for_status()
            return await resp.json()

    async def get_version_status(self, session_manager: SessionManager, node_type: str, package_name: str, version_name: str) -> dict[str, Any]:
        await session_manager.ensure_session()
        headers = session_manager.auth_headers()
        url = f"{settings.BACKEND_URL}/depex/graph/version/status"
        params = {"node_type": node_type, "package_name": package_name, "version_name": version_name}

        async with session_manager.session.get(url, params=params, headers=headers) as resp:
            if resp.status == 422:
                text = await resp.text()
                raise RuntimeError(f"422 validation error: {text}")
            if resp.status == 404:
                raise PackageNotFoundException()
            resp.raise_for_status()
            return await resp.json()

    async def get_version_ssc(self, session_manager: SessionManager, node_type: str, package_name: str, version_name: str) -> dict[str, Any]:
        await session_manager.ensure_session()
        headers = session_manager.auth_headers()
        url = f"{settings.BACKEND_URL}/depex/operation/ssc/version_ssc_info"
        body = {"node_type": node_type, "package_name": package_name, "version_name": version_name, "max_depth": 2}

        async with session_manager.session.post(url, json=body, headers=headers) as resp:
            if resp.status == 422:
                text = await resp.text()
                raise RuntimeError(f"422 validation error: {text}")
            if resp.status == 404:
                raise PackageNotFoundException()
            resp.raise_for_status()
            return await resp.json()
