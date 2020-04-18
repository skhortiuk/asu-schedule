from typing import Optional

from fastapi import APIRouter

from src.controllers.schedule_controller import get_group_schedule, get_teacher_schedule
from src.schemas.schema import x_schedule_header
from src.utils.events import Events
from src.utils.tracking import track

tag = "Schedule"
router = APIRouter()


@router.get("/groups", tags=[tag])
@track(
    fmt="value={value}, date_from={date_from}, date_to={date_to}",
    event=Events.GET_GROUPS_SCHEDULE,
)
async def groups_schedule(
    *,
    value: str,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    schedule_url: str = x_schedule_header
):
    return await get_group_schedule(
        from_date=date_from, to_date=date_to, group=value, schedule_url=schedule_url
    )


@router.get("/teachers", tags=[tag])
@track(
    fmt="value={value}, date_from={date_from}, date_to={date_to}",
    event=Events.GET_TEACHERS_SCHEDULE,
)
async def teachers_schedule(
    *,
    value: str,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    schedule_url: str = x_schedule_header
):
    return await get_teacher_schedule(
        from_date=date_from, to_date=date_to, teacher=value, schedule_url=schedule_url
    )
