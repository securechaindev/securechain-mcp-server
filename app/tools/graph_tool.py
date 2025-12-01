from json import dumps
from typing import Literal

from mcp.types import TextContent

from app.dependencies import (
    get_graph_logic,
    get_json_encoder,
    get_request_context,
    get_session_pool,
)
from app.exceptions import PackageNotFoundException, VersionNotFoundException


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
    json_encoder = get_json_encoder()
    session_pool = get_session_pool()
    request_context = get_request_context()
    graph_logic = get_graph_logic()

    api_key = request_context.get_api_key()
    sm = await session_pool.get(api_key)
    try:
        out = await graph_logic.get_package_status(sm, node_type, package_name)
        return [TextContent(type="text", text=dumps(json_encoder.encode(out), ensure_ascii=False, indent=2))]
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
    json_encoder = get_json_encoder()
    session_pool = get_session_pool()
    request_context = get_request_context()
    graph_logic = get_graph_logic()

    api_key = request_context.get_api_key()
    sm = await session_pool.get(api_key)
    try:
        out = await graph_logic.get_package_ssc(sm, node_type, package_name)
        return [TextContent(type="text", text=dumps(json_encoder.encode(out), ensure_ascii=False, indent=2))]
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
    json_encoder = get_json_encoder()
    session_pool = get_session_pool()
    request_context = get_request_context()
    graph_logic = get_graph_logic()

    api_key = request_context.get_api_key()
    sm = await session_pool.get(api_key)
    try:
        out = await graph_logic.get_version_status(sm, node_type, package_name, version_name)
        return [TextContent(type="text", text=dumps(json_encoder.encode(out), ensure_ascii=False, indent=2))]
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
    json_encoder = get_json_encoder()
    session_pool = get_session_pool()
    request_context = get_request_context()
    graph_logic = get_graph_logic()

    api_key = request_context.get_api_key()
    sm = await session_pool.get(api_key)
    try:
        out = await graph_logic.get_version_ssc(sm, node_type, package_name, version_name)
        return [TextContent(type="text", text=dumps(json_encoder.encode(out), ensure_ascii=False, indent=2))]
    except PackageNotFoundException:
        return [TextContent(type="text", text=f"Package {package_name} of type {node_type} not Found.")]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
        try:
            out = await graph_logic.get_version_ssc(sm, node_type, package_name, version_name)
            return [TextContent(type="text", text=dumps(json_encoder.encode(out), ensure_ascii=False, indent=2))]
        except PackageNotFoundException:
            return [TextContent(type="text", text=f"Package {package_name} of type {node_type} not Found.")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {e!s}")]
