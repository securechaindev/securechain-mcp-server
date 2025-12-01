from fastapi import HTTPException


class CWENotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="The CWE have not been found.")
