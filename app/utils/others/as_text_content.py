from json import dumps

from mcp.types import TextContent


async def as_text_content(payload) -> list[TextContent]:
    return [TextContent(type="text", text=dumps(payload, ensure_ascii=False, indent=2))]
