import urllib.parse
from json.decoder import JSONDecodeError

import aiohttp

from src.rest_client.config import DEFAULT_ENCODING


class BaseRestClient:

    def __init__(self, destination):
        self.destination = destination

    async def get(self, headers=None, **params):
        return await self._make_http_request("GET", headers=headers, params=params)

    async def post(self, data, headers=None):
        print(data)
        return await self._make_http_request("POST", headers=headers, data=data)

    async def _make_http_request(
            self, request_method: str, request_url: str = None,
            headers=None, data=None, params=None
    ):
        request_url = request_url or self.destination
        params = {k: v for k, v in params.items() if v is not None} if params else None
        data = urllib.parse.urlencode(data)
        async with aiohttp.ClientSession() as session:
            async with session.request(
                    method=request_method, url=request_url, params=params, data=data, headers=headers
            ) as response:
                try:
                    return await response.json(encoding=DEFAULT_ENCODING, content_type="text/html")
                except JSONDecodeError:
                    return await response.text(encoding=DEFAULT_ENCODING), response.status
