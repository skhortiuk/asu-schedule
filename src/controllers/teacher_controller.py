from typing import Optional

from src.rest_client.teachers import TeachersRestClient
from src.rest_client.utils import with_rest_client, external_call


@with_rest_client(TeachersRestClient)
async def get_all_teachers(
        client: TeachersRestClient, faculty: Optional[int] = None,
        query: Optional[str] = None, **kwargs
):
    with external_call(client) as rest_client:
        data, status = await rest_client.all_teachers(faculty=faculty, query=query)
    return data, status


@with_rest_client(TeachersRestClient)
async def is_teacher_exists(
        client: TeachersRestClient, faculty: Optional[int] = None,
        teacher: Optional[str] = None, **kwargs
):
    with external_call(client) as rest_client:
        data, status = await rest_client.exists(faculty=faculty, teacher=teacher)
    return data, status
