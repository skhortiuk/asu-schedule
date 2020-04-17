from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from src.routesrs import groups, teachers, schedule, faculties

app = FastAPI()


def custom_open_api():
    if app.openapi_schema:
        return app.openapi_schema
    open_api_schema = get_openapi(
        title="Ultimate Schedule API",
        version="1.0.0",
        description="Provides you possibility to interact with different university's schedules.",
        routes=app.routes,
    )
    app.openapi_schema = open_api_schema
    return app.openapi_schema


app.openapi = custom_open_api
app.include_router(groups.router, prefix="/groups")
app.include_router(teachers.router, prefix="/teachers")
app.include_router(schedule.router, prefix="/schedule")
app.include_router(faculties.router, prefix="/faculties")
