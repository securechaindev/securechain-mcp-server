from typing import Any

from app.exceptions import TIXsNotFoundException

from .dbs import get_collection


async def read_tixs_by_owner_name(owner: str, name: str, sbom_name: str) -> dict[str, Any]:
    tixs_collection = get_collection("tixs")
    cursor = tixs_collection.find(
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
