from typing import Optional

from fastapi import APIRouter

from src.routesrs.schema import x_schedule_header

router = APIRouter()


@router.get("/")
async def groups(*, query: Optional[str] = None, schedule_url: str = x_schedule_header):
    return {"query": query, "schedule_url": schedule_url}


@router.get("/exists")
async def group_exists(*, query: str, schedule_url: str = x_schedule_header):
    return {"query": query, "schedule_url": schedule_url}
