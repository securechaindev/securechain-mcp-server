from json import dumps

from mcp.types import TextContent

from app.dependencies import (
    get_json_encoder,
    get_request_context,
    get_session_pool,
    get_tix_service,
    get_vex_logic,
    get_vex_service,
)
from app.exceptions import TIXsNotFoundException, VEXsNotFoundException
from app.logics import VEXLogic
from app.services import TIXService, VEXService
from app.utils import JSONEncoder, RequestContext, SessionPool


class VEXTool:
    def __init__(self):
        self.vex_service: VEXService = get_vex_service()
        self.tix_service: TIXService = get_tix_service()
        self.json_encoder: JSONEncoder = get_json_encoder()
        self.session_pool: SessionPool = get_session_pool()
        self.request_context: RequestContext = get_request_context()
        self.vex_logic: VEXLogic = get_vex_logic()

    async def get_vexs_tool(
        self,
        owner: str,
        name: str,
        sbom_name: str,
    ) -> list[TextContent]:
        api_key = self.request_context.get_api_key()
        sm = await self.session_pool.get(api_key)
        try:
            await self.vex_logic.create_vex(sm, owner, name)
            vexs = await self.vex_service.read_vexs_by_owner_name(owner, name, sbom_name)
            tixs = await self.tix_service.read_tixs_by_owner_name(owner, name, sbom_name)
            return [TextContent(type="text", text=dumps(self.json_encoder.encode({"vexs": vexs, "tixs": tixs}), ensure_ascii=False, indent=2))]
        except VEXsNotFoundException:
            return [TextContent(type="text", text=f"Vulnerability Exploitability eXchanges not found for repository with owner {owner} and name {name}.")]
        except TIXsNotFoundException:
            return [TextContent(type="text", text=f"Threat Intelligence eXchanges not found for repository with owner {owner} and name {name}.")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {e!s}")]
