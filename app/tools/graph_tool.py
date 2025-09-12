from typing import Literal

from mcp.types import TextContent

from app.exceptions import PackageNotFoundException, VersionNotFoundException
from app.utils import (
    as_text_content,
    get_auth_from_request,
    get_current_headers,
    get_package_ssc,
    get_package_status,
    get_version_ssc,
    get_version_status,
    session_pool,
)


async def get_package_status_tool(
    node_type: Literal[
        "PyPIPackage",
        "NPMPackage",
        "MavenPackage",
        "CargoPackage",
        "RubyGemsPackage",
        "NuGetPackage"
    ],
    package_name: str
) -> list[TextContent]:
    headers = await get_current_headers()
    email, password = await get_auth_from_request(headers)
    sm = await session_pool.get(email, password)
    try:
        out = await get_package_status(sm, node_type, package_name)
        return await as_text_content(out)
    except PackageNotFoundException:
        return [TextContent(type="text", text=f"Package {package_name} of type {node_type} not Found.")]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]


async def get_package_ssc_tool(
    node_type: Literal[
        "PyPIPackage",
        "NPMPackage",
        "MavenPackage",
        "CargoPackage",
        "RubyGemsPackage",
        "NuGetPackage"
    ],
    package_name: str
) -> list[TextContent]:
    headers = await get_current_headers()
    email, password = await get_auth_from_request(headers)
    sm = await session_pool.get(email, password)
    try:
        out = await get_package_ssc(sm, node_type, package_name)
        return await as_text_content(out)
    except PackageNotFoundException:
        return [TextContent(type="text", text=f"Package {package_name} of type {node_type} not Found.")]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]


async def get_version_status_tool(
    node_type: Literal[
        "PyPIPackage",
        "NPMPackage",
        "MavenPackage",
        "CargoPackage",
        "RubyGemsPackage",
        "NuGetPackage"
    ],
    package_name: str,
    version_name: str
) -> list[TextContent]:
    headers = await get_current_headers()
    email, password = await get_auth_from_request(headers)
    sm = await session_pool.get(email, password)
    try:
        out = await get_version_status(sm, node_type, package_name, version_name)
        return await as_text_content(out)
    except VersionNotFoundException:
        return [TextContent(type="text", text=f"Version {version_name} related to package {package_name} of type {node_type} not Found.")]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]


async def get_version_ssc_tool(
    node_type: Literal[
        "PyPIPackage",
        "NPMPackage",
        "MavenPackage",
        "CargoPackage",
        "RubyGemsPackage",
        "NuGetPackage"
    ],
    package_name: str,
    version_name: str
) -> list[TextContent]:
    headers = await get_current_headers()
    email, password = await get_auth_from_request(headers)
    sm = await session_pool.get(email, password)
    try:
        out = await get_version_ssc(sm, node_type, package_name, version_name)
        return await as_text_content(out)
    except PackageNotFoundException:
        return [TextContent(type="text", text=f"Package {package_name} of type {node_type} not Found.")]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
