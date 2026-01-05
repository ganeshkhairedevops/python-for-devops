from fastapi import APIRouter
from app.services.aws_service import get_aws_resources

router = APIRouter()
# Route to get AWS resources
@router.get("/aws")
def aws_resources():
    return get_aws_resources()
