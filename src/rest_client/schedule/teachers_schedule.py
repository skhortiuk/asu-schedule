from src.rest_client.schedule.base import ScheduleBaseRestClient


class TeacherScheduleRestClient(ScheduleBaseRestClient):
    ENTITY = "teacher"
