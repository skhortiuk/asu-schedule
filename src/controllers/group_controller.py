from typing import Optional

from src.rest_client.groups import GroupRestClient
from src.rest_client.utils import with_rest_client


@with_rest_client(GroupRestClient)
async def get_all_groups(client: GroupRestClient, query: Optional[str] = None, faculty: Optional[int] = None):
    return await client.all_groups(query=query, faculty=faculty)


@with_rest_client(GroupRestClient)
async def is_group_exists(client: GroupRestClient, query: str, faculty: Optional[int] = None):
    return await client.exists(group_code=query, faculty=faculty)
