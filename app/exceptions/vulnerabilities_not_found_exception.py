from fastapi import HTTPException


class VulnerabilitiesNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="The Vulnerabilities have not been found.")
