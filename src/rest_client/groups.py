from typing import Dict, Optional

from src.rest_client.base import api_response
from src.rest_client.base_lists_client import BaseListsClient
from src.rest_client.config import GROUPS_AJAX_FLAG


class GroupRestClient(BaseListsClient):
    REQUEST_AJAX_FLAG = GROUPS_AJAX_FLAG

    async def all_groups(self, headers: Dict = None, faculty: int = None, query: Optional[str] = None) -> api_response:
        return await self.get(headers=headers, faculty=faculty, query=query)

    async def exists(self, group_code: str, faculty: int = None, headers=None) -> api_response:
        group_codes, status = await self.all_groups(headers=headers, faculty=faculty, query=group_code)
        return {
                   "exists": group_code in group_codes["suggestions"]
               }, status
