from collections.abc import Mapping
from contextvars import ContextVar
from typing import Optional

_current_headers: ContextVar[Optional[Mapping[str, str]]] = ContextVar("current_headers", default=None)

def set_current_headers(headers: Mapping[str, str]):
    return _current_headers.set(headers)

def reset_current_headers(token):
    _current_headers.reset(token)

def get_current_headers() -> Mapping[str, str]:
    headers = _current_headers.get()
    return headers or {}
