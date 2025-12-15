from typing import Any

from app.database import DatabaseManager
from app.exceptions import VEXsNotFoundException


class VEXService:
    def __init__(self, db: DatabaseManager):
        self.vexs_collection = db.get_vexs_collection()

    async def read_vexs_by_owner_name(self, owner: str, name: str, sbom_name: str) -> list[dict[str, Any]]:
        cursor = self.vexs_collection.find(
            {
                "owner": owner,
                "name": name,
                "sbom_name": sbom_name
            }
        )
        results = await cursor.to_list(length=None)
        vexs = [vex.get("vex", {}) for vex in results]
        if not vexs:
            raise VEXsNotFoundException()
        return vexs
