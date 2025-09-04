from fastapi import Request

from app.exceptions import AuthenticationError


async def get_auth_from_request(request: Request) -> tuple[str, str]:
    email = request.headers.get("x-auth-email")
    password = request.headers.get("x-auth-pass")
    if not email or not password:
        raise AuthenticationError()
    return email, password
