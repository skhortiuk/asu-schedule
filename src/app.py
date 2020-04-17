from http.client import INTERNAL_SERVER_ERROR

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

from src.rest_client.utils import ServiceUnavailableError
from src.routesrs import groups, teachers, schedule, faculties

app = FastAPI()


@app.exception_handler(ServiceUnavailableError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=INTERNAL_SERVER_ERROR, content={
            "message": exc.message
        }
    )


def custom_open_api():
    if not app.openapi_schema:
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
