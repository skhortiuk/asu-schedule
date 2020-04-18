import functools

from src.logger.logger import logger

base_fmt = "Schedule URL: {schedule_url}. Params: [{fmt}]. Event: {event}"


def track(fmt, event):
    def wrapper(func):
        @functools.wraps(func)
        async def inner(*args, **kwargs):
            message = base_fmt.format(fmt=fmt.format(**kwargs), event=event, **kwargs)
            logger.track(message, event_type=event)
            return await func(*args, **kwargs)

        return inner

    return wrapper
