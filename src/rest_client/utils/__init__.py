import contextlib
import datetime
import functools

from src.common.errors import BaseCustomException


class ServiceUnavailableError(BaseCustomException):
    def __init__(self, message, status, response):
        super(ServiceUnavailableError, self).__init__(message)
        self.status = status
        self.response = response

    def json(self):
        return {
            "message": self.message,
            "status": self.status,
            "response": self.response,
        }


def with_rest_client(rest_client, wrap_response=True):
    def wrapper(func):
        @functools.wraps(func)
        async def inner(*args, **kwargs):
            client = rest_client(kwargs["schedule_url"])
            response, status = await func(client, *args, **kwargs)
            if wrap_response:
                response = {
                    "response_time": datetime.datetime.utcnow().isoformat(),
                    "data": response,
                }
            return response

        return inner

    return wrapper


class WrappedRestClient:
    def __init__(self, rest_client):
        self.data = None
        self.status = None
        self.rest_client = rest_client

    def __getattr__(self, item):
        self._method = item
        return self.patched

    async def patched(self, *args, **kwargs):
        method = getattr(self.rest_client, self._method)
        response = await method(*args, **kwargs)
        self.data, self.status = response
        return self.data, self.status


@contextlib.contextmanager
def external_call(
    rest_client, allowed_statuses=(200,), error_message="Service unavailable."
):
    wrapped_client = WrappedRestClient(rest_client)
    try:
        yield wrapped_client
    finally:
        if wrapped_client.status not in allowed_statuses:
            raise ServiceUnavailableError(
                error_message,
                status=wrapped_client.status,
                response=wrapped_client.data,
            )
