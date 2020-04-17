from fastapi import APIRouter

from src.schemas.schema import x_schedule_header
from src.controllers.faculties_controller import get_all_faculties, is_faculty_exists

tag = "Faculties"
router = APIRouter()


@router.get("", tags=[tag])
async def faculties(*, schedule_url: str = x_schedule_header):
    return await get_all_faculties(schedule_url=schedule_url)


@router.get("/exists", tags=[tag])
async def group_exists(*, query: str, schedule_url: str = x_schedule_header):
    return await is_faculty_exists(schedule_url=schedule_url, query=query)
