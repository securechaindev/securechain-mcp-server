from fastapi import HTTPException


class CWEsNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="The CWEs have not been found.")
