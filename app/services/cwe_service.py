from typing import Any

from app.exceptions import CWENotFoundException, CWEsNotFoundException

from .dbs import get_collection


async def read_cwe_by_id(cwe_id: str) -> dict[str, Any]:
    cwes_collection = get_collection("cwes")
    result = await cwes_collection.find_one(
        {
            "id": cwe_id
        }
    )
    if not result:
        raise CWENotFoundException()
    return result


async def read_cwes_by_vulnerability_id(vulnerability_id: str) -> list[dict[str, Any]]:
    cwes_collection = get_collection("cwes")
    cursor = cwes_collection.find(
        {
            "cvelist": {"$in": [vulnerability_id]}
        }
    )
    results = await cursor.to_list(length=None)
    if not results:
        raise CWEsNotFoundException()
    return results
