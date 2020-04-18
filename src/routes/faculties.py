from fastapi import APIRouter
from src.utils.events import Events
from src.schemas.schema import x_schedule_header
from src.controllers.faculties_controller import get_all_faculties, is_faculty_exists
from src.utils.tracking import track

tag = "Faculties"
router = APIRouter()


@router.get("", tags=[tag])
@track(fmt="", event=Events.GET_ALL_FACULTIES)
async def faculties(*, schedule_url: str = x_schedule_header):
    return await get_all_faculties(schedule_url=schedule_url)


@router.get("/exists", tags=[tag])
@track(fmt="query={query}", event=Events.IS_FACULTY_EXISTS)
async def faculty_exists(*, query: str, schedule_url: str = x_schedule_header):
    return await is_faculty_exists(schedule_url=schedule_url, query=query)
