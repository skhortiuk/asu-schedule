from fastapi import FastAPI

from src.routesrs import groups, teachers, schedule, faculties

app = FastAPI()

app.include_router(groups.router, prefix="/groups")
app.include_router(teachers.router, prefix="/teachers")
app.include_router(schedule.router, prefix="/schedule")
app.include_router(faculties.router, prefix="/faculties")
