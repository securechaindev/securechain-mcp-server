from collections.abc import Mapping
from contextvars import ContextVar, Token

from app.exceptions import AuthenticationErrorException


class RequestContext:
    current_headers: ContextVar[Mapping[str, str] | None] = ContextVar("current_headers", default=None)

    def set_headers(self, headers: Mapping[str, str]) -> Token:
        return self.current_headers.set(headers)

    def reset_headers(self, token: Token) -> None:
        self.current_headers.reset(token)

    def get_headers(self) -> Mapping[str, str]:
        return self.current_headers.get() or {}

    def get_api_key(self) -> str:
        headers = self.get_headers()
        api_key = headers.get("x-api-key")
        if not api_key:
            raise AuthenticationErrorException()
        return api_key
