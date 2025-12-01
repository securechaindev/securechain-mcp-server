from typing import Any

from app.database import DatabaseManager
from app.exceptions import CWENotFoundException, CWEsNotFoundException


class CWEService:
    def __init__(self, db: DatabaseManager):
        self.cwes_collection = db.get_cwes_collection()

    async def read_cwe_by_id(self, cwe_id: str) -> dict[str, Any]:
        result = await self.cwes_collection.find_one(
            {
                "id": cwe_id
            }
        )
        if not result:
            raise CWENotFoundException()
        return result

    async def read_cwes_by_vulnerability_id(self, vulnerability_id: str) -> list[dict[str, Any]]:
        cursor = self.cwes_collection.find(
            {
                "cvelist": {"$in": [vulnerability_id]}
            }
        )
        results = await cursor.to_list(length=None)
        if not results:
            raise CWEsNotFoundException()
        return results
