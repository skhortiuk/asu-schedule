import logging


class StatisticsHandler(logging.Handler):
    """
    Custom logger handler to handle all messages with priority >= 20.
    Used to collect statistic.
    """

    def emit(self, record: logging.LogRecord) -> None:
        if self.tracking_enabled(record):
            self.track(record)

    @staticmethod
    def tracking_enabled(record):
        return getattr(record, "track", False)

    def track(self, record):  # noqa
        return NotImplemented
