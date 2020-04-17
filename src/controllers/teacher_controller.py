from typing import Optional

from src.rest_client.teachers import TeachersRestClient
from src.rest_client.utils import with_rest_client


@with_rest_client(TeachersRestClient)
async def get_all_teachers(client: TeachersRestClient, faculty: Optional[int] = None,  **kwargs):
    return await client.all_teachers(faculty=faculty)
