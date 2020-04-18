import contextvars

from fastapi import Request

client_ip = contextvars.ContextVar("client_ip_address")


async def statistics_middleware(request: Request, call_next):
    client_ip.set(request.client.host)
    return await call_next(request)
