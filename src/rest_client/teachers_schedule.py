from src.rest_client.base_schedule_client import ScheduleBaseRestClient


class TeacherScheduleRestClient(ScheduleBaseRestClient):
    ENTITY = "teacher"
