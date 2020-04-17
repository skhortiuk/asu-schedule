import asyncio

from src.rest_client.base_lists_client import BaseListsClient
from src.rest_client.config import TEACHERS_AJAX_FLAG


class TeachersRestClient(BaseListsClient):
    REQUEST_AJAX_FLAG = TEACHERS_AJAX_FLAG

    async def all_teachers(self, headers=None, faculty: int = None):
        return await self.get(headers=headers, faculty=faculty)

    async def exists(self, teacher: str, faculty: int = None, headers=None):
        teachers = await self.all_teachers(headers=headers, faculty=faculty)
        return teacher in teachers["suggestions"]
