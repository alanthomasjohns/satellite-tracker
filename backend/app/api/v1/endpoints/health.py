from fastapi import APIRouter
from app.services.health_service import HealthService

router = APIRouter(tags=["Health"])
health_service = HealthService()


@router.get("/health")
def health_check():
    return health_service.get_status()