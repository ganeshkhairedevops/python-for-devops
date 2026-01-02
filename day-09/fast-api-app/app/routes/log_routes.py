from fastapi import APIRouter
from app.services.log_service import analyze_logs

router = APIRouter()
# Route to get log analysis
@router.get("/logs")
def logs():
    return {"log_summary": analyze_logs()}
