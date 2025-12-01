from fastapi import HTTPException


class AuthenticationErrorException(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Missing X-Auth-Email or X-Auth-Pass")
