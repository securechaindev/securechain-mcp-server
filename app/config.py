from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class MCPSettings(BaseSettings):
    GRAPH_DB_URI: str = Field("bolt://neo4j:7687", alias="GRAPH_DB_URI")
    VULN_DB_URI: str = Field('mongodb://mongoSecureChain:mongoSecureChain@mongo:27017/admin', alias="VULN_DB_URI")
    GRAPH_DB_USER: str = Field("neo4j", alias="GRAPH_DB_USER")
    GRAPH_DB_PASSWORD: str = Field("neoSecureChain", alias="GRAPH_DB_PASSWORD")
    BACKEND_URL: str = Field("http://securechain-gateway:8000", alias="BACKEND_URL")
    AUTH_LOGIN_URL: str = Field("/auth/login", alias="AUTH_LOGIN_URL")
    AUTH_REFRESH_URL: str = Field("/auth/refresh", alias="AUTH_REFRESH_URL")
    AUTH_EMAIL: str = Field("mcp-bot@example.com", alias="AUTH_EMAIL")
    AUTH_PASS: str = Field("supersecre3T*", alias="AUTH_PASS")
    REQUEST_TIMEOUT: float = Field(60, alias="REQUEST_TIMEOUT")
    SAFETY_MARGIN: int = Field(30, alias="SAFETY_MARGIN")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=False
    )


@lru_cache
def get_settings() -> MCPSettings:
    return MCPSettings()


mcp_settings: MCPSettings = get_settings()
