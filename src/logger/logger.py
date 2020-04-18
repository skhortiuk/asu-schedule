import logging

from src.logger.handlers.statistics import StatisticsHandler
from src.rest_client.config import STATISTICS_URL
from src.rest_client.statistics.statistics import StatisticsRestClient

logger = logging.getLogger(__name__)
old_factory = logging.getLogRecordFactory()


def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    message = record.getMessage()
    if message.startswith("Stats"):
        record.track = True
        record.getMessage = lambda: message[6:]
    return record


def track(self, message, *, ip, event_type, level="info"):
    """
    Include the message to statistic.
    :param self: logger instance
    :param message: message to be logged (won't be a part of statistic)
    :param ip: IP address of user
    :param event_type: Desired event type
    :param level: log level

    Example:
        logger.track("Schedule requested.", ip=<user ip address>, event_type="Schedule Request")
    """
    getattr(self, level)("Stats " + message, extra={"ip": ip, "event_type": event_type})


formatter = logging.Formatter(
    fmt="Time: [{asctime}], Level: {levelname}, FIle: {filename}, Line {lineno}, Message: {message}",
    style="{",
)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

statistics_handler = StatisticsHandler(
    level=logging.INFO, rest_client=StatisticsRestClient(destination=STATISTICS_URL)
)

logger.addHandler(stream_handler)
logger.addHandler(statistics_handler)
logger.setLevel(logging.DEBUG)

logging.setLogRecordFactory(record_factory)
logging.Logger.track = track
