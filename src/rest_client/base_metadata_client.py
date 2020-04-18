from typing import Dict

from src.rest_client.base import BaseRestClient, api_response
from src.rest_client.config import API_AJAX_FLAG


class BaseMetadataClient(BaseRestClient):
    AJAX_ID = API_AJAX_FLAG
    REQUEST_AJAX_FLAG: NotImplemented

    async def get(self, headers: Dict = None, **params) -> api_response:
        params.update({"n": self.AJAX_ID, "lev": self.REQUEST_AJAX_FLAG})
        return await super(BaseMetadataClient, self).get(headers=headers, **params)
