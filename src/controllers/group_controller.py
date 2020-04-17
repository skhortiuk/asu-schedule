from typing import Optional

from src.rest_client.groups import GroupRestClient
from src.rest_client.utils import with_rest_client, external_call


@with_rest_client(GroupRestClient)
async def get_all_groups(client: GroupRestClient, query: Optional[str] = None, faculty: Optional[int] = None, **kwargs):
    with external_call(client) as client:
        data, status = await client.all_groups(query=query, faculty=faculty)
    return data


@with_rest_client(GroupRestClient)
async def is_group_exists(client: GroupRestClient, query: str, faculty: Optional[int] = None, **kwargs):
    with external_call(client) as rest_client:
        data, status = await rest_client.exists(group_code=query, faculty=faculty)
        print(data, status)
    return data
