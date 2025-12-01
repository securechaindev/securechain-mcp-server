from typing import Any

from app.database import DatabaseManager
from app.exceptions import TIXsNotFoundException


class TIXService:
    def __init__(self, db: DatabaseManager):
        self.tixs_collection = db.get_tixs_collection()

    async def read_tixs_by_owner_name(self, owner: str, name: str, sbom_name: str) -> dict[str, Any]:
        cursor = self.tixs_collection.find(
            {
                "owner": owner,
                "name": name,
                "sbom_name": sbom_name
            }
        )
        results = await cursor.to_list(length=None)
        tixs = [tix.get("tix", {}) for tix in results]
        if not tixs:
            raise TIXsNotFoundException()
        return tixs
