from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.mcp_server import mcp
from app.middleware import RequestContextMiddleware
from app.utils import session_pool

mcp_app = mcp.http_app(path="/mcp")

mcp_app.add_middleware(RequestContextMiddleware, sse_path="/mcp")

app = FastAPI(title="Secure Chain MCP API", lifespan=mcp_app.lifespan)

app.mount("/", mcp_app)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await session_pool.close_all()

@app.get("/health")
async def health():
    return {"detail": "healthy"}
