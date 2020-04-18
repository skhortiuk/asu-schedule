from typing import Optional

from src.rest_client.groups.groups import GroupRestClient
from src.rest_client.utils import with_rest_client, external_call


@with_rest_client(GroupRestClient)
async def get_all_groups(
    client: GroupRestClient,
    query: Optional[str] = None,
    faculty: Optional[int] = None,
    **kwargs
):
    with external_call(client) as rest_client:
        data, status = await rest_client.all_groups(query=query, faculty=faculty)
    return data, status


@with_rest_client(GroupRestClient)
async def is_group_exists(
    client: GroupRestClient, group: str, faculty: Optional[int] = None, **kwargs
):
    with external_call(client) as rest_client:
        data, status = await rest_client.exists(group_code=group, faculty=faculty)
    return data, status
