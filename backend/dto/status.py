from pydantic import BaseModel
from datetime import datetime, timezone

class Status(BaseModel):
    status: int
    timestamp: datetime = datetime.now(timezone.utc)

class StatusCountResponse(BaseModel):
    count: int
