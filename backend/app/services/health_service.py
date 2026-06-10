from datetime import UTC, datetime


class HealthService:
    def get_status(self) -> dict:
        return {
            "status": "healthy",
            "service": "satellite-tracker",
            "version": "0.1.0",
            "timestamp": datetime.now(UTC).isoformat(),
        }