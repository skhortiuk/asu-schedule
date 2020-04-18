from src.rest_client.base import BaseRestClient


class StatisticsRestClient(BaseRestClient):
    async def track_event(self, ip, event_type, token):
        return await self.post(
            json=self.build_event(ip, event_type, token), mime_type="application/json"
        )

    @staticmethod
    def build_event(ip, event_type, token):
        return {
            "api_key": token,
            "events": [{"ip": ip, "event_type": event_type, "user_id": ip}],
        }
