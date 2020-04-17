import logging

from src.logger.handlers import StatisticsHandler

logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    fmt="Time: [{asctime}], Level: {levelname}, FIle: {filename}, Line {lineno}, Message: {message}", style="{"
)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

statistics_handler = StatisticsHandler(level=logging.INFO)

logger.addHandler(stream_handler)
logger.addHandler(statistics_handler)
logger.setLevel(logging.DEBUG)

logger.debug(12)
