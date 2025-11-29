from functools import lru_cache

from neo4j import AsyncDriver, AsyncGraphDatabase
from pymongo import AsyncMongoClient
from pymongo.asynchronous.collection import AsyncCollection
from pymongo.asynchronous.database import AsyncDatabase

from app.settings import settings


@lru_cache
def get_graph_db_driver() -> AsyncDriver:
    return AsyncGraphDatabase.driver(
        uri=settings.GRAPH_DB_URI,
        auth=(settings.GRAPH_DB_USER, settings.GRAPH_DB_PASSWORD),
    )


@lru_cache
def get_collection(collection_name: str) -> AsyncCollection:
    client: AsyncMongoClient = AsyncMongoClient(settings.VULN_DB_URI)
    securechain_db: AsyncDatabase = client.get_database("securechain")
    vulnerabilities_db: AsyncDatabase = client.get_database("vulnerabilities")
    match collection_name:
        case "tixs":
            return securechain_db.get_collection(collection_name)
        case "vexs":
            return securechain_db.get_collection(collection_name)
        case "vulnerabilities":
            return vulnerabilities_db.get_collection(collection_name)
        case "cwes":
            return vulnerabilities_db.get_collection(collection_name)
        case "exploits":
            return vulnerabilities_db.get_collection(collection_name)
