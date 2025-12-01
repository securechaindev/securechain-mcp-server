from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.dependencies import get_session_pool
from app.mcp_server import mcp
from app.middleware import RequestContextMiddleware
from app.settings import settings

mcp_app = mcp.http_app(path="/mcp")

mcp_app.add_middleware(RequestContextMiddleware, sse_path="/mcp")

DESCRIPTION = """
The Secure Chain Model Context Protocol (MCP) server to give context about your software supply chain to any type of LLM or AI agent.
"""

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with mcp_app.lifespan(app):
        yield
    await get_session_pool().close_all()

app = FastAPI(
    lifespan=lifespan,
    title="Secure Chain MCP API",
    docs_url=settings.DOCS_URL,
    version="1.1.0",
    description=DESCRIPTION,
    contact={
        "name": "Secure Chain Team",
        "url": "https://github.com/securechaindev",
        "email": "hi@securechain.dev",
    },
    license_info={
        "name": "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "url": "https://www.gnu.org/licenses/gpl-3.0.html",
    },
)

app.mount("/", mcp_app)
