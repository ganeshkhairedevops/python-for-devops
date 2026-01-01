from fastapi import APIRouter
from app.services.awsservice import get_aws_resources

router = APIRouter()

@router.get("/aws")
def aws_resources():
    return get_aws_resources()
