from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GRAPH_DB_URI: str = Field("bolt://neo4j:7687", alias="GRAPH_DB_URI")
    VULN_DB_URI: str = Field('mongodb://mongoSecureChain:mongoSecureChain@mongo:27017/admin', alias="VULN_DB_URI")
    GRAPH_DB_USER: str = Field("neo4j", alias="GRAPH_DB_USER")
    GRAPH_DB_PASSWORD: str = Field("neoSecureChain", alias="GRAPH_DB_PASSWORD")
    BACKEND_URL: str = Field("http://securechain-gateway:8000", alias="BACKEND_URL")
    REQUEST_TIMEOUT: int = Field(60, alias="REQUEST_TIMEOUT")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=False
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
