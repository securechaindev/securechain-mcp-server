from fastapi import HTTPException


class TIXsNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="The Threat Intelligence eXchanges have not been found.")
