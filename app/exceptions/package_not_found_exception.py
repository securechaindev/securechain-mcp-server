from fastapi import HTTPException


class PackageNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="The Package have not been found.")
