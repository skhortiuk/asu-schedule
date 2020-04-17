from typing import Optional

from fastapi import APIRouter

from src.routesrs.schema import x_schedule_header
from src.controllers.group_controller import get_all_groups, is_group_exists

router = APIRouter()


@router.get("")
async def groups(*, query: Optional[str] = None, faculty: Optional[int] = None, schedule_url: str = x_schedule_header):
    return await get_all_groups(schedule_url=schedule_url, faculty=faculty, query=query)


@router.get("/exists")
async def group_exists(*, query: str, faculty: str, schedule_url: str = x_schedule_header):
    return await is_group_exists(query=query, faculty=faculty, schedule_url=schedule_url)
