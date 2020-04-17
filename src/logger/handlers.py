import logging


class StatisticsHandler(logging.Handler):
    """
    Custom logger handler to handle all messages with priority >= 20.
    Used to collect statistic.
    """

    def emit(self, record: logging.LogRecord) -> None:
        print(record)
        self.track(record)

    def track(self, record):  # noqa
        return NotImplemented
