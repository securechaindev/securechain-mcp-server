from fastapi import HTTPException


class AuthenticationError(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Missing X-Auth-Email or X-Auth-Pass")


class PackageNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="The Package have not been found.")


class VersionNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="The Version have not been found.")


class VulnerabilityNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="The Vulnerability have not been found.")


class VulnerabilitiesNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="The Vulnerabilities have not been found.")


class ExploitNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="The Exploit have not been found.")


class ExploitsNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="The Exploits have not been found.")


class CWENotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="The CWE have not been found.")


class CWEsNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="The CWEs have not been found.")
