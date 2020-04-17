from src.rest_client.base_schedule_client import ScheduleBaseRestClient


class GroupScheduleRestClient(ScheduleBaseRestClient):
    ENTITY = "group"
