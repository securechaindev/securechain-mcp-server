from typing import Any

from .dbs import get_collection


async def read_cwe_by_id(cwe_id: str) -> dict[str, Any]:
    cwes_collection = get_collection("cwes")
    result = await cwes_collection.find_one(
        {
            "id": cwe_id
        }
    )
    return result if result else {}


async def read_cwes_by_vulnerability_id(vulnerability_id: str) -> list[dict[str, Any]]:
    cwes_collection = get_collection("cwes")
    cursor = cwes_collection.find(
        {
            "cvelist": {"$in": [vulnerability_id]}
        }
    )
    results = await cursor.to_list(length=None)
    return results
