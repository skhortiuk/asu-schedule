from src.rest_client.faculties import FacultiesRestClient
from src.rest_client.utils import with_rest_client, external_call
from src.common.parse import parse_faculties


@with_rest_client(FacultiesRestClient)
async def get_all_faculties(client: FacultiesRestClient, **kwargs):
    with external_call(client) as rest_client:
        data, status = await rest_client.all_faculties(**kwargs)
    return parse_faculties(data), status


@with_rest_client(FacultiesRestClient)
async def is_faculty_exists(client: FacultiesRestClient, query: str, **kwargs):
    with external_call(client) as rest_client:
        data, status = await rest_client.all_faculties(**kwargs)

    exists = False
    for faculty in parse_faculties(data):
        if query in faculty["name"]:
            exists = True
            break
    return {
               "exists": exists
           }, status
