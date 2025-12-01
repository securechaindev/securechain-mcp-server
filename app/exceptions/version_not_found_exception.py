from fastapi import HTTPException


class VersionNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="The Version have not been found.")
