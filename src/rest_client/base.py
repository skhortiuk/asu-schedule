import urllib.parse
from json.decoder import JSONDecodeError
from typing import Union, Tuple, Dict, AnyStr

import aiohttp

from src.rest_client.config import DEFAULT_ENCODING

api_response = Union[Tuple[Dict, int], Tuple[AnyStr, int]]


class BaseRestClient:
    def __init__(self, destination: str):
        self.destination = destination

    async def get(self, headers: Dict = None, **params) -> api_response:
        return await self._make_http_request("GET", headers=headers, params=params)

    async def post(self, data: Dict, headers: Dict = None) -> api_response:
        return await self._make_http_request("POST", headers=headers, data=data)

    async def make_direct_http_request(
        self,
        request_method: str,
        request_url: str = None,
        headers: Dict = None,
        data: Dict = None,
        params: Dict = None,
    ):
        return await self._make_http_request(
            request_method, request_url, headers, data, params
        )

    async def _make_http_request(
        self,
        request_method: str,
        request_url: str = None,
        headers: Dict = None,
        data: Dict = None,
        params: Dict = None,
    ) -> api_response:
        request_url = request_url or self.destination
        params = {k: v for k, v in params.items() if v is not None} if params else None
        data = urllib.parse.urlencode(data) if data else None
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method=request_method,
                url=request_url,
                params=params,
                data=data,
                headers=headers,
            ) as response:
                try:
                    return (
                        await response.json(
                            encoding=DEFAULT_ENCODING, content_type="text/html"
                        ),
                        response.status,
                    )
                except JSONDecodeError:
                    return (
                        await response.text(encoding=DEFAULT_ENCODING),
                        response.status,
                    )
