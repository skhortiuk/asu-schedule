from typing import Optional

from fastapi import APIRouter

from src.routesrs.schema import x_schedule_header

router = APIRouter()


@router.get("/")
async def faculties(*, value: str, date_from: Optional[str] = None, date_to: Optional[str] = None,
                    schedule_url: str = x_schedule_header):
    return {"value": value, "date_from": date_from, "date_to": date_to, "schedule_url": schedule_url}


@router.get("/exists")
async def faculties_exists(*, value: str, date_from: Optional[str] = None, date_to: Optional[str] = None,
                           schedule_url: str = x_schedule_header):
    return {"value": value, "date_from": date_from, "date_to": date_to, "schedule_url": schedule_url}
