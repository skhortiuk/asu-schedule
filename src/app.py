from http.client import INTERNAL_SERVER_ERROR

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse, RedirectResponse

from src.common.errors import ParsingError
from src.logger.logger import logger
from src.middlewares.statistics import statistics_middleware
from src.rest_client.utils import ServiceUnavailableError
from src.routesrs import groups, teachers, schedule, faculties

app = FastAPI()


@app.exception_handler(ParsingError)
@app.exception_handler(ServiceUnavailableError)
async def validation_exception_handler(request, exc):
    logger.exception(exc)
    return JSONResponse(status_code=INTERNAL_SERVER_ERROR, content=exc.json())


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
app.middleware("http")(statistics_middleware)
app.add_middleware(CORSMiddleware, allow_origins=["*"])
app.include_router(groups.router, prefix="/groups")
app.include_router(teachers.router, prefix="/teachers")
app.include_router(schedule.router, prefix="/schedule")
app.include_router(faculties.router, prefix="/faculties")


@app.get("/")
async def docs_redirect():
    return RedirectResponse("/docs")
