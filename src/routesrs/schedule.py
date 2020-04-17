from fastapi import APIRouter

from src.controllers.schedule_controller import get_group_schedule
from src.routesrs.schema import x_schedule_header

router = APIRouter()


@router.get("/groups")
async def groups_schedule(
        *, value: str, date_from: str, date_to: str,
        schedule_url: str = x_schedule_header
):
    return await get_group_schedule(
        from_date=date_from, to_date=date_to, group=value, schedule_url=schedule_url
    )
