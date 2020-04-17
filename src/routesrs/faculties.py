from typing import Optional

from fastapi import APIRouter

from src.schemas.schema import x_schedule_header

tag = "Faculties"
router = APIRouter()


@router.get("", tags=[tag])
async def groups(*, query: Optional[str] = None, schedule_url: str = x_schedule_header):
    return {"query": query, "schedule_url": schedule_url}


@router.get("/exists", tags=[tag])
async def group_exists(*, query: str, schedule_url: str = x_schedule_header):
    return {"query": query, "schedule_url": schedule_url}
