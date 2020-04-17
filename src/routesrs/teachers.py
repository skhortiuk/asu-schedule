from typing import Optional

from fastapi import APIRouter

from src.controllers.teacher_controller import get_all_teachers
from src.routesrs.schema import x_schedule_header

router = APIRouter()


@router.get("")
async def teacher(*, faculty: Optional[int] = None, schedule_url: str = x_schedule_header):
    return await get_all_teachers(schedule_url=schedule_url, faculty=faculty)


@router.get("/exists")
async def teacher_exists(*, query: Optional[str] = None, schedule_url: str = x_schedule_header):
    return {"query": query, "schedule_url": schedule_url}
