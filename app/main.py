from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.mcp_server import mcp
from app.utils import session_pool

mcp_app = mcp.http_app(path="/mcp")

app = FastAPI(title="Secure Chain MCP API", lifespan=mcp_app.lifespan)

app.mount("/", mcp_app)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Aquí podrías añadir lógica de startup si hace falta
    yield
    # Shutdown: cerrar todas las sesiones activas
    await session_pool.close_all()

@app.get("/health")
async def health():
    return {"detail": "healthy"}
