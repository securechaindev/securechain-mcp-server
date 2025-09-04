from mcp.types import TextContent

from app.exceptions import CWENotFoundException
from app.services import read_cwe_by_id
from app.utils import as_text_content, json_encoder


async def get_cwe_tool(
    cwe_id: str
) -> list[TextContent]:
    try:
        out = await read_cwe_by_id(cwe_id)
        return await as_text_content(await json_encoder(out))
    except CWENotFoundException:
        return [TextContent(type="text", text=f"cwe_not_found: {cwe_id}")]
    except Exception as e:
        return [TextContent(type="text", text=f"error: {e!s}")]
