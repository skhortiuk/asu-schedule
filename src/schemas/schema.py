from fastapi import Header
from validators.url import regex

from src.routes.config import SCHEDULE_HEADER_NAME

x_schedule_header = Header(..., alias=SCHEDULE_HEADER_NAME, regex=regex.pattern)
