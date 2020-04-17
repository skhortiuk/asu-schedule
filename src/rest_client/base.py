import aiohttp
import ujson

from src.rest_client.config import DEFAULT_ENCODING


class BaseRestClient:

    def __init__(self, destination):
        self.destination = destination

    async def get(self, headers=None, **params):
        return await self._make_http_request("GET", headers=headers, params=params)

    async def _make_http_request(
            self, request_method: str, request_url: str = None,
            headers=None, data=None,
            params=None, jsonify: bool = True
    ):
        request_url = request_url or self.destination
        headers = headers or None
        data = ujson.dumps(data) if (data is not None and jsonify) else data
        params = {k: v for k, v in params.items() if v is not None} if params else None
        async with aiohttp.ClientSession() as session:
            async with session.request(
                    method=request_method, url=request_url, params=params, data=data, headers=headers
            ) as response:
                try:
                    return await response.json(encoding=DEFAULT_ENCODING, content_type="text/html")
                except aiohttp.ContentTypeError:
                    return response.content, response.status
