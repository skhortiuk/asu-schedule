from src.rest_client.schedule.base import ScheduleBaseRestClient


class GroupScheduleRestClient(ScheduleBaseRestClient):
    ENTITY = "group"
