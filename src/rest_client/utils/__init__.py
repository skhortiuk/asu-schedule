import datetime
import functools


def with_rest_client(rest_client, wrap_response=False):
    def wrapper(func):
        @functools.wraps(func)
        async def inner(*args, **kwargs):
            client = rest_client(kwargs["schedule_url"])
            response = await func(client, *args, **kwargs)
            if wrap_response:
                response = {
                    "response_time": datetime.datetime.utcnow(),
                    "data": response
                }
            return response

        return inner

    return wrapper
