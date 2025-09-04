from functools import lru_cache

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)
from neo4j import AsyncDriver, AsyncGraphDatabase

from app.config import mcp_settings


@lru_cache
def get_graph_db_driver() -> AsyncDriver:
    return AsyncGraphDatabase.driver(
        uri=mcp_settings.GRAPH_DB_URI,
        auth=(mcp_settings.GRAPH_DB_USER, mcp_settings.GRAPH_DB_PASSWORD),
    )


@lru_cache
def get_collection(collection_name: str) -> AsyncIOMotorCollection:
    client: AsyncIOMotorClient = AsyncIOMotorClient(mcp_settings.VULN_DB_URI)
    vulnerabilities_db: AsyncIOMotorDatabase = client.get_database("vulnerabilities")
    match collection_name:
        case "vulnerabilities":
            return vulnerabilities_db.get_collection(collection_name)
        case "cwes":
            return vulnerabilities_db.get_collection(collection_name)
        case "exploits":
            return vulnerabilities_db.get_collection(collection_name)
