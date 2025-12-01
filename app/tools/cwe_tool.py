from json import dumps

from mcp.types import TextContent

from app.dependencies import get_cwe_service, get_json_encoder
from app.exceptions import CWENotFoundException, CWEsNotFoundException
from app.services import CWEService
from app.utils import JSONEncoder


class CWETool:
    def __init__(self):
        self.cwe_service: CWEService = get_cwe_service()
        self.json_encoder: JSONEncoder = get_json_encoder()

    async def get_cwe_tool(
        self,
        cwe_id: str
    ) -> list[TextContent]:
        try:
            out = await self.cwe_service.read_cwe_by_id(cwe_id)
            return [TextContent(type="text", text=dumps(self.json_encoder.encode(out), ensure_ascii=False, indent=2))]
        except CWENotFoundException:
            return [TextContent(type="text", text=f"CWE with ID {cwe_id} not found.")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {e!s}")]


    async def get_cwes_by_vulnerability_tool(
        self,
        vulnerability_id: str
    ) -> list[TextContent]:
        try:
            out = await self.cwe_service.read_cwes_by_vulnerability_id(vulnerability_id)
            return [TextContent(type="text", text=dumps(self.json_encoder.encode(out), ensure_ascii=False, indent=2))]
        except CWEsNotFoundException:
            return [TextContent(type="text", text=f"CWEs related to vulnerability {vulnerability_id} not found.")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {e!s}")]
