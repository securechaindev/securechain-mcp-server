from mcp.types import TextContent

from app.exceptions import VEXsNotFoundException
from app.services import read_vexs_by_owner_name
from app.utils import (
    as_text_content,
    create_vex,
    get_auth_from_request,
    get_current_headers,
    session_pool,
)


async def get_vexs_tool(
    owner: str,
    name: str
) -> list[TextContent]:
    headers = await get_current_headers()
    email, password = await get_auth_from_request(headers)
    sm = await session_pool.get(email, password)
    try:
        await create_vex(sm, owner, name)
        out = await read_vexs_by_owner_name(owner, name)
        return await as_text_content(out)
    except VEXsNotFoundException:
        return [TextContent(type="text", text=f"VEXs not found for repository with owner {owner} and name {name}.")]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e!s}")]
