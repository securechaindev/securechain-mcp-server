from json import dumps

from mcp.types import TextContent

from app.dependencies import (
    get_json_encoder,
    get_request_context,
    get_session_pool,
    get_vex_service,
    get_vex_tix_logic,
)
from app.exceptions import VEXsNotFoundException


async def get_vexs_tool(
    owner: str,
    name: str,
    sbom_name: str,
) -> list[TextContent]:
    vex_service = get_vex_service()
    json_encoder = get_json_encoder()
    session_pool = get_session_pool()
    request_context = get_request_context()
    vex_tix_logic = get_vex_tix_logic()

    api_key = request_context.get_api_key()
    sm = await session_pool.get(api_key)
    try:
        await vex_tix_logic.generate_vex_tix(sm, owner, name)
        vexs = await vex_service.read_vexs_by_owner_name(owner, name, sbom_name)
        return [TextContent(type="text", text=dumps(json_encoder.encode({"vexs": vexs}), ensure_ascii=False, indent=2))]
    except VEXsNotFoundException:
        return [TextContent(type="text", text=f"Vulnerability Exploitability eXchanges not found for repository with owner {owner} and name {name}.")]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
