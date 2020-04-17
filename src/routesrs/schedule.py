from typing import Optional

from fastapi import APIRouter

from src.controllers.schedule_controller import get_group_schedule, get_teacher_schedule
from src.schemas.schema import x_schedule_header

tag = "Schedule"
router = APIRouter()


@router.get("/groups", tags=[tag])
async def groups_schedule(
        *, value: str, date_from: Optional[str] = None, date_to: Optional[str] = None,
        schedule_url: str = x_schedule_header
):
    return await get_group_schedule(
        from_date=date_from, to_date=date_to, group=value, schedule_url=schedule_url
    )


@router.get("/teachers", tags=[tag])
async def teachers_schedule(
        *, value: str, date_from: Optional[str] = None, date_to: Optional[str] = None,
        schedule_url: str = x_schedule_header
):
    return await get_teacher_schedule(
        from_date=date_from, to_date=date_to, teacher=value, schedule_url=schedule_url
    )
