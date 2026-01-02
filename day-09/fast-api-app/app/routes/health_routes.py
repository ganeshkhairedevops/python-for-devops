from fastapi import APIRouter
from app.services.health_service import get_full_health

router = APIRouter()
# Route to get health check
@router.get("/health")
def health_check():
    return get_full_health()
