from typing import Dict

from src.rest_client.base import BaseRestClient, api_response
from src.rest_client.config import DEFAULT_ENCODING


class ScheduleBaseRestClient(BaseRestClient):
    ENTITY: NotImplemented

    async def schedule(
            self, from_date: str, to_date: str,
            value: str, headers: Dict = None
    ) -> api_response:
        payload = {
            "sdate": from_date.encode(DEFAULT_ENCODING),
            "edate": to_date.encode(DEFAULT_ENCODING),
            self.ENTITY: value.encode(DEFAULT_ENCODING)
        }
        return await self.post(headers=headers, data=payload)
