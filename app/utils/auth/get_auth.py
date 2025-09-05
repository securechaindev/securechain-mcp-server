from contextvars import ContextVar

from app.exceptions import AuthenticationError


async def get_auth_from_request(headers: ContextVar) -> tuple[str, str]:
    email = headers.get("x-auth-email")
    password = headers.get("x-auth-pass")
    if not email or not password:
        raise AuthenticationError()
    return email, password
