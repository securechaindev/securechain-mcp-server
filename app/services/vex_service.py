from typing import Any

from app.exceptions import VEXsNotFoundException

from .dbs import get_collection


async def read_vexs_by_owner_name(owner: str, name: str, sbom_name: str) -> dict[str, Any]:
    vexs_collection = get_collection("vexs")
    cursor = vexs_collection.find(
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
