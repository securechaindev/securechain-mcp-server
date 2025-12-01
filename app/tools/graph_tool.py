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
from app.logics import GraphLogic
from app.utils import JSONEncoder, RequestContext, SessionPool


class GraphTool:
    def __init__(self):
        self.json_encoder: JSONEncoder = get_json_encoder()
        self.session_pool: SessionPool = get_session_pool()
        self.request_context: RequestContext = get_request_context()
        self.graph_logic: GraphLogic = get_graph_logic()

    async def get_package_status_tool(
        self,
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
        api_key = self.request_context.get_api_key()
        sm = await self.session_pool.get(api_key)
        try:
            out = await self.graph_logic.get_package_status(sm, node_type, package_name)
            return [TextContent(type="text", text=dumps(self.json_encoder.encode(out), ensure_ascii=False, indent=2))]
        except PackageNotFoundException:
            return [TextContent(type="text", text=f"Package {package_name} of type {node_type} not Found.")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {e!s}")]


    async def get_package_ssc_tool(
        self,
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
        api_key = self.request_context.get_api_key()
        sm = await self.session_pool.get(api_key)
        try:
            out = await self.graph_logic.get_package_ssc(sm, node_type, package_name)
            return [TextContent(type="text", text=dumps(self.json_encoder.encode(out), ensure_ascii=False, indent=2))]
        except PackageNotFoundException:
            return [TextContent(type="text", text=f"Package {package_name} of type {node_type} not Found.")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {e!s}")]


    async def get_version_status_tool(
        self,
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
        api_key = self.request_context.get_api_key()
        sm = await self.session_pool.get(api_key)
        try:
            out = await self.graph_logic.get_version_status(sm, node_type, package_name, version_name)
            return [TextContent(type="text", text=dumps(self.json_encoder.encode(out), ensure_ascii=False, indent=2))]
        except VersionNotFoundException:
            return [TextContent(type="text", text=f"Version {version_name} related to package {package_name} of type {node_type} not Found.")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {e!s}")]


    async def get_version_ssc_tool(
        self,
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
        api_key = self.request_context.get_api_key()
        sm = await self.session_pool.get(api_key)
        try:
            out = await self.graph_logic.get_version_ssc(sm, node_type, package_name, version_name)
            return [TextContent(type="text", text=dumps(self.json_encoder.encode(out), ensure_ascii=False, indent=2))]
        except PackageNotFoundException:
            return [TextContent(type="text", text=f"Package {package_name} of type {node_type} not Found.")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {e!s}")]
