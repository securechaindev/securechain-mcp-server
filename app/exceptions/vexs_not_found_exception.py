from fastapi import HTTPException


class VEXsNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="The Vulnerability Exploitability eXchanges have not been found.")
