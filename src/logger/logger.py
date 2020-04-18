import logging

from src.logger.handlers import StatisticsHandler

logger = logging.getLogger(__name__)
old_factory = logging.getLogRecordFactory()


def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    message = record.getMessage()
    if message.startswith("Stats"):
        record.track = True
        record.getMessage = lambda: message[6:]
    return record


def track(self, message, level="info"):
    getattr(self, level)("Stats " + message)


formatter = logging.Formatter(
    fmt="Time: [{asctime}], Level: {levelname}, FIle: {filename}, Line {lineno}, Message: {message}",
    style="{",
)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

statistics_handler = StatisticsHandler(level=logging.INFO)

logger.addHandler(stream_handler)
logger.addHandler(statistics_handler)
logger.setLevel(logging.DEBUG)

logging.setLogRecordFactory(record_factory)
logging.Logger.track = track
