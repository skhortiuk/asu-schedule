from fastapi import APIRouter

from src.routes.v1 import schedule, teachers, faculties, groups

router_v1 = APIRouter()

router_v1.include_router(groups.router, prefix="/groups")
router_v1.include_router(teachers.router, prefix="/teachers")
router_v1.include_router(schedule.router, prefix="/schedule")
router_v1.include_router(faculties.router, prefix="/faculties")
