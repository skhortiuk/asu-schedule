from typing import Dict, Optional

from src.rest_client.base import BaseRestClient


class FacultiesRestClient(BaseRestClient):
    async def all_faculties(self, headers: Optional[Dict] = None, **kwargs):
        return await self.get(headers=headers, **kwargs)

    async def exists(self, query: str, headers=None):
        faculties, status = await self.all_faculties(headers=headers, query=query)
        exists = False
        for faculty in faculties:
            if query == faculty.get('name', ""):
                exists = True
                break
        return {"exists": exists},   status
