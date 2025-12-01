from functools import lru_cache

from pydantic import ConfigDict, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env", extra="ignore", case_sensitive=False)

    GRAPH_DB_URI: str = Field("bolt://neo4j:7687", alias="GRAPH_DB_URI")
    VULN_DB_URI: str = Field('mongodb://mongoSecureChain:mongoSecureChain@mongo:27017/admin', alias="VULN_DB_URI")
    GRAPH_DB_USER: str = Field("neo4j", alias="GRAPH_DB_USER")
    GRAPH_DB_PASSWORD: str = Field("neoSecureChain", alias="GRAPH_DB_PASSWORD")
    BACKEND_URL: str = Field("http://securechain-gateway:8000", alias="BACKEND_URL")
    REQUEST_TIMEOUT: int = Field(60, alias="REQUEST_TIMEOUT")

    # Database Configuration
    DB_MIN_POOL_SIZE: int = 10
    DB_MAX_POOL_SIZE: int = 100
    DB_MAX_IDLE_TIME_MS: int = 60000
    DB_DEFAULT_QUERY_TIMEOUT_MS: int = 30000
    DB_VEXS_COLLECTION: str = "vexs"
    DB_TIXS_COLLECTION: str = "tixs"
    DB_VULNERABILITIES_COLLECTION: str = "vulnerabilities"
    DB_CWES_COLLECTION: str = "cwes"
    DB_EXPLOITS_COLLECTION: str = "exploits"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
