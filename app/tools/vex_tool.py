from mcp.types import TextContent

from app.exceptions import TIXsNotFoundException, VEXsNotFoundException
from app.services import read_tixs_by_owner_name, read_vexs_by_owner_name
from app.utils import (
    as_text_content,
    create_vex,
    get_auth_from_request,
    get_current_headers,
    session_pool,
)


async def get_vexs_tool(
    owner: str,
    name: str,
    sbom_name: str,
) -> list[TextContent]:
    headers = await get_current_headers()
    email, password = await get_auth_from_request(headers)
    sm = await session_pool.get(email, password)
    try:
        await create_vex(sm, owner, name)
        vexs = await read_vexs_by_owner_name(owner, name, sbom_name)
        tixs = await read_tixs_by_owner_name(owner, name, sbom_name)
        return await as_text_content({"vexs": vexs, "tixs": tixs})
    except VEXsNotFoundException:
        return [TextContent(type="text", text=f"Vulnerability Exploitability eXchanges not found for repository with owner {owner} and name {name}.")]
    except TIXsNotFoundException:
        return [TextContent(type="text", text=f"Threat Intelligence eXchanges not found for repository with owner {owner} and name {name}.")]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
