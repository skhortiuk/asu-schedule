from src.rest_client.base import BaseRestClient
from src.rest_client.config import API_AJAX_FLAG


class BaseListsClient(BaseRestClient):
    AJAX_ID = API_AJAX_FLAG
    REQUEST_AJAX_FLAG: NotImplemented

    async def get(self, headers=None, **params):
        params.update({
            "n": self.AJAX_ID,
            "lev": self.REQUEST_AJAX_FLAG
        })
        return await super(BaseListsClient, self).get(headers=headers, **params)
