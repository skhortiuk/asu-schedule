from src.common.parse import parse
from src.rest_client.groups_schedule import GroupScheduleRestClient
from src.rest_client.utils import with_rest_client, external_call


@with_rest_client(GroupScheduleRestClient)
async def get_group_schedule(client: GroupScheduleRestClient, from_date: str, to_date: str, group: str):
    with external_call(client) as rest_client:
        data, status = await rest_client.schedule(from_date=from_date, to_date=to_date, value=group)
    return parse(data), status
