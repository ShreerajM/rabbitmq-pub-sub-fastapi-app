from fastapi import APIRouter
from datetime import datetime
from db import get_collection
from dto.status import StatusCountResponse
from db.status import get_status_between
status_router = APIRouter()

collection = get_collection()


@status_router.get("/status_count", response_model=StatusCountResponse)
async def get_status_count(start: datetime, end: datetime):
    statuses = get_status_between(start,end)
    count = sum(status["status"] for status in statuses)
    return StatusCountResponse(count=count) 
