import httpx
from app.core.config import (
    CELESTRAK_BASE_URL,
    DEFAULT_GROUP,
    DEFAULT_FORMAT,
    REQUEST_TIMEOUT,
)


class TLEProvider:
    """Retrieves raw TLE data from CelesTrak."""

    def get_station_tles(self) -> str:
        response = httpx.get(
            CELESTRAK_BASE_URL,
            params={
                "GROUP": DEFAULT_GROUP,
                "FORMAT": DEFAULT_FORMAT,
            },
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()

        return response.text