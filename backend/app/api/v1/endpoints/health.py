from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "satellite-tracker",
        "version": "0.1.0",
    }