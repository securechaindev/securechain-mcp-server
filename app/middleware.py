from app.utils import reset_current_headers, set_current_headers


class RequestContextMiddleware:
    def __init__(self, app, sse_path="/mcp"):
        self.app = app
        self.sse_path = sse_path

    @staticmethod
    def _headers_to_dict(raw_headers: list[tuple[bytes, bytes]]) -> dict[str, str]:
        return {k.decode("latin1").lower(): v.decode("latin1") for k, v in raw_headers}

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        path = scope.get("path", "")
        method = scope.get("method", "GET")
        headers = self._headers_to_dict(scope.get("headers", []))

        if path == self.sse_path and method == "GET" and "text/event-stream" in headers.get("accept", ""):
            return await self.app(scope, receive, send)

        token = await set_current_headers(headers)
        try:
            return await self.app(scope, receive, send)
        finally:
            await reset_current_headers(token)
