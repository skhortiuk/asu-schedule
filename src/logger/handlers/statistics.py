import asyncio
import logging
import os

from src.rest_client.statistics.statistics import StatisticsRestClient
from src.rest_client.utils import external_call


class StatisticsHandler(logging.Handler):
    """
    Custom logger handler to handle all messages with priority >= 20.
    Used to collect statistic.
    """

    def __init__(self, rest_client: StatisticsRestClient, *args, **kwargs):
        super(StatisticsHandler, self).__init__(*args, **kwargs)
        self.api_token = os.getenv("statistics_api_token")
        self.rest_client = rest_client

    def emit(self, record) -> None:
        if self.tracking_enabled(record):
            asyncio.get_event_loop().run_in_executor(None, self.track, record)

    @staticmethod
    def tracking_enabled(record):
        return getattr(record, "track", False)

    def track(self, record):
        with external_call(
            self.rest_client, error_message="Statistics unavailable"
        ) as client:
            asyncio.new_event_loop().run_until_complete(
                client.track_event(record.ip, record.event_type, self.api_token)
            )
