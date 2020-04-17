from src.rest_client.base_lists_client import BaseListsClient
from src.rest_client.config import GROUPS_AJAX_FLAG


class GroupRestClient(BaseListsClient):
    REQUEST_AJAX_FLAG = GROUPS_AJAX_FLAG

    async def all_groups(self, headers=None, faculty: int = None):
        return await self.get(headers=headers, faculty=faculty)

    async def exists(self, group_code: str, faculty: int = None, headers=None):
        group_codes = await self.all_groups(headers=headers, faculty=faculty)
        return group_code in group_codes["suggestions"]
