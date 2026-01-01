from fastapi import APIRouter
from app.services.health_service import get_full_health

router = APIRouter()

@router.get("/health")
def health_check():
    return get_full_health()
